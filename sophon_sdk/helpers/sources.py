"""Job source constructors."""

from __future__ import annotations

from typing import Dict


def upload_job_source(upload_id: str) -> Dict[str, str]:
    return {"type": "upload", "upload_id": upload_id}


class JobSource:
    @staticmethod
    def upload(upload_id: str) -> Dict[str, str]:
        return upload_job_source(upload_id)
