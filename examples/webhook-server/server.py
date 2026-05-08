import json
import os

from fastapi import FastAPI, HTTPException, Request, Response

import sophon_sdk


SECRET = os.environ["SOPHON_WEBHOOK_SECRET"]
app = FastAPI()


@app.post("/webhooks/sophon", status_code=204)
async def sophon_webhook(request: Request) -> Response:
    raw_body = await request.body()

    try:
        sophon_sdk.verify_webhook_signature(
            raw_body,
            request.headers.get("X-Turbo-Signature-256"),
            request.headers.get("X-Turbo-Timestamp"),
            SECRET,
        )
    except sophon_sdk.WebhookSignatureError as exc:
        print("rejected SOPHON webhook", {"reason": exc.reason})
        raise HTTPException(status_code=401, detail="invalid signature") from exc

    event = json.loads(raw_body)
    print("accepted SOPHON webhook", {"type": event.get("type"), "id": event.get("id")})

    return Response(status_code=204)
