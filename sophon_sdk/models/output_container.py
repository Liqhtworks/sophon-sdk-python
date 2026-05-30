# coding: utf-8

"""SOPHON Encoding API client (generated)."""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class OutputContainer(str, Enum):
    """
    Output container format. MP4 is widely compatible; MKV supports a broader range of audio codecs for passthrough. 
    """

    """
    allowed enum values
    """
    MP4 = 'mp4'
    MKV = 'mkv'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OutputContainer from a JSON string"""
        return cls(json.loads(json_str))


