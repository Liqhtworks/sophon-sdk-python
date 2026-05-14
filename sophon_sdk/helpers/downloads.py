"""Output download helper for completed jobs.

`GET /v1/jobs/{id}/output` returns a 302 to a presigned URL with a TTL.
This helper follows the redirect and exposes the underlying response so
callers can stream straight to disk, S3, or any other sink without
reimplementing the no-redirect / follow-redirect dance.
"""

from __future__ import annotations

import shutil
import urllib.parse
import urllib.request
from dataclasses import dataclass
from http.client import HTTPResponse
from pathlib import Path
from typing import Optional, Union


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


def download_output_stream(
    *,
    base_url: str,
    api_key: str,
    job_id: str,
    timeout_seconds: float = 60.0,
) -> HTTPResponse:
    """Resolve the presigned URL for job `job_id` and return an open
    streaming response. Callers are responsible for closing it
    (use ``with download_output_stream(...) as resp:``).
    """
    location = _resolve_location(
        base_url=base_url, api_key=api_key, job_id=job_id, timeout=timeout_seconds
    )
    download_url = urllib.parse.urljoin(base_url.rstrip("/") + "/", location)
    return urllib.request.urlopen(download_url, timeout=timeout_seconds)  # type: ignore[return-value]


def download_output(
    *,
    base_url: str,
    api_key: str,
    job_id: str,
    dest: Union[str, Path],
    timeout_seconds: float = 60.0,
    chunk_bytes: int = 1024 * 1024,
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
