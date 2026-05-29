"""Output download helper for completed jobs.

`GET /v1/jobs/{id}/output` returns a 302 to a presigned URL with a TTL.
This helper follows the redirect and exposes the underlying response so
callers can stream straight to disk, S3, or any other sink without
reimplementing the no-redirect / follow-redirect dance.

Security: the presigned target is validated before it is fetched. Only
``https://`` URLs whose host is on an allowlist (Backblaze B2 by default,
plus the configured API host) are followed, and the download itself does
not chase any further redirect. This bounds the helper to "exactly one
redirect, to an allowlisted host" and stops a compromised or spoofed API
response from turning the helper into an open redirect follower or an
SSRF / local-file (``file://``) reader.
"""

from __future__ import annotations

import urllib.parse
import urllib.request
from dataclasses import dataclass
from http.client import HTTPResponse
from pathlib import Path
from typing import Iterable, Optional, Union


# Presigned outputs are served from Backblaze B2. Any host ending in one of
# these suffixes (or matching it exactly, sans leading dot) is accepted.
_DEFAULT_OUTPUT_HOST_SUFFIXES = (".backblazeb2.com",)


class DownloadSecurityError(ValueError):
    """Raised when the resolved output URL fails the scheme/host allowlist."""


@dataclass
class DownloadResult:
    bytes: int
    path: Optional[Path]


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):  # type: ignore[no-untyped-def]
        response = urllib.request.addinfourl(fp, headers, req.get_full_url())
        response.code = code  # type: ignore[attr-defined]
        return response

    http_error_301 = http_error_303 = http_error_307 = http_error_302


def _allowed_hosts(base_url: str, extra: Optional[Iterable[str]]) -> tuple[set[str], tuple[str, ...]]:
    """Return (exact_hosts, suffixes) the resolved output URL may use.

    The API host from ``base_url`` is always allowed (the API may serve the
    bytes itself instead of redirecting). Callers can extend the set via
    ``extra``: an entry beginning with ``"."`` is treated as a host suffix,
    otherwise as an exact host match.
    """
    exact: set[str] = set()
    suffixes: list[str] = list(_DEFAULT_OUTPUT_HOST_SUFFIXES)

    base_host = urllib.parse.urlsplit(base_url).hostname
    if base_host:
        exact.add(base_host.lower())

    for entry in extra or ():
        entry = entry.strip().lower()
        if not entry:
            continue
        if entry.startswith("."):
            suffixes.append(entry)
        else:
            exact.add(entry)
    return exact, tuple(suffixes)


def _validate_download_url(
    url: str, *, base_url: str, allowed_output_hosts: Optional[Iterable[str]]
) -> None:
    """Raise :class:`DownloadSecurityError` unless ``url`` is an https URL on
    an allowlisted host."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme.lower() != "https":
        raise DownloadSecurityError(
            f"refusing to download output from non-https URL (scheme={parts.scheme!r})"
        )
    host = (parts.hostname or "").lower()
    if not host:
        raise DownloadSecurityError("refusing to download output URL with no host")

    exact, suffixes = _allowed_hosts(base_url, allowed_output_hosts)
    if host in exact:
        return
    for suffix in suffixes:
        # ".backblazeb2.com" matches "f004.backblazeb2.com" and "backblazeb2.com".
        if host == suffix.lstrip(".") or host.endswith(suffix):
            return
    raise DownloadSecurityError(
        f"refusing to download output from non-allowlisted host {host!r}"
    )


def download_output_stream(
    *,
    base_url: str,
    api_key: str,
    job_id: str,
    timeout_seconds: float = 60.0,
    allowed_output_hosts: Optional[Iterable[str]] = None,
) -> HTTPResponse:
    """Resolve the presigned URL for job `job_id` and return an open
    streaming response. Callers are responsible for closing it
    (use ``with download_output_stream(...) as resp:``).

    The presigned URL is validated (https + allowlisted host) before it is
    fetched, and no further redirect is followed. Pass ``allowed_output_hosts``
    to extend the allowlist (exact host, or ``".example.com"`` as a suffix).
    """
    location = _resolve_location(
        base_url=base_url, api_key=api_key, job_id=job_id, timeout=timeout_seconds
    )
    download_url = urllib.parse.urljoin(base_url.rstrip("/") + "/", location)
    _validate_download_url(
        download_url, base_url=base_url, allowed_output_hosts=allowed_output_hosts
    )

    # Fetch with a no-redirect opener so a second-hop redirect from the
    # presigned host is not blindly chased to an arbitrary location.
    opener = urllib.request.build_opener(_NoRedirectHandler())
    response = opener.open(download_url, timeout=timeout_seconds)
    status = getattr(response, "status", None) or getattr(response, "code", None)
    if isinstance(status, int) and 300 <= status < 400:
        try:
            response.close()
        except Exception:
            pass
        raise DownloadSecurityError(
            f"refusing to follow a second redirect from the output URL (status={status})"
        )
    return response  # type: ignore[return-value]


def download_output(
    *,
    base_url: str,
    api_key: str,
    job_id: str,
    dest: Union[str, Path],
    timeout_seconds: float = 60.0,
    chunk_bytes: int = 1024 * 1024,
    allowed_output_hosts: Optional[Iterable[str]] = None,
) -> DownloadResult:
    """Download job output to ``dest`` (file path). Streams in chunks so
    multi-GB outputs do not buffer in memory. Returns total bytes written.
    """
    dest_path = Path(dest)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    with download_output_stream(
        base_url=base_url,
        api_key=api_key,
        job_id=job_id,
        timeout_seconds=timeout_seconds,
        allowed_output_hosts=allowed_output_hosts,
    ) as response, open(dest_path, "wb") as fh:
        while True:
            chunk = response.read(chunk_bytes)
            if not chunk:
                break
            fh.write(chunk)
            total += len(chunk)
    return DownloadResult(bytes=total, path=dest_path)


def _resolve_location(*, base_url: str, api_key: str, job_id: str, timeout: float) -> str:
    req = urllib.request.Request(
        f"{base_url.rstrip('/')}/v1/jobs/{job_id}/output",
        headers={"Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    opener = urllib.request.build_opener(_NoRedirectHandler())
    redirect = opener.open(req, timeout=timeout)
    location = redirect.headers.get("Location")
    if not location:
        raise RuntimeError(f"job {job_id}: GET /v1/jobs/{{id}}/output did not return a Location header")
    return location
