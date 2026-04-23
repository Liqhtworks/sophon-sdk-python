"""Webhook signature verification for inbound terminal-job deliveries.

SOPHON signs each delivery with HMAC-SHA256 over ``f"{timestamp}.{raw_body}"``
using the per-webhook secret. The hex digest is sent as
``X-Turbo-Signature-256: sha256=<hex>``.

Consumers call :func:`verify_webhook_signature` with the RAW request body
(bytes or str — NOT a parsed dict), the signature header, the timestamp
header, and the webhook secret. The helper does a constant-time comparison
and enforces a replay window by default.
"""

from __future__ import annotations

import hmac
import time
from datetime import datetime, timezone
from hashlib import sha256
from typing import Callable, Optional, Union


class WebhookSignatureError(Exception):
    """Raised when a delivery cannot be authenticated."""

    REASONS = frozenset(
        {
            "missing_signature",
            "missing_timestamp",
            "invalid_timestamp",
            "replay_window_exceeded",
            "bad_prefix",
            "bad_signature_encoding",
            "signature_mismatch",
        }
    )

    def __init__(self, reason: str, message: Optional[str] = None):
        if reason not in self.REASONS:
            raise ValueError(f"unknown reason: {reason}")
        super().__init__(message or reason)
        self.reason = reason


def verify_webhook_signature(
    raw_body: Union[bytes, bytearray, str],
    signature_header: Optional[str],
    timestamp_header: Optional[str],
    secret: str,
    *,
    replay_window_seconds: float = 5 * 60,
    now: Optional[Callable[[], float]] = None,
) -> None:
    """Raise :class:`WebhookSignatureError` if the delivery is not authentic.

    ``raw_body`` must be the raw bytes (or the string representation of them)
    exactly as received — do not pass a parsed JSON object.
    """
    if not signature_header:
        raise WebhookSignatureError("missing_signature")
    if not timestamp_header:
        raise WebhookSignatureError("missing_timestamp")

    delivered_ts = _parse_rfc3339(timestamp_header)
    if delivered_ts is None:
        raise WebhookSignatureError("invalid_timestamp")

    current_time = (now or time.time)()

    if replay_window_seconds > 0:
        drift = abs(current_time - delivered_ts)
        if drift > replay_window_seconds:
            raise WebhookSignatureError("replay_window_exceeded")

    if not signature_header.startswith("sha256="):
        raise WebhookSignatureError("bad_prefix")
    delivered_hex = signature_header[len("sha256=") :].strip()

    try:
        delivered = bytes.fromhex(delivered_hex)
    except ValueError as exc:
        raise WebhookSignatureError("bad_signature_encoding") from exc

    body_bytes = raw_body.encode("utf-8") if isinstance(raw_body, str) else bytes(raw_body)
    payload = f"{timestamp_header}.".encode("utf-8") + body_bytes

    expected = hmac.new(secret.encode("utf-8"), payload, sha256).digest()

    if not hmac.compare_digest(delivered, expected):
        raise WebhookSignatureError("signature_mismatch")


def _parse_rfc3339(value: str) -> Optional[float]:
    """Parse an RFC 3339 / ISO 8601 timestamp to a UTC epoch float."""
    # Python 3.11+ parses the trailing "Z"; older versions need it normalized.
    normalized = value.replace("Z", "+00:00") if value.endswith("Z") else value
    try:
        dt = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.timestamp()
