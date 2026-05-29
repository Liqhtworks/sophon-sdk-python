# coding: utf-8

# flake8: noqa

"""Official Python SDK for the SOPHON Encoding API."""

from importlib import metadata as _metadata

try:
    __version__ = _metadata.version("sophon_sdk")
except _metadata.PackageNotFoundError:
    __version__ = "0.0.0+unknown"

# Define package exports
__all__ = [
    "DownloadsApi",
    "HealthApi",
    "JobsApi",
    "UploadsApi",
    "WebhooksApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "CompleteUploadResponse",
    "CreateJobOutputOptions",
    "CreateJobRequest",
    "CreateUploadRequest",
    "CreateUploadResponse",
    "CreateWebhookRequest",
    "ErrorBody",
    "ErrorEnvelope",
    "JobOutputInfo",
    "JobProfile",
    "JobProgress",
    "JobResponse",
    "JobSourceInfo",
    "JobSourceType",
    "JobStatus",
    "ListJobsResponse",
    "OutputContainer",
    "ReadyResponse",
    "UploadJobSource",
    "UploadPartResponse",
    "UploadStatusResponse",
    "WebhookDeliveryPayload",
    "WebhookListItem",
    "WebhookListResponse",
    "WebhookResponse",
    # Helpers
    "DownloadResult",
    "DownloadSecurityError",
    "JobSource",
    "JobsApiLike",
    "JobTerminalError",
    "JobTimeoutError",
    "TERMINAL_STATUSES",
    "UploadFileResult",
    "UploadProgress",
    "UploadsApiLike",
    "WebhookSignatureError",
    "create_job",
    "download_output",
    "download_output_stream",
    "guess_mime_type",
    "upload_file",
    "upload_job_source",
    "verify_webhook_signature",
    "wait_for_job",
    # Profile string constants
    "JOB_PROFILE_SOPHON_ESPRESSO",
    "JOB_PROFILE_SOPHON_CORTADO",
    "JOB_PROFILE_SOPHON_AMERICANO",
    "JOB_PROFILE_SOPHON_ESPRESSO_HQ",
    "JOB_PROFILE_SOPHON_CORTADO_HQ",
    "JOB_PROFILE_SOPHON_AMERICANO_HQ",
    "JOB_PROFILE_SOPHON_ESPRESSO_10BIT",
    "JOB_PROFILE_SOPHON_CORTADO_10BIT",
    "JOB_PROFILE_SOPHON_AMERICANO_10BIT",
    "JOB_PROFILE_SOPHON_ESPRESSO_HQ_10BIT",
    "JOB_PROFILE_SOPHON_CORTADO_HQ_10BIT",
    "JOB_PROFILE_SOPHON_AMERICANO_HQ_10BIT",
    "JOB_PROFILE_SOPHON_AUTO",
]

# import apis into sdk package
from sophon_sdk.api.downloads_api import DownloadsApi as DownloadsApi
from sophon_sdk.api.health_api import HealthApi as HealthApi
from sophon_sdk.api.jobs_api import JobsApi as JobsApi
from sophon_sdk.api.uploads_api import UploadsApi as UploadsApi
from sophon_sdk.api.webhooks_api import WebhooksApi as WebhooksApi

# import ApiClient
from sophon_sdk.api_response import ApiResponse as ApiResponse
from sophon_sdk.api_client import ApiClient as ApiClient
from sophon_sdk.configuration import Configuration as Configuration
from sophon_sdk.exceptions import OpenApiException as OpenApiException
from sophon_sdk.exceptions import ApiTypeError as ApiTypeError
from sophon_sdk.exceptions import ApiValueError as ApiValueError
from sophon_sdk.exceptions import ApiKeyError as ApiKeyError
from sophon_sdk.exceptions import ApiAttributeError as ApiAttributeError
from sophon_sdk.exceptions import ApiException as ApiException

# import models into sdk package
from sophon_sdk.models.complete_upload_response import CompleteUploadResponse as CompleteUploadResponse
from sophon_sdk.models.create_job_output_options import CreateJobOutputOptions as CreateJobOutputOptions
from sophon_sdk.models.create_job_request import CreateJobRequest as CreateJobRequest
from sophon_sdk.models.create_upload_request import CreateUploadRequest as CreateUploadRequest
from sophon_sdk.models.create_upload_response import CreateUploadResponse as CreateUploadResponse
from sophon_sdk.models.create_webhook_request import CreateWebhookRequest as CreateWebhookRequest
from sophon_sdk.models.error_body import ErrorBody as ErrorBody
from sophon_sdk.models.error_envelope import ErrorEnvelope as ErrorEnvelope
from sophon_sdk.models.job_output_info import JobOutputInfo as JobOutputInfo
from sophon_sdk.models.job_profile import JobProfile as JobProfile
from sophon_sdk.models.job_progress import JobProgress as JobProgress
from sophon_sdk.models.job_response import JobResponse as JobResponse
from sophon_sdk.models.job_source_info import JobSourceInfo as JobSourceInfo
from sophon_sdk.models.job_source_type import JobSourceType as JobSourceType
from sophon_sdk.models.job_status import JobStatus as JobStatus
from sophon_sdk.models.list_jobs_response import ListJobsResponse as ListJobsResponse
from sophon_sdk.models.output_container import OutputContainer as OutputContainer
from sophon_sdk.models.ready_response import ReadyResponse as ReadyResponse
from sophon_sdk.models.upload_job_source import UploadJobSource as UploadJobSource
from sophon_sdk.models.upload_part_response import UploadPartResponse as UploadPartResponse
from sophon_sdk.models.upload_status_response import UploadStatusResponse as UploadStatusResponse
from sophon_sdk.models.webhook_delivery_payload import WebhookDeliveryPayload as WebhookDeliveryPayload
from sophon_sdk.models.webhook_list_item import WebhookListItem as WebhookListItem
from sophon_sdk.models.webhook_list_response import WebhookListResponse as WebhookListResponse
from sophon_sdk.models.webhook_response import WebhookResponse as WebhookResponse


# --- Hand-written helpers (spliced in by api/sdk/generate.sh) ------------
from sophon_sdk.helpers import (  # noqa: E402,F401
    CreateJobApiLike,
    DownloadResult,
    DownloadSecurityError,
    JobSource,
    JobTerminalError,
    JobTimeoutError,
    JobsApiLike,
    TERMINAL_STATUSES,
    UploadFileResult,
    UploadProgress,
    UploadsApiLike,
    WebhookSignatureError,
    create_job,
    download_output,
    download_output_stream,
    guess_mime_type,
    upload_job_source,
    upload_file,
    verify_webhook_signature,
    wait_for_job,
)

# --- Profile string constants ---------------------------------------------
# JobProfile enum names are mangled by the OpenAPI generator (hyphens
# become "MINUS"). These autocomplete-friendly aliases let callers write
# JOB_PROFILE_SOPHON_ESPRESSO instead of JobProfile.SOPHON_MINUS_ESPRESSO,
# while keeping the canonical "profile names are strings" contract.
JOB_PROFILE_SOPHON_ESPRESSO = "sophon-espresso"
JOB_PROFILE_SOPHON_CORTADO = "sophon-cortado"
JOB_PROFILE_SOPHON_AMERICANO = "sophon-americano"
JOB_PROFILE_SOPHON_ESPRESSO_HQ = "sophon-espresso-hq"
JOB_PROFILE_SOPHON_CORTADO_HQ = "sophon-cortado-hq"
JOB_PROFILE_SOPHON_AMERICANO_HQ = "sophon-americano-hq"
JOB_PROFILE_SOPHON_ESPRESSO_10BIT = "sophon-espresso-10bit"
JOB_PROFILE_SOPHON_CORTADO_10BIT = "sophon-cortado-10bit"
JOB_PROFILE_SOPHON_AMERICANO_10BIT = "sophon-americano-10bit"
JOB_PROFILE_SOPHON_ESPRESSO_HQ_10BIT = "sophon-espresso-hq-10bit"
JOB_PROFILE_SOPHON_CORTADO_HQ_10BIT = "sophon-cortado-hq-10bit"
JOB_PROFILE_SOPHON_AMERICANO_HQ_10BIT = "sophon-americano-hq-10bit"
JOB_PROFILE_SOPHON_AUTO = "sophon-auto"
