# coding: utf-8

"""SOPHON Encoding API client (generated)."""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class JobOutputInfo(BaseModel):
    """
    JobOutputInfo
    """ # noqa: E501
    state: StrictStr
    container: StrictStr = Field(description="Output container format (\"mp4\" or \"mkv\").")
    audio: StrictBool = Field(description="Whether the output file actually contains audio. Reflects the muxed result, not the request flag — a video-only source with audio requested will report false. ")
    target_height: Optional[StrictInt] = Field(default=None, description="Customer-requested output height, echoed back. Null when the job ran at source dimensions (passthrough). ")
    width: Optional[StrictInt] = Field(default=None, description="Actual encoded output width in pixels (post-ffprobe). Null until the job completes or if the probe failed. ")
    height: Optional[StrictInt] = Field(default=None, description="Actual encoded output height in pixels. See `width`.")
    bytes: Optional[StrictInt] = None
    sha256: Optional[StrictStr] = None
    retention_expires_at: Optional[datetime] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["state", "container", "audio", "target_height", "width", "height", "bytes", "sha256", "retention_expires_at"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pending', 'available']):
            raise ValueError("must be one of enum values ('pending', 'available')")
        return value

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of JobOutputInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobOutputInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "state": obj.get("state"),
            "container": obj.get("container"),
            "audio": obj.get("audio"),
            "target_height": obj.get("target_height"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "bytes": obj.get("bytes"),
            "sha256": obj.get("sha256"),
            "retention_expires_at": obj.get("retention_expires_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


