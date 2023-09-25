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


class Options(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    E-mail configuration
    """


    class MetaOapg:
        
        class properties:
            
            
            class TimeOffset(
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
                ) -> 'TimeOffset':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            PoolName = schemas.StrSchema
            ChannelName = schemas.StrSchema
        
            @staticmethod
            def Encoding() -> typing.Type['EncodingType']:
                return EncodingType
            TrackOpens = schemas.BoolSchema
            TrackClicks = schemas.BoolSchema
            __annotations__ = {
                "TimeOffset": TimeOffset,
                "PoolName": PoolName,
                "ChannelName": ChannelName,
                "Encoding": Encoding,
                "TrackOpens": TrackOpens,
                "TrackClicks": TrackClicks,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOffset"]) -> MetaOapg.properties.TimeOffset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PoolName"]) -> MetaOapg.properties.PoolName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ChannelName"]) -> MetaOapg.properties.ChannelName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Encoding"]) -> 'EncodingType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TrackOpens"]) -> MetaOapg.properties.TrackOpens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TrackClicks"]) -> MetaOapg.properties.TrackClicks: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TimeOffset", "PoolName", "ChannelName", "Encoding", "TrackOpens", "TrackClicks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOffset"]) -> typing.Union[MetaOapg.properties.TimeOffset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PoolName"]) -> typing.Union[MetaOapg.properties.PoolName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ChannelName"]) -> typing.Union[MetaOapg.properties.ChannelName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Encoding"]) -> typing.Union['EncodingType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TrackOpens"]) -> typing.Union[MetaOapg.properties.TrackOpens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TrackClicks"]) -> typing.Union[MetaOapg.properties.TrackClicks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TimeOffset", "PoolName", "ChannelName", "Encoding", "TrackOpens", "TrackClicks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        TimeOffset: typing.Union[MetaOapg.properties.TimeOffset, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        PoolName: typing.Union[MetaOapg.properties.PoolName, str, schemas.Unset] = schemas.unset,
        ChannelName: typing.Union[MetaOapg.properties.ChannelName, str, schemas.Unset] = schemas.unset,
        Encoding: typing.Union['EncodingType', schemas.Unset] = schemas.unset,
        TrackOpens: typing.Union[MetaOapg.properties.TrackOpens, bool, schemas.Unset] = schemas.unset,
        TrackClicks: typing.Union[MetaOapg.properties.TrackClicks, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Options':
        return super().__new__(
            cls,
            *_args,
            TimeOffset=TimeOffset,
            PoolName=PoolName,
            ChannelName=ChannelName,
            Encoding=Encoding,
            TrackOpens=TrackOpens,
            TrackClicks=TrackClicks,
            _configuration=_configuration,
            **kwargs,
        )

from ElasticEmail.model.encoding_type import EncodingType
