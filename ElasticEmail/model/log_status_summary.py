# coding: utf-8

"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.    To start using this API, you will need your Access Token (available <a target=\"_blank\" href=\"https://app.elasticemail.com/marketing/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    Downloadable library clients can be found in our Github repository <a target=\"_blank\" href=\"https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme\">here</a>  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ElasticEmail import schemas  # noqa: F401


class LogStatusSummary(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Summary of log status
    """


    class MetaOapg:
        
        class properties:
            Recipients = schemas.Int64Schema
            EmailTotal = schemas.Int64Schema
            SmsTotal = schemas.Int64Schema
            Delivered = schemas.Int64Schema
            Bounced = schemas.Int64Schema
            InProgress = schemas.Int64Schema
            Opened = schemas.Int64Schema
            Clicked = schemas.Int64Schema
            Unsubscribed = schemas.Int64Schema
            Complaints = schemas.Int64Schema
            Inbound = schemas.Int64Schema
            ManualCancel = schemas.Int64Schema
            NotDelivered = schemas.Int64Schema
            __annotations__ = {
                "Recipients": Recipients,
                "EmailTotal": EmailTotal,
                "SmsTotal": SmsTotal,
                "Delivered": Delivered,
                "Bounced": Bounced,
                "InProgress": InProgress,
                "Opened": Opened,
                "Clicked": Clicked,
                "Unsubscribed": Unsubscribed,
                "Complaints": Complaints,
                "Inbound": Inbound,
                "ManualCancel": ManualCancel,
                "NotDelivered": NotDelivered,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Recipients"]) -> MetaOapg.properties.Recipients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmailTotal"]) -> MetaOapg.properties.EmailTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SmsTotal"]) -> MetaOapg.properties.SmsTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Delivered"]) -> MetaOapg.properties.Delivered: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Bounced"]) -> MetaOapg.properties.Bounced: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["InProgress"]) -> MetaOapg.properties.InProgress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Opened"]) -> MetaOapg.properties.Opened: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Clicked"]) -> MetaOapg.properties.Clicked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Unsubscribed"]) -> MetaOapg.properties.Unsubscribed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Complaints"]) -> MetaOapg.properties.Complaints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Inbound"]) -> MetaOapg.properties.Inbound: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ManualCancel"]) -> MetaOapg.properties.ManualCancel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NotDelivered"]) -> MetaOapg.properties.NotDelivered: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Recipients", "EmailTotal", "SmsTotal", "Delivered", "Bounced", "InProgress", "Opened", "Clicked", "Unsubscribed", "Complaints", "Inbound", "ManualCancel", "NotDelivered", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Recipients"]) -> typing.Union[MetaOapg.properties.Recipients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmailTotal"]) -> typing.Union[MetaOapg.properties.EmailTotal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SmsTotal"]) -> typing.Union[MetaOapg.properties.SmsTotal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Delivered"]) -> typing.Union[MetaOapg.properties.Delivered, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Bounced"]) -> typing.Union[MetaOapg.properties.Bounced, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["InProgress"]) -> typing.Union[MetaOapg.properties.InProgress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Opened"]) -> typing.Union[MetaOapg.properties.Opened, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Clicked"]) -> typing.Union[MetaOapg.properties.Clicked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Unsubscribed"]) -> typing.Union[MetaOapg.properties.Unsubscribed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Complaints"]) -> typing.Union[MetaOapg.properties.Complaints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Inbound"]) -> typing.Union[MetaOapg.properties.Inbound, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ManualCancel"]) -> typing.Union[MetaOapg.properties.ManualCancel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NotDelivered"]) -> typing.Union[MetaOapg.properties.NotDelivered, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Recipients", "EmailTotal", "SmsTotal", "Delivered", "Bounced", "InProgress", "Opened", "Clicked", "Unsubscribed", "Complaints", "Inbound", "ManualCancel", "NotDelivered", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Recipients: typing.Union[MetaOapg.properties.Recipients, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        EmailTotal: typing.Union[MetaOapg.properties.EmailTotal, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        SmsTotal: typing.Union[MetaOapg.properties.SmsTotal, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Delivered: typing.Union[MetaOapg.properties.Delivered, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Bounced: typing.Union[MetaOapg.properties.Bounced, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        InProgress: typing.Union[MetaOapg.properties.InProgress, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Opened: typing.Union[MetaOapg.properties.Opened, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Clicked: typing.Union[MetaOapg.properties.Clicked, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Unsubscribed: typing.Union[MetaOapg.properties.Unsubscribed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Complaints: typing.Union[MetaOapg.properties.Complaints, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Inbound: typing.Union[MetaOapg.properties.Inbound, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ManualCancel: typing.Union[MetaOapg.properties.ManualCancel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        NotDelivered: typing.Union[MetaOapg.properties.NotDelivered, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogStatusSummary':
        return super().__new__(
            cls,
            *args,
            Recipients=Recipients,
            EmailTotal=EmailTotal,
            SmsTotal=SmsTotal,
            Delivered=Delivered,
            Bounced=Bounced,
            InProgress=InProgress,
            Opened=Opened,
            Clicked=Clicked,
            Unsubscribed=Unsubscribed,
            Complaints=Complaints,
            Inbound=Inbound,
            ManualCancel=ManualCancel,
            NotDelivered=NotDelivered,
            _configuration=_configuration,
            **kwargs,
        )
