# sophon-sdk

Official Python SDK for the SOPHON Encoding API.

This repository is generated from `Liqhtworks/sophon-api`. The curated
`README.md` and `examples/` directory are preserved across SDK regeneration.

## Install

```bash
pip install sophon-sdk
```

Requires Python 3.9+.

## Get an API key

1. Sign in at <https://sophon.rs/account/general>.
2. In **API keys**, create a key for your server-side integration.
3. Copy the `xt_live_...` token when it is shown. It is only shown once.
4. Store it as an environment variable:

```bash
export SOPHON_API_KEY=xt_live_...
export SOPHON_BASE_URL=https://api.liqhtworks.xyz
```

Keep API keys on the server. Do not ship them in client apps, public repos,
logs, or analytics events.

## Quick Start

This is the smallest complete server-side flow: upload a local video, create an
encode job, wait for completion, and download the MP4 output.

```python
import os
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

import sophon_sdk
from sophon_sdk.models.create_job_request import CreateJobRequest

api_key = os.environ["SOPHON_API_KEY"]
base_url = os.getenv("SOPHON_BASE_URL", "https://api.liqhtworks.xyz")
input_path = Path("source.mov")
mime_type = "video/quicktime" if input_path.suffix == ".mov" else "video/mp4"


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        response = urllib.request.addinfourl(fp, headers, req.get_full_url())
        response.code = code
        return response

    http_error_301 = http_error_303 = http_error_307 = http_error_302


configuration = sophon_sdk.Configuration(
    host=base_url,
    access_token=api_key,
)

with sophon_sdk.ApiClient(configuration) as api_client:
    uploads = sophon_sdk.UploadsApi(api_client)
    jobs = sophon_sdk.JobsApi(api_client)

    result = sophon_sdk.upload_file(
        uploads,
        input_path,
        file_name=input_path.name,
        mime_type=mime_type,
        concurrency=4,
    )

    job = sophon_sdk.create_job(
        jobs,
        idempotency_key=str(uuid.uuid4()),
        create_job_request=CreateJobRequest(
            source=sophon_sdk.JobSource.upload(result.upload_id),
            profile="sophon-espresso",
        ),
    )

    final = sophon_sdk.wait_for_job(
        jobs,
        job.id,
        timeout_seconds=30 * 60,
    )
    if final.status != "completed":
        raise RuntimeError(f"job ended in {final.status}")

    req = urllib.request.Request(
        f"{base_url}/v1/jobs/{final.id}/output",
        headers={"Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    opener = urllib.request.build_opener(NoRedirectHandler())
    redirect = opener.open(req)
    location = redirect.headers.get("Location")
    if not location:
        raise RuntimeError("missing output redirect")

    download_url = urllib.parse.urljoin(base_url.rstrip("/") + "/", location)
    with urllib.request.urlopen(download_url, timeout=60) as download:
        Path("sophon-output.mp4").write_bytes(download.read())

    print(f"wrote sophon-output.mp4 from {final.id}")
```

For a runnable copy of this flow, see
[`examples/encode_file.py`](./examples/encode_file.py).

### Profile choice

Use `sophon-auto` for production unless you need deterministic encoder
settings. The quickstart uses `sophon-espresso` because it is the fastest
smoke-test profile and always produces a new encoded output.

## Upload Input Forms

`upload_file` accepts all common server-side input forms:

```python
from io import BytesIO
from pathlib import Path

# 1. Path-like input.
sophon_sdk.upload_file(
    uploads,
    Path("source.mov"),
    file_name="source.mov",
    mime_type="video/quicktime",
)

# 2. Bytes input.
data = Path("source.mov").read_bytes()
sophon_sdk.upload_file(
    uploads,
    data,
    file_name="source.mov",
    mime_type="video/quicktime",
)

# 3. Binary file-like input. The object must support seek().
with open("source.mov", "rb") as fh:
    sophon_sdk.upload_file(
        uploads,
        fh,
        file_name="source.mov",
        mime_type="video/quicktime",
    )

# BytesIO works too.
buf = BytesIO(data)
sophon_sdk.upload_file(
    uploads,
    buf,
    file_name="source.mov",
    mime_type="video/quicktime",
)
```

## Webhooks

Use `verify_webhook_signature` with the raw request body before JSON parsing.

See [`examples/webhook-server`](./examples/webhook-server) for a FastAPI route
that reads the raw body, verifies `X-Turbo-Signature-256`, and only then parses
JSON.

## Helpers

| Helper | Purpose |
|---|---|
| `upload_file` | Chunked upload orchestration with bounded concurrency, retries, resume, and progress callbacks. |
| `wait_for_job` | Poll until terminal status with timeout and typed errors. |
| `verify_webhook_signature` | Constant-time HMAC verification plus replay-window enforcement. |

## API Docs

Generated endpoint/model docs live under [`docs/`](./docs).

## Versioning

`sophon-sdk` follows [SemVer](https://semver.org/), with one pre-1.0
caveat: while we are at `v0.x`, **minor bumps may include breaking
changes**. Pin a compatible range until 1.0:

```bash
pip install "sophon-sdk~=0.1"
# or in pyproject.toml: "sophon-sdk>=0.1,<0.2"
```

Patch releases (`0.1.x`) are always backward-compatible — they ship bug
fixes, helper-layer improvements, and additive types. Once we cut
`v1.0.0`, regular SemVer applies and breaking changes only land on
major bumps. See [`CHANGELOG.md`](./CHANGELOG.md) for the per-release
log.

## License

Apache License 2.0. See [`LICENSE`](./LICENSE).
