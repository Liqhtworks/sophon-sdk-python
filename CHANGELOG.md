# Changelog

All notable changes to `sophon-sdk` (PyPI) are recorded here. The
package follows [SemVer](https://semver.org/) — see `README.md` for the
versioning policy applied during the v0.x pre-1.0 phase.

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

[0.1.4]: https://github.com/Liqhtworks/sophon-sdk-python/releases/tag/v0.1.4
[0.1.2]: https://github.com/Liqhtworks/sophon-sdk-python/releases/tag/v0.1.2
[0.1.0]: https://github.com/Liqhtworks/sophon-sdk-python/releases/tag/v0.1.0
