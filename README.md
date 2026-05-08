# sophon-sdk

Official Python SDK for the SOPHON Encoding API.

This repository is generated from `Liqhtworks/sophon-api`. The curated
`README.md` and `examples/` directory are preserved across SDK regeneration.

## Install

```bash
pip install sophon-sdk
```

Requires Python 3.9+.

## Quick Start

```python
import os
from pathlib import Path

import sophon_sdk

configuration = sophon_sdk.Configuration(
    host=os.getenv("SOPHON_BASE_URL", "https://api.liqhtworks.xyz"),
    access_token=os.environ["SOPHON_API_KEY"],
)

with sophon_sdk.ApiClient(configuration) as api_client:
    uploads = sophon_sdk.UploadsApi(api_client)

    result = sophon_sdk.upload_file(
        uploads,
        Path("source.mov"),
        file_name="source.mov",
        mime_type="video/quicktime",
        concurrency=4,
    )

    print(result.upload_id)
```

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

## License

Proprietary. See [`LICENSE`](./LICENSE).
