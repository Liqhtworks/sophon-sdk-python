# coding: utf-8

"""SOPHON Encoding API client (generated)."""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class JobStatus(str, Enum):
    """
    Lifecycle status for an encoding job.
    """

    """
    allowed enum values
    """
    QUEUED = 'queued'
    PROBING = 'probing'
    ENCODING = 'encoding'
    MUXING = 'muxing'
    UPLOADING_OUTPUT = 'uploading_output'
    COMPLETED = 'completed'
    FAILED = 'failed'
    CANCELED = 'canceled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobStatus from a JSON string"""
        return cls(json.loads(json_str))


