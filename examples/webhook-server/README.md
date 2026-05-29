# Webhook receiver example

A minimal FastAPI route that verifies SOPHON webhook deliveries **before**
parsing them. This is the reference for the security-critical pattern: verify
the HMAC signature over the raw request body, then parse.

## Run

```bash
pip install fastapi uvicorn
export SOPHON_WEBHOOK_SECRET=whsec_...   # shown once when you create the webhook
uvicorn app:app --port 8000
```

Expose the port (e.g. with a tunnel) and register the public URL as your
webhook endpoint via the SOPHON API. Point it at `/webhooks/sophon`.

## Why verify the raw body

`verify_webhook_signature` recomputes `HMAC-SHA256("{timestamp}.{raw_body}")`
and compares it to `X-Turbo-Signature-256` in constant time. If you parse the
JSON first and re-serialize it, the bytes change (key order, whitespace) and
the signature will never match. Always pass the **raw** bytes, exactly as
received, and reject the delivery if verification fails — only then parse.

The helper also enforces a replay window (5 minutes by default) using the
signed timestamp, so a captured-and-replayed delivery is rejected.
