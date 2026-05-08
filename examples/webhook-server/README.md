# FastAPI Webhook Server

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
SOPHON_WEBHOOK_SECRET=whsec_... uvicorn server:app --reload
```

Register `POST /webhooks/sophon` as the webhook endpoint. The route calls
`await request.body()` before parsing JSON so signature verification receives
the original request bytes.
