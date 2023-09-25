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


class ContactActivity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            TotalSent = schemas.Int32Schema
            TotalOpened = schemas.Int32Schema
            TotalClicked = schemas.Int32Schema
            TotalFailed = schemas.Int32Schema
            
            
            class LastSent(
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
                ) -> 'LastSent':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class LastOpened(
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
                ) -> 'LastOpened':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class LastClicked(
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
                ) -> 'LastClicked':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class LastFailed(
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
                ) -> 'LastFailed':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            LastIP = schemas.StrSchema
            
            
            class ErrorCode(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ErrorCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            FriendlyErrorMessage = schemas.StrSchema
            __annotations__ = {
                "TotalSent": TotalSent,
                "TotalOpened": TotalOpened,
                "TotalClicked": TotalClicked,
                "TotalFailed": TotalFailed,
                "LastSent": LastSent,
                "LastOpened": LastOpened,
                "LastClicked": LastClicked,
                "LastFailed": LastFailed,
                "LastIP": LastIP,
                "ErrorCode": ErrorCode,
                "FriendlyErrorMessage": FriendlyErrorMessage,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalSent"]) -> MetaOapg.properties.TotalSent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalOpened"]) -> MetaOapg.properties.TotalOpened: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalClicked"]) -> MetaOapg.properties.TotalClicked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalFailed"]) -> MetaOapg.properties.TotalFailed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastSent"]) -> MetaOapg.properties.LastSent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastOpened"]) -> MetaOapg.properties.LastOpened: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastClicked"]) -> MetaOapg.properties.LastClicked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastFailed"]) -> MetaOapg.properties.LastFailed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastIP"]) -> MetaOapg.properties.LastIP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ErrorCode"]) -> MetaOapg.properties.ErrorCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FriendlyErrorMessage"]) -> MetaOapg.properties.FriendlyErrorMessage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TotalSent", "TotalOpened", "TotalClicked", "TotalFailed", "LastSent", "LastOpened", "LastClicked", "LastFailed", "LastIP", "ErrorCode", "FriendlyErrorMessage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalSent"]) -> typing.Union[MetaOapg.properties.TotalSent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalOpened"]) -> typing.Union[MetaOapg.properties.TotalOpened, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalClicked"]) -> typing.Union[MetaOapg.properties.TotalClicked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalFailed"]) -> typing.Union[MetaOapg.properties.TotalFailed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastSent"]) -> typing.Union[MetaOapg.properties.LastSent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastOpened"]) -> typing.Union[MetaOapg.properties.LastOpened, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastClicked"]) -> typing.Union[MetaOapg.properties.LastClicked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastFailed"]) -> typing.Union[MetaOapg.properties.LastFailed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastIP"]) -> typing.Union[MetaOapg.properties.LastIP, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ErrorCode"]) -> typing.Union[MetaOapg.properties.ErrorCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FriendlyErrorMessage"]) -> typing.Union[MetaOapg.properties.FriendlyErrorMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TotalSent", "TotalOpened", "TotalClicked", "TotalFailed", "LastSent", "LastOpened", "LastClicked", "LastFailed", "LastIP", "ErrorCode", "FriendlyErrorMessage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        TotalSent: typing.Union[MetaOapg.properties.TotalSent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TotalOpened: typing.Union[MetaOapg.properties.TotalOpened, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TotalClicked: typing.Union[MetaOapg.properties.TotalClicked, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TotalFailed: typing.Union[MetaOapg.properties.TotalFailed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        LastSent: typing.Union[MetaOapg.properties.LastSent, None, str, datetime, schemas.Unset] = schemas.unset,
        LastOpened: typing.Union[MetaOapg.properties.LastOpened, None, str, datetime, schemas.Unset] = schemas.unset,
        LastClicked: typing.Union[MetaOapg.properties.LastClicked, None, str, datetime, schemas.Unset] = schemas.unset,
        LastFailed: typing.Union[MetaOapg.properties.LastFailed, None, str, datetime, schemas.Unset] = schemas.unset,
        LastIP: typing.Union[MetaOapg.properties.LastIP, str, schemas.Unset] = schemas.unset,
        ErrorCode: typing.Union[MetaOapg.properties.ErrorCode, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        FriendlyErrorMessage: typing.Union[MetaOapg.properties.FriendlyErrorMessage, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContactActivity':
        return super().__new__(
            cls,
            *_args,
            TotalSent=TotalSent,
            TotalOpened=TotalOpened,
            TotalClicked=TotalClicked,
            TotalFailed=TotalFailed,
            LastSent=LastSent,
            LastOpened=LastOpened,
            LastClicked=LastClicked,
            LastFailed=LastFailed,
            LastIP=LastIP,
            ErrorCode=ErrorCode,
            FriendlyErrorMessage=FriendlyErrorMessage,
            _configuration=_configuration,
            **kwargs,
        )