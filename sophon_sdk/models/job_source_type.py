# coding: utf-8

"""SOPHON Encoding API client (generated)."""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class JobSourceType(str, Enum):
    """
    Discriminator for `JobSource` variants.
    """

    """
    allowed enum values
    """
    UPLOAD = 'upload'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobSourceType from a JSON string"""
        return cls(json.loads(json_str))


