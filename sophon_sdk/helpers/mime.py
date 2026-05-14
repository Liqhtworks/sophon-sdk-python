"""MIME-type helper for upload sources."""

from __future__ import annotations

import mimetypes
import os
from pathlib import Path
from typing import Union

_FALLBACK = "application/octet-stream"


def guess_mime_type(path: Union[str, Path], default: str = _FALLBACK) -> str:
    """Return a best-effort MIME type for ``path`` using stdlib
    ``mimetypes.guess_type``. Falls back to ``default`` (octet-stream by
    default) when the suffix is unknown."""
    guess, _ = mimetypes.guess_type(os.fspath(path))
    return guess or default
