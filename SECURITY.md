# Security Policy

## Supported versions

`sophon-sdk` is in the `v0.x` pre-1.0 phase. Security fixes are shipped on
the **latest `0.1.x` patch release**. Pin a compatible range and stay current:

```bash
pip install "sophon-sdk~=0.1"
```

| Version | Supported |
|---------|-----------|
| latest `0.1.x` | ✅ |
| older `0.1.x` | ⚠️ upgrade to the latest patch |
| `< 0.1` | ❌ |

## Reporting a vulnerability

**Please do not open a public GitHub issue for security reports.**

Report privately through one of:

1. **GitHub private vulnerability reporting** (preferred) — on the
   [`Liqhtworks/sophon-sdk-python`](https://github.com/Liqhtworks/sophon-sdk-python)
   repo, go to **Security → Report a vulnerability**.
2. **Email** `support@sophon.rs` with `SECURITY` in the subject. Include a
   description, affected version, and reproduction steps.

We aim to acknowledge a report within **3 business days** and to provide a
remediation timeline after triage. Please give us a reasonable window to ship
a fix before any public disclosure (coordinated disclosure).

## Scope

This policy covers the `sophon-sdk` Python package in this repository. Issues
in the SOPHON Encoding API itself (`api.liqhtworks.xyz`) or the web app should
be reported through the same channels and will be routed to the platform team.

## What's in scope for this SDK

- Leaking the API key (logs, URLs, telemetry, exceptions).
- Transport security regressions (disabling TLS verification by default,
  plaintext fallback).
- Following the job-output redirect to a non-allowlisted host or scheme
  (SSRF / local-file / open redirect).
- Webhook signature verification weaknesses (non-constant-time compare,
  missing replay protection).
- Vulnerable transitive dependencies.

## Handling API keys safely

- Keep keys server-side. Never ship them in client apps, public repos, logs,
  or analytics events.
- Scope keys to the least privilege your integration needs.
- Rotate keys on a schedule and immediately on suspected exposure. See the
  **Security** section of [`README.md`](./README.md) for the rotation steps.
