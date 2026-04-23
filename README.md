# sophon-sdk

Official Python SDK for the [SOPHON Encoding API](https://liqhtworks.xyz).

> **This package is generated.** Source lives in [Liqhtworks/sophon-api](https://github.com/Liqhtworks/sophon-api) (`api/openapi.yaml` + `api/sdk/helpers/python/`). Do not edit files in this repository by hand — changes are overwritten on every release.

## Install

```bash
pip install sophon-sdk
# or
uv add sophon-sdk
```

## Quick start

```python
import os
import uuid
from sophon_sdk import (
    ApiClient, Configuration,
    JobsApi, UploadsApi,
    upload_file, wait_for_job, verify_webhook_signature,
)

config = Configuration(
    host="https://api.liqhtworks.xyz",
    access_token=os.environ["SOPHON_API_KEY"],
)
client = ApiClient(config)
uploads = UploadsApi(client)
jobs = JobsApi(client)

# 1. Upload a file (chunked, concurrent, resumable).
result = upload_file(
    uploads,
    "/path/to/source.mov",
    file_name="source.mov",
    mime_type="video/quicktime",
    on_progress=lambda p: print(f"{p.parts_done}/{p.parts_total}"),
)

# 2. Start an encode.
job = jobs.create_job(
    idempotency_key=str(uuid.uuid4()),
    create_job_request={
        "source": {"type": "upload", "upload_id": result.upload_id},
        "profile": "sophon-auto",
    },
)

# 3. Wait for it to finish.
done = wait_for_job(jobs, job.id)
print(done.status)  # "completed"
```

## Webhook verification

```python
from sophon_sdk import verify_webhook_signature

# In your webhook handler — `raw_body` MUST be the raw bytes, not parsed JSON.
verify_webhook_signature(
    raw_body,
    signature_header=request.headers.get("X-Turbo-Signature-256"),
    timestamp_header=request.headers.get("X-Turbo-Timestamp"),
    secret=os.environ["SOPHON_WEBHOOK_SECRET"],
)
```

## Runtime support

- Python 3.9+

## License

Proprietary — see [`LICENSE`](./LICENSE).
