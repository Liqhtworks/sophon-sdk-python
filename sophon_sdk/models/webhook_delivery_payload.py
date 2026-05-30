# coding: utf-8

"""SOPHON Encoding API client (generated)."""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class WebhookDeliveryPayload(BaseModel):
    """
    Payload delivered to registered webhook endpoints on terminal job events. Signed with HMAC-SHA256 over `\"{timestamp}.{raw_body}\"` using the per-webhook secret. Consumers must verify the signature before processing. 
    """ # noqa: E501
    event_id: StrictStr = Field(description="Unique delivery event ID for deduplication.")
    type: StrictStr = Field(description="Event type.")
    timestamp: datetime = Field(description="ISO 8601 timestamp of the event.")
    job_id: StrictStr = Field(description="The job that reached a terminal state.")
    status: StrictStr = Field(description="Terminal job status.")
    metadata: Dict[str, Any] = Field(description="Opaque metadata from the original job submission.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["event_id", "type", "timestamp", "job_id", "status", "metadata"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['job.completed', 'job.failed', 'job.canceled']):
            raise ValueError("must be one of enum values ('job.completed', 'job.failed', 'job.canceled')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['completed', 'failed', 'canceled']):
            raise ValueError("must be one of enum values ('completed', 'failed', 'canceled')")
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
        """Create an instance of WebhookDeliveryPayload from a JSON string"""
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
        """Create an instance of WebhookDeliveryPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_id": obj.get("event_id"),
            "type": obj.get("type"),
            "timestamp": obj.get("timestamp"),
            "job_id": obj.get("job_id"),
            "status": obj.get("status"),
            "metadata": obj.get("metadata")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


