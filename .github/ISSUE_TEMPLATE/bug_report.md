---
name: Bug report
about: Something the SDK does that contradicts the docs or its type hints.
title: "[bug] "
labels: bug
---

## What happened

<!-- What you tried to do, what the SDK did instead. -->

## Reproducer

```python
# Minimum code that reproduces. Strip secrets.
from sophon_sdk import ApiClient, Configuration, JobsApi
# …
```

## Environment

- `sophon-sdk` version: `0.1.x` (from `pip show sophon-sdk`)
- Python version: `…`
- OS: `…`

## Expected vs. actual

- Expected: `…`
- Actual: `…` (paste traceback inside a fenced block)

## Anything else

<!-- Logs, X-Request-Id headers from the response, etc. -->
