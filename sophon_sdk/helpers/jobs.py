"""Polling helper that resolves when a job hits a terminal state."""

from __future__ import annotations

import math
import threading
import time
from typing import Any, Callable, Iterable, Optional, Protocol


TERMINAL_STATUSES: frozenset[str] = frozenset({"completed", "failed", "canceled"})


class JobsApiLike(Protocol):
    def get_job(self, id: str) -> Any: ...


class CreateJobApiLike(Protocol):
    def create_job(self, *, idempotency_key: str, create_job_request: Any) -> Any: ...


class JobTerminalError(RuntimeError):
    """Raised when the job reaches failed/canceled and the caller was
    waiting for the default terminal set."""

    def __init__(self, job: Any):
        self.job = job
        status = _attr(job, "status")
        err = _attr(job, "error")
        super().__init__(err or f"job {_attr(job, 'id')} ended in status {status}")


class JobTimeoutError(TimeoutError):
    def __init__(self, job_id: str, waited_ms: int):
        self.job_id = job_id
        self.waited_ms = waited_ms
        super().__init__(f"job {job_id} did not finish within {waited_ms}ms")


def wait_for_job(
    api: JobsApiLike,
    job_id: str,
    *,
    until: Optional[Iterable[str]] = None,
    poll_min_seconds: float = 1.0,
    poll_max_seconds: float = 15.0,
    poll_backoff: float = 1.5,
    timeout_seconds: float = 3600.0,
    on_progress: Optional[Callable[[Any], None]] = None,
    stop_event: Optional[threading.Event] = None,
) -> Any:
    """Poll ``api.get_job(job_id)`` until the job hits a terminal status (or
    a caller-specified ``until`` set), then return the final job.

    Raises ``JobTerminalError`` on ``failed``/``canceled`` when using the
    default terminal set. Raises ``JobTimeoutError`` if the deadline elapses.
    """
    wait_set = frozenset(until) if until is not None else TERMINAL_STATUSES
    using_default_terminal = until is None
    stop = stop_event or threading.Event()

    start_time = time.monotonic()
    deadline = start_time + timeout_seconds
    interval = poll_min_seconds

    while True:
        if stop.is_set():
            raise RuntimeError("wait_for_job aborted")
        if time.monotonic() > deadline:
            waited_ms = int((time.monotonic() - start_time) * 1000)
            raise JobTimeoutError(job_id, waited_ms)

        job = api.get_job(id=job_id)
        _normalize_status(job)
        if on_progress:
            on_progress(job)

        status = _status_str(_attr(job, "status"))
        if status in wait_set:
            if using_default_terminal and status in {"failed", "canceled"}:
                raise JobTerminalError(job)
            return job

        _interruptible_sleep(interval, stop)
        interval = min(math.ceil(interval * poll_backoff * 1000) / 1000.0, poll_max_seconds)


def create_job(
    api: CreateJobApiLike,
    *,
    idempotency_key: str,
    create_job_request: Any,
) -> Any:
    """Create a job after normalizing omitted metadata to an empty object."""
    _coerce_metadata_default(create_job_request)
    return api.create_job(
        idempotency_key=idempotency_key,
        create_job_request=create_job_request,
    )


def _coerce_metadata_default(create_job_request: Any) -> None:
    if isinstance(create_job_request, dict):
        if create_job_request.get("metadata") is None:
            create_job_request["metadata"] = {}
        return

    if getattr(create_job_request, "metadata", None) is None:
        setattr(create_job_request, "metadata", {})


def _interruptible_sleep(seconds: float, stop: threading.Event) -> None:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if stop.wait(min(0.1, deadline - time.monotonic())):
            return


def _attr(obj: Any, name: str) -> Any:
    if isinstance(obj, dict):
        return obj.get(name)
    return getattr(obj, name, None)


def _normalize_status(job: Any) -> None:
    """Coerce a job's status field to a plain string for cross-SDK parity
    with Go (Go's helpers.Job.Status is a string). Mutates dicts in place;
    bypasses pydantic validate_assignment via object.__setattr__ so a
    JobStatus(str, Enum) field on JobResponse is replaced with its .value."""
    if isinstance(job, dict):
        if "status" in job:
            job["status"] = _status_str(job["status"])
        return
    status = getattr(job, "status", None)
    # Plain str (type, not isinstance — JobStatus is str-subclass) → no-op.
    if status is None or type(status) is str:
        return
    try:
        object.__setattr__(job, "status", _status_str(status))
    except Exception:
        pass


def _status_str(status: Any) -> Any:
    """Normalize a JobStatus enum to its string value so callers and
    comparisons see the wire string regardless of whether the underlying
    api.get_job returned an enum or a plain dict with a raw status."""
    value = getattr(status, "value", status)
    return value
