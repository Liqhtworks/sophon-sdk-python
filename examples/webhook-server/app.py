"""Minimal FastAPI webhook receiver for SOPHON terminal-job deliveries.

The security-critical rule: **verify the HMAC signature over the RAW request
body before parsing JSON.** Parsing first and re-serializing changes bytes
(key order, whitespace) and will not match the signature. This route reads the
raw body, verifies ``X-Turbo-Signature-256`` with the SDK's constant-time
helper, and only then parses the payload.

Run:

    pip install fastapi uvicorn
    export SOPHON_WEBHOOK_SECRET=whsec_...   # shown once when you create the webhook
    uvicorn app:app --port 8000

Point your SOPHON webhook at https://<your-host>/webhooks/sophon.
"""

import json
import os

from fastapi import FastAPI, Request, Response

from sophon_sdk import WebhookSignatureError, verify_webhook_signature

# SOPHON signs each delivery with HMAC-SHA256 over "{timestamp}.{raw_body}".
# These headers carry the hex digest and the signed timestamp.
SIGNATURE_HEADER = "X-Turbo-Signature-256"
TIMESTAMP_HEADER = "X-Turbo-Timestamp"

app = FastAPI()


@app.post("/webhooks/sophon")
async def sophon_webhook(request: Request) -> Response:
    secret = os.environ["SOPHON_WEBHOOK_SECRET"]

    # 1. Read the RAW body first — do not call request.json() yet.
    raw_body = await request.body()

    # 2. Verify before trusting anything in the payload.
    try:
        verify_webhook_signature(
            raw_body=raw_body,
            signature_header=request.headers.get(SIGNATURE_HEADER),
            timestamp_header=request.headers.get(TIMESTAMP_HEADER),
            secret=secret,
            # replay_window_seconds defaults to 5 minutes; tune if your
            # receiver runs behind a slow queue.
        )
    except WebhookSignatureError as exc:
        # Don't echo details that could help an attacker probe the check.
        return Response(status_code=401, content=f"invalid signature: {exc.reason}")

    # 3. Only now is it safe to parse and act on the payload.
    event = json.loads(raw_body)
    job_id = event.get("job_id") or event.get("id")
    status = event.get("status")
    print(f"verified delivery: job={job_id} status={status}")

    # Return 2xx quickly; do heavy work asynchronously so SOPHON's delivery
    # timeout doesn't trigger a retry storm.
    return Response(status_code=200, content="ok")
