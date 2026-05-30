"""Upload orchestration on top of the generated UploadsApi.

The generated SDK exposes create_upload / upload_part / complete_upload as
separate calls; this wrapper handles chunk slicing, bounded concurrency,
per-part retry, resume against existing sessions, and progress reporting.
"""

from __future__ import annotations

import io
import os
import random
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any, BinaryIO, Callable, Optional, Protocol, Union


class UploadsApiLike(Protocol):
    def create_upload(
        self, create_upload_request: Any, idempotency_key: str
    ) -> Any: ...

    def upload_part(self, id: str, part_number: int, body: bytes) -> Any: ...

    def complete_upload(self, id: str, idempotency_key: str) -> Any: ...

    def get_upload(self, id: str) -> Any: ...


@dataclass
class UploadProgress:
    bytes_uploaded: int
    bytes_total: int
    parts_done: int
    parts_total: int


@dataclass
class UploadFileResult:
    upload_id: str
    sha256: str
    bytes: int


# Sentinel used so callers can disable retries with retries=0 without the
# default kicking in, while keeping the default at 3 for retries=None.
_DEFAULT_RETRIES = 3
_RETRYABLE_STATUSES = {408, 429}


def _is_retryable(exc: BaseException) -> bool:
    """Treat network errors + 5xx/429/408 as retryable."""
    if isinstance(exc, (ConnectionError, TimeoutError)):
        return True
    status = getattr(exc, "status", None)
    if status is None:
        status = getattr(getattr(exc, "response", None), "status", None)
    if isinstance(status, int):
        return status in _RETRYABLE_STATUSES or 500 <= status < 600
    return False


def _with_retry(
    fn: Callable[[], Any], retries: int, base_ms: int, stop: threading.Event
) -> Any:
    attempt = 0
    while True:
        if stop.is_set():
            raise RuntimeError("upload aborted")
        try:
            return fn()
        except BaseException as exc:
            if stop.is_set() or attempt >= retries or not _is_retryable(exc):
                raise
            delay_ms = base_ms * (2 ** attempt) + random.randint(0, base_ms)
            _interruptible_sleep(delay_ms / 1000.0, stop)
            attempt += 1


def _interruptible_sleep(seconds: float, stop: threading.Event) -> None:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if stop.wait(min(0.1, deadline - time.monotonic())):
            return


def _source_size_and_reader(
    source: Union[bytes, bytearray, BinaryIO, Path, str]
) -> tuple[int, Callable[[int, int], bytes], Callable[[], None]]:
    """Return (size, slice_reader(start, end), close). The reader returns bytes
    for [start, end) and must be thread-safe against concurrent callers."""
    if isinstance(source, (bytes, bytearray)):
        buf = bytes(source)

        def read_bytes(a: int, b: int) -> bytes:
            return buf[a:b]

        return len(buf), read_bytes, lambda: None

    if isinstance(source, (str, Path)):
        path = os.fspath(source)
        size = os.path.getsize(path)
        lock = threading.Lock()
        fh = open(path, "rb")  # noqa: SIM115 — closed via returned callback

        def read_path(a: int, b: int) -> bytes:
            with lock:
                fh.seek(a)
                return fh.read(b - a)

        return size, read_path, fh.close

    # Generic BinaryIO. We need size: prefer len() of a bytes-backed stream,
    # else seek-to-end. For thread safety we serialize reads via a lock.
    lock = threading.Lock()
    if hasattr(source, "getbuffer"):
        size = len(source.getbuffer())  # type: ignore[attr-defined]
    else:
        cur = source.tell()
        source.seek(0, io.SEEK_END)
        size = source.tell()
        source.seek(cur)

    def read_stream(a: int, b: int) -> bytes:
        with lock:
            source.seek(a)
            return source.read(b - a)

    return size, read_stream, lambda: None


def upload_file(
    api: UploadsApiLike,
    source: Union[bytes, bytearray, BinaryIO, Path, str],
    *,
    file_name: str,
    mime_type: Optional[str] = None,
    upload_id: Optional[str] = None,
    concurrency: int = 4,
    retries: int = _DEFAULT_RETRIES,
    retry_base_ms: int = 500,
    idempotency_key: Optional[str] = None,
    on_progress: Optional[Callable[[UploadProgress], None]] = None,
    stop_event: Optional[threading.Event] = None,
) -> UploadFileResult:
    """Upload ``source`` as a new or resumed chunked upload and return its
    final id / sha256 / bytes.

    ``source`` accepts bytes, a file path (str or Path), or an open binary
    file-like object. The file-like object must support .seek().
    """
    if concurrency < 1:
        raise ValueError("concurrency must be >= 1")
    if retries < 0:
        raise ValueError("retries must be >= 0")

    idem = idempotency_key or f"idem-{uuid.uuid4()}"
    stop = stop_event or threading.Event()

    if mime_type is None:
        from .mime import guess_mime_type
        mime_type = guess_mime_type(file_name)

    size, slice_reader, close_source = _source_size_and_reader(source)
    if size == 0:
        close_source()
        raise ValueError("upload_file: source is empty (0 bytes)")

    try:
        already_received: set[int] = set()
        if upload_id is not None:
            status = api.get_upload(id=upload_id)
            session_id = _attr(status, "id")
            total_chunks = int(_attr(status, "total_chunks"))
            already_received = set(
                int(p) for p in (_attr(status, "received_chunks") or [])
            )
            chunk_size = (size + total_chunks - 1) // total_chunks
        else:
            req = {
                "file_name": file_name,
                "file_size": size,
                "mime_type": mime_type,
            }
            # SOPHON scopes idempotency keys per-route. Same key on
            # createUpload + completeUpload returns 409. Derive distinct
            # per-route keys from the caller's seed so retries still work.
            session = _with_retry(
                lambda: api.create_upload(
                    create_upload_request=req, idempotency_key=f"{idem}/create"
                ),
                retries=retries,
                base_ms=retry_base_ms,
                stop=stop,
            )
            session_id = _attr(session, "id")
            chunk_size = int(_attr(session, "chunk_size"))
            total_chunks = int(_attr(session, "total_chunks"))

        progress = UploadProgress(
            bytes_uploaded=0,
            bytes_total=size,
            parts_done=0,
            parts_total=total_chunks,
        )
        for part in already_received:
            progress.parts_done += 1
            progress.bytes_uploaded += _part_bytes(
                size, chunk_size, total_chunks, part
            )
        if on_progress:
            on_progress(UploadProgress(**progress.__dict__))

        progress_lock = threading.Lock()

        def upload_one(part_number: int) -> None:
            if stop.is_set():
                raise RuntimeError("upload aborted")
            start = part_number * chunk_size
            end = min(start + chunk_size, size)
            chunk = slice_reader(start, end)

            _with_retry(
                lambda: api.upload_part(
                    id=session_id, part_number=part_number, body=chunk
                ),
                retries=retries,
                base_ms=retry_base_ms,
                stop=stop,
            )

            with progress_lock:
                progress.parts_done += 1
                progress.bytes_uploaded += end - start
                if on_progress:
                    on_progress(UploadProgress(**progress.__dict__))

        pending = [
            i for i in range(total_chunks) if i not in already_received
        ]
        if pending:
            with ThreadPoolExecutor(
                max_workers=min(concurrency, len(pending))
            ) as pool:
                for res in pool.map(upload_one, pending):
                    del res  # propagate exceptions eagerly

        done = _with_retry(
            lambda: api.complete_upload(
                id=session_id, idempotency_key=f"{idem}/complete"
            ),
            retries=retries,
            base_ms=retry_base_ms,
            stop=stop,
        )
        return UploadFileResult(
            upload_id=_attr(done, "id"),
            sha256=_attr(done, "sha256"),
            bytes=int(_attr(done, "bytes")),
        )
    finally:
        close_source()


def _part_bytes(total: int, chunk_size: int, total_chunks: int, part: int) -> int:
    if part < total_chunks - 1:
        return chunk_size
    return total - chunk_size * (total_chunks - 1)


def _attr(obj: Any, name: str) -> Any:
    """Support both pydantic-style models (attributes) and dicts."""
    if isinstance(obj, dict):
        return obj.get(name)
    return getattr(obj, name, None)
