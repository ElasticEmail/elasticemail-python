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


class EmailStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Status information of the specified email
    """


    class MetaOapg:
        
        class properties:
            _from = schemas.StrSchema
            To = schemas.StrSchema
            Date = schemas.DateTimeSchema
        
            @staticmethod
            def Status() -> typing.Type['LogJobStatus']:
                return LogJobStatus
            StatusName = schemas.StrSchema
            StatusChangeDate = schemas.DateTimeSchema
            DateSent = schemas.DateTimeSchema
            
            
            class DateOpened(
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
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'DateOpened':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class DateClicked(
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
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'DateClicked':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            ErrorMessage = schemas.StrSchema
            TransactionID = schemas.StrSchema
            EnvelopeFrom = schemas.StrSchema
            __annotations__ = {
                "From": _from,
                "To": To,
                "Date": Date,
                "Status": Status,
                "StatusName": StatusName,
                "StatusChangeDate": StatusChangeDate,
                "DateSent": DateSent,
                "DateOpened": DateOpened,
                "DateClicked": DateClicked,
                "ErrorMessage": ErrorMessage,
                "TransactionID": TransactionID,
                "EnvelopeFrom": EnvelopeFrom,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["From"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["To"]) -> MetaOapg.properties.To: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Date"]) -> MetaOapg.properties.Date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> 'LogJobStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatusName"]) -> MetaOapg.properties.StatusName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatusChangeDate"]) -> MetaOapg.properties.StatusChangeDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateSent"]) -> MetaOapg.properties.DateSent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateOpened"]) -> MetaOapg.properties.DateOpened: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateClicked"]) -> MetaOapg.properties.DateClicked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ErrorMessage"]) -> MetaOapg.properties.ErrorMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TransactionID"]) -> MetaOapg.properties.TransactionID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EnvelopeFrom"]) -> MetaOapg.properties.EnvelopeFrom: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["From", "To", "Date", "Status", "StatusName", "StatusChangeDate", "DateSent", "DateOpened", "DateClicked", "ErrorMessage", "TransactionID", "EnvelopeFrom", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["From"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["To"]) -> typing.Union[MetaOapg.properties.To, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Date"]) -> typing.Union[MetaOapg.properties.Date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> typing.Union['LogJobStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatusName"]) -> typing.Union[MetaOapg.properties.StatusName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatusChangeDate"]) -> typing.Union[MetaOapg.properties.StatusChangeDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateSent"]) -> typing.Union[MetaOapg.properties.DateSent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateOpened"]) -> typing.Union[MetaOapg.properties.DateOpened, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateClicked"]) -> typing.Union[MetaOapg.properties.DateClicked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ErrorMessage"]) -> typing.Union[MetaOapg.properties.ErrorMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TransactionID"]) -> typing.Union[MetaOapg.properties.TransactionID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EnvelopeFrom"]) -> typing.Union[MetaOapg.properties.EnvelopeFrom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["From", "To", "Date", "Status", "StatusName", "StatusChangeDate", "DateSent", "DateOpened", "DateClicked", "ErrorMessage", "TransactionID", "EnvelopeFrom", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        To: typing.Union[MetaOapg.properties.To, str, schemas.Unset] = schemas.unset,
        Date: typing.Union[MetaOapg.properties.Date, str, datetime, schemas.Unset] = schemas.unset,
        Status: typing.Union['LogJobStatus', schemas.Unset] = schemas.unset,
        StatusName: typing.Union[MetaOapg.properties.StatusName, str, schemas.Unset] = schemas.unset,
        StatusChangeDate: typing.Union[MetaOapg.properties.StatusChangeDate, str, datetime, schemas.Unset] = schemas.unset,
        DateSent: typing.Union[MetaOapg.properties.DateSent, str, datetime, schemas.Unset] = schemas.unset,
        DateOpened: typing.Union[MetaOapg.properties.DateOpened, None, str, datetime, schemas.Unset] = schemas.unset,
        DateClicked: typing.Union[MetaOapg.properties.DateClicked, None, str, datetime, schemas.Unset] = schemas.unset,
        ErrorMessage: typing.Union[MetaOapg.properties.ErrorMessage, str, schemas.Unset] = schemas.unset,
        TransactionID: typing.Union[MetaOapg.properties.TransactionID, str, schemas.Unset] = schemas.unset,
        EnvelopeFrom: typing.Union[MetaOapg.properties.EnvelopeFrom, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmailStatus':
        return super().__new__(
            cls,
            *_args,
            To=To,
            Date=Date,
            Status=Status,
            StatusName=StatusName,
            StatusChangeDate=StatusChangeDate,
            DateSent=DateSent,
            DateOpened=DateOpened,
            DateClicked=DateClicked,
            ErrorMessage=ErrorMessage,
            TransactionID=TransactionID,
            EnvelopeFrom=EnvelopeFrom,
            _configuration=_configuration,
            **kwargs,
        )

from ElasticEmail.model.log_job_status import LogJobStatus
