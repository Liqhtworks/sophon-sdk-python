# Changelog

All notable changes to `sophon-sdk` (PyPI) are recorded here. The
package follows [SemVer](https://semver.org/) — see `README.md` for the
versioning policy applied during the v0.x pre-1.0 phase.

## [0.1.5] — 2026-05-14

- `download_output` / `download_output_stream` helpers — follow the
  `GET /v1/jobs/{id}/output` redirect and stream the encoded MP4 to a
  destination path (or expose the open response for custom sinks). No
  more redirect-handling boilerplate in caller code.
- `guess_mime_type(path)` helper; `upload_file`'s `mime_type` is now
  optional and inferred from the file name when omitted.
- `upload_file` now retries `create_upload` and `complete_upload` (not
  just `upload_part`). A transient 5xx/429/network blip at session
  open or finalize no longer kills an otherwise-successful upload.
- `upload_file` rejects zero-byte sources client-side with a clear
  `ValueError` instead of bouncing off the server's generic file_size
  validation.
- `JobSource.upload(upload_id)` and `upload_job_source(upload_id)` now
  return a typed `UploadJobSource` pydantic model instead of a plain
  dict — static type checkers and IDE autocomplete see the model.
- `wait_for_job` normalizes the job's `status` to a plain string before
  invoking `on_progress`, matching the Go SDK's `helpers.Job.Status`
  contract for cross-SDK consumers. `JobTimeoutError.waited_ms` is now
  derived from a captured start time rather than `deadline - timeout`
  round-trip math.
- Module docstrings no longer embed the full Daisy integration
  walkthrough — `help()` and IDE hover output are usable again.
- `__version__` reads from `importlib.metadata` so it always tracks
  `pyproject.toml`.
- `JOB_PROFILE_SOPHON_*` string constants exposed on the package for
  autocomplete-friendly profile selection alongside the existing
  (string-typed) wire contract.
- `pyproject.toml` no longer mixes Poetry blocks with the setuptools
  build backend; dev dependencies live under
  `[project.optional-dependencies].dev`. Author email is a real
  Liqhtworks address.

## [0.1.4] — 2026-05-08

- `JobSource.upload(upload_id)` constructor — typed alternative to the
  fragile `{"type": "upload", "upload_id": "..."}` literal.
- `create_job(metadata=None)` now normalizes to `{}` before the wire
  call. Earlier releases let `None` through and the API rejected it with
  HTTP 400 on the spec's `required: [metadata]` rule.
- Generated and helper exports tightened so the customer-facing surface
  is reachable from `sophon_sdk` directly without deep imports.

## [0.1.2] — 2026-04-23

- Per-route idempotency keys in `upload_file`. Earlier releases reused
  one key for both `create_upload` and `complete_upload`; SOPHON scopes
  idempotency keys per route and rejected the second call with HTTP 409.
  Now derives `f"{idem}/create"` and `f"{idem}/complete"` from the
  caller's seed so retries still reach the server's idempotent path.

## [0.1.0] — 2026-04-23

Initial public release.

- Generated transport (`ApiClient`, `Configuration`, `JobsApi`,
  `UploadsApi`, `WebhooksApi`, `DownloadsApi`, `HealthApi`) from the
  SOPHON OpenAPI spec.
- Hand-written helpers exposed at the top of the package:
  - `upload_file` — chunked, concurrent, resumable upload that accepts
    bytes, a `pathlib.Path`, or a binary file-like. Progress callback,
    bounded retry, AbortEvent support.
  - `wait_for_job` — typed terminal-state polling with backoff and
    timeout.
  - `verify_webhook_signature` — constant-time HMAC-SHA256 verification
    with a default replay window.
- Published via PyPI's trusted-publisher OIDC flow.

[0.1.5]: https://github.com/Liqhtworks/sophon-sdk-python/releases/tag/v0.1.5
[0.1.4]: https://github.com/Liqhtworks/sophon-sdk-python/releases/tag/v0.1.4
[0.1.2]: https://github.com/Liqhtworks/sophon-sdk-python/releases/tag/v0.1.2
[0.1.0]: https://github.com/Liqhtworks/sophon-sdk-python/releases/tag/v0.1.0
