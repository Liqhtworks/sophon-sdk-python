"""Job source constructors."""

from __future__ import annotations

from sophon_sdk.models.job_source_type import JobSourceType
from sophon_sdk.models.upload_job_source import UploadJobSource


def upload_job_source(upload_id: str) -> UploadJobSource:
    return UploadJobSource(type=JobSourceType.UPLOAD, upload_id=upload_id)


class JobSource:
    @staticmethod
    def upload(upload_id: str) -> UploadJobSource:
        return upload_job_source(upload_id)
