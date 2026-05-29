"""Security tests for the output-download helper's URL allowlist.

These cover the P1 finding: the helper must follow exactly one redirect and
only to an allowlisted https host, never to file://, an internal host, or an
attacker-chosen redirect target.
"""

import pytest

from sophon_sdk.helpers import downloads
from sophon_sdk.helpers.downloads import DownloadSecurityError, _validate_download_url

BASE = "https://api.liqhtworks.xyz"


@pytest.mark.parametrize(
    "url",
    [
        "https://f004.backblazeb2.com/file/bucket/out.mp4",
        "https://bucket.s3.us-west-002.backblazeb2.com/out.mp4",
        "https://backblazeb2.com/out.mp4",
        "https://api.liqhtworks.xyz/v1/jobs/abc/output.mp4",  # API host itself
    ],
)
def test_allows_https_allowlisted_hosts(url):
    _validate_download_url(url, base_url=BASE, allowed_output_hosts=None)


@pytest.mark.parametrize(
    "url",
    [
        "http://f004.backblazeb2.com/out.mp4",  # plaintext
        "file:///etc/passwd",  # local file read
        "ftp://f004.backblazeb2.com/out.mp4",  # non-https scheme
        "https://169.254.169.254/latest/meta-data/",  # cloud metadata SSRF
        "https://evil.example.com/out.mp4",  # arbitrary host
        "https://backblazeb2.com.evil.com/out.mp4",  # suffix-spoof
        "https://localhost/out.mp4",
    ],
)
def test_rejects_disallowed_urls(url):
    with pytest.raises(DownloadSecurityError):
        _validate_download_url(url, base_url=BASE, allowed_output_hosts=None)


def test_extra_allowlist_extends_hosts():
    url = "https://cdn.example.com/out.mp4"
    with pytest.raises(DownloadSecurityError):
        _validate_download_url(url, base_url=BASE, allowed_output_hosts=None)
    # exact-host opt-in
    _validate_download_url(url, base_url=BASE, allowed_output_hosts=["cdn.example.com"])
    # suffix opt-in
    _validate_download_url(url, base_url=BASE, allowed_output_hosts=[".example.com"])


def test_stream_rejects_malicious_redirect_before_fetch(monkeypatch):
    """A spoofed/compromised API 302 to file:// or an internal host must be
    refused before any second-hop network/file access is attempted."""
    calls = {"opened": 0}

    def fake_resolve(*, base_url, api_key, job_id, timeout):
        return "file:///etc/passwd"

    def fake_open(*args, **kwargs):  # pragma: no cover - must never run
        calls["opened"] += 1
        raise AssertionError("opener.open must not be called for a bad URL")

    monkeypatch.setattr(downloads, "_resolve_location", fake_resolve)
    monkeypatch.setattr(
        downloads.urllib.request, "build_opener", lambda *a, **k: type("O", (), {"open": staticmethod(fake_open)})()
    )

    with pytest.raises(DownloadSecurityError):
        downloads.download_output_stream(
            base_url=BASE, api_key="xt_live_x", job_id="job123"
        )
    assert calls["opened"] == 0
