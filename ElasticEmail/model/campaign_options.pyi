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


class CampaignOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Different send options for a Campaign
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def DeliveryOptimization() -> typing.Type['DeliveryOptimizationType']:
                return DeliveryOptimizationType
            
            
            class TrackOpens(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                class MetaOapg:
                    format = 'boolean'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TrackOpens':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TrackClicks(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                class MetaOapg:
                    format = 'boolean'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TrackClicks':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ScheduleFor(
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
                ) -> 'ScheduleFor':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def SplitOptions() -> typing.Type['SplitOptions']:
                return SplitOptions
            __annotations__ = {
                "DeliveryOptimization": DeliveryOptimization,
                "TrackOpens": TrackOpens,
                "TrackClicks": TrackClicks,
                "ScheduleFor": ScheduleFor,
                "SplitOptions": SplitOptions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DeliveryOptimization"]) -> 'DeliveryOptimizationType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TrackOpens"]) -> MetaOapg.properties.TrackOpens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TrackClicks"]) -> MetaOapg.properties.TrackClicks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ScheduleFor"]) -> MetaOapg.properties.ScheduleFor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SplitOptions"]) -> 'SplitOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["DeliveryOptimization", "TrackOpens", "TrackClicks", "ScheduleFor", "SplitOptions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DeliveryOptimization"]) -> typing.Union['DeliveryOptimizationType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TrackOpens"]) -> typing.Union[MetaOapg.properties.TrackOpens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TrackClicks"]) -> typing.Union[MetaOapg.properties.TrackClicks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ScheduleFor"]) -> typing.Union[MetaOapg.properties.ScheduleFor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SplitOptions"]) -> typing.Union['SplitOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["DeliveryOptimization", "TrackOpens", "TrackClicks", "ScheduleFor", "SplitOptions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        DeliveryOptimization: typing.Union['DeliveryOptimizationType', schemas.Unset] = schemas.unset,
        TrackOpens: typing.Union[MetaOapg.properties.TrackOpens, None, bool, schemas.Unset] = schemas.unset,
        TrackClicks: typing.Union[MetaOapg.properties.TrackClicks, None, bool, schemas.Unset] = schemas.unset,
        ScheduleFor: typing.Union[MetaOapg.properties.ScheduleFor, None, str, datetime, schemas.Unset] = schemas.unset,
        SplitOptions: typing.Union['SplitOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CampaignOptions':
        return super().__new__(
            cls,
            *args,
            DeliveryOptimization=DeliveryOptimization,
            TrackOpens=TrackOpens,
            TrackClicks=TrackClicks,
            ScheduleFor=ScheduleFor,
            SplitOptions=SplitOptions,
            _configuration=_configuration,
            **kwargs,
        )

from ElasticEmail.model.delivery_optimization_type import DeliveryOptimizationType
from ElasticEmail.model.split_options import SplitOptions
