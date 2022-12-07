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


class RecipientEvent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Detailed information about message recipient
    """


    class MetaOapg:
        
        class properties:
            TransactionID = schemas.StrSchema
            MsgID = schemas.StrSchema
            FromEmail = schemas.StrSchema
            To = schemas.StrSchema
            Subject = schemas.StrSchema
        
            @staticmethod
            def EventType() -> typing.Type['EventType']:
                return EventType
            EventDate = schemas.DateTimeSchema
            ChannelName = schemas.StrSchema
        
            @staticmethod
            def MessageCategory() -> typing.Type['MessageCategory']:
                return MessageCategory
            
            
            class NextTryOn(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NextTryOn':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            Message = schemas.StrSchema
            IPAddress = schemas.StrSchema
            PoolName = schemas.StrSchema
            __annotations__ = {
                "TransactionID": TransactionID,
                "MsgID": MsgID,
                "FromEmail": FromEmail,
                "To": To,
                "Subject": Subject,
                "EventType": EventType,
                "EventDate": EventDate,
                "ChannelName": ChannelName,
                "MessageCategory": MessageCategory,
                "NextTryOn": NextTryOn,
                "Message": Message,
                "IPAddress": IPAddress,
                "PoolName": PoolName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TransactionID"]) -> MetaOapg.properties.TransactionID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MsgID"]) -> MetaOapg.properties.MsgID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FromEmail"]) -> MetaOapg.properties.FromEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["To"]) -> MetaOapg.properties.To: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Subject"]) -> MetaOapg.properties.Subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EventType"]) -> 'EventType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EventDate"]) -> MetaOapg.properties.EventDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ChannelName"]) -> MetaOapg.properties.ChannelName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MessageCategory"]) -> 'MessageCategory': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NextTryOn"]) -> MetaOapg.properties.NextTryOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Message"]) -> MetaOapg.properties.Message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IPAddress"]) -> MetaOapg.properties.IPAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PoolName"]) -> MetaOapg.properties.PoolName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TransactionID", "MsgID", "FromEmail", "To", "Subject", "EventType", "EventDate", "ChannelName", "MessageCategory", "NextTryOn", "Message", "IPAddress", "PoolName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TransactionID"]) -> typing.Union[MetaOapg.properties.TransactionID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MsgID"]) -> typing.Union[MetaOapg.properties.MsgID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FromEmail"]) -> typing.Union[MetaOapg.properties.FromEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["To"]) -> typing.Union[MetaOapg.properties.To, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Subject"]) -> typing.Union[MetaOapg.properties.Subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EventType"]) -> typing.Union['EventType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EventDate"]) -> typing.Union[MetaOapg.properties.EventDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ChannelName"]) -> typing.Union[MetaOapg.properties.ChannelName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MessageCategory"]) -> typing.Union['MessageCategory', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NextTryOn"]) -> typing.Union[MetaOapg.properties.NextTryOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Message"]) -> typing.Union[MetaOapg.properties.Message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IPAddress"]) -> typing.Union[MetaOapg.properties.IPAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PoolName"]) -> typing.Union[MetaOapg.properties.PoolName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TransactionID", "MsgID", "FromEmail", "To", "Subject", "EventType", "EventDate", "ChannelName", "MessageCategory", "NextTryOn", "Message", "IPAddress", "PoolName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        TransactionID: typing.Union[MetaOapg.properties.TransactionID, str, schemas.Unset] = schemas.unset,
        MsgID: typing.Union[MetaOapg.properties.MsgID, str, schemas.Unset] = schemas.unset,
        FromEmail: typing.Union[MetaOapg.properties.FromEmail, str, schemas.Unset] = schemas.unset,
        To: typing.Union[MetaOapg.properties.To, str, schemas.Unset] = schemas.unset,
        Subject: typing.Union[MetaOapg.properties.Subject, str, schemas.Unset] = schemas.unset,
        EventType: typing.Union['EventType', schemas.Unset] = schemas.unset,
        EventDate: typing.Union[MetaOapg.properties.EventDate, str, datetime, schemas.Unset] = schemas.unset,
        ChannelName: typing.Union[MetaOapg.properties.ChannelName, str, schemas.Unset] = schemas.unset,
        MessageCategory: typing.Union['MessageCategory', schemas.Unset] = schemas.unset,
        NextTryOn: typing.Union[MetaOapg.properties.NextTryOn, None, str, datetime, schemas.Unset] = schemas.unset,
        Message: typing.Union[MetaOapg.properties.Message, str, schemas.Unset] = schemas.unset,
        IPAddress: typing.Union[MetaOapg.properties.IPAddress, str, schemas.Unset] = schemas.unset,
        PoolName: typing.Union[MetaOapg.properties.PoolName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecipientEvent':
        return super().__new__(
            cls,
            *args,
            TransactionID=TransactionID,
            MsgID=MsgID,
            FromEmail=FromEmail,
            To=To,
            Subject=Subject,
            EventType=EventType,
            EventDate=EventDate,
            ChannelName=ChannelName,
            MessageCategory=MessageCategory,
            NextTryOn=NextTryOn,
            Message=Message,
            IPAddress=IPAddress,
            PoolName=PoolName,
            _configuration=_configuration,
            **kwargs,
        )

from ElasticEmail.model.event_type import EventType
from ElasticEmail.model.message_category import MessageCategory
