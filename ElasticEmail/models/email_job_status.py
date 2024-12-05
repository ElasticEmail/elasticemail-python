# coding: utf-8

"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.    To start using this API, you will need your Access Token (available <a target=\"_blank\" href=\"https://app.elasticemail.com/marketing/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    Downloadable library clients can be found in our Github repository <a target=\"_blank\" href=\"https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme\">here</a>

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ElasticEmail.models.email_job_failed_status import EmailJobFailedStatus
from typing import Optional, Set
from typing_extensions import Self

class EmailJobStatus(BaseModel):
    """
    EmailJobStatus
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID number of your attachment", alias="ID")
    status: Optional[StrictStr] = Field(default=None, description="Name of status: submitted, complete, in_progress", alias="Status")
    recipients_count: Optional[StrictInt] = Field(default=None, alias="RecipientsCount")
    failed: Optional[List[EmailJobFailedStatus]] = Field(default=None, alias="Failed")
    failed_count: Optional[StrictInt] = Field(default=None, description="Total emails failed.", alias="FailedCount")
    sent: Optional[List[StrictStr]] = Field(default=None, alias="Sent")
    sent_count: Optional[StrictInt] = Field(default=None, description="Total emails sent.", alias="SentCount")
    delivered: Optional[List[StrictStr]] = Field(default=None, description="Number of delivered messages", alias="Delivered")
    delivered_count: Optional[StrictInt] = Field(default=None, alias="DeliveredCount")
    pending: Optional[List[StrictStr]] = Field(default=None, alias="Pending")
    pending_count: Optional[StrictInt] = Field(default=None, alias="PendingCount")
    opened: Optional[List[StrictStr]] = Field(default=None, description="Number of opened messages", alias="Opened")
    opened_count: Optional[StrictInt] = Field(default=None, description="Total emails opened.", alias="OpenedCount")
    clicked: Optional[List[StrictStr]] = Field(default=None, description="Number of clicked messages", alias="Clicked")
    clicked_count: Optional[StrictInt] = Field(default=None, description="Total emails clicked", alias="ClickedCount")
    unsubscribed: Optional[List[StrictStr]] = Field(default=None, description="Number of unsubscribed messages", alias="Unsubscribed")
    unsubscribed_count: Optional[StrictInt] = Field(default=None, description="Total emails unsubscribed", alias="UnsubscribedCount")
    abuse_reports: Optional[List[StrictStr]] = Field(default=None, alias="AbuseReports")
    abuse_reports_count: Optional[StrictInt] = Field(default=None, alias="AbuseReportsCount")
    message_ids: Optional[List[StrictStr]] = Field(default=None, description="List of all MessageIDs for this job.", alias="MessageIDs")
    __properties: ClassVar[List[str]] = ["ID", "Status", "RecipientsCount", "Failed", "FailedCount", "Sent", "SentCount", "Delivered", "DeliveredCount", "Pending", "PendingCount", "Opened", "OpenedCount", "Clicked", "ClickedCount", "Unsubscribed", "UnsubscribedCount", "AbuseReports", "AbuseReportsCount", "MessageIDs"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EmailJobStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in failed (list)
        _items = []
        if self.failed:
            for _item in self.failed:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Failed'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmailJobStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ID": obj.get("ID"),
            "Status": obj.get("Status"),
            "RecipientsCount": obj.get("RecipientsCount"),
            "Failed": [EmailJobFailedStatus.from_dict(_item) for _item in obj["Failed"]] if obj.get("Failed") is not None else None,
            "FailedCount": obj.get("FailedCount"),
            "Sent": obj.get("Sent"),
            "SentCount": obj.get("SentCount"),
            "Delivered": obj.get("Delivered"),
            "DeliveredCount": obj.get("DeliveredCount"),
            "Pending": obj.get("Pending"),
            "PendingCount": obj.get("PendingCount"),
            "Opened": obj.get("Opened"),
            "OpenedCount": obj.get("OpenedCount"),
            "Clicked": obj.get("Clicked"),
            "ClickedCount": obj.get("ClickedCount"),
            "Unsubscribed": obj.get("Unsubscribed"),
            "UnsubscribedCount": obj.get("UnsubscribedCount"),
            "AbuseReports": obj.get("AbuseReports"),
            "AbuseReportsCount": obj.get("AbuseReportsCount"),
            "MessageIDs": obj.get("MessageIDs")
        })
        return _obj

