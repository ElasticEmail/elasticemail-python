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


class Utm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Utm marketing data to be attached to every link in this e-mail.
    """


    class MetaOapg:
        
        class properties:
            Source = schemas.StrSchema
            Medium = schemas.StrSchema
            Campaign = schemas.StrSchema
            Content = schemas.StrSchema
            __annotations__ = {
                "Source": Source,
                "Medium": Medium,
                "Campaign": Campaign,
                "Content": Content,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Source"]) -> MetaOapg.properties.Source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Medium"]) -> MetaOapg.properties.Medium: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Campaign"]) -> MetaOapg.properties.Campaign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Content"]) -> MetaOapg.properties.Content: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Source", "Medium", "Campaign", "Content", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Source"]) -> typing.Union[MetaOapg.properties.Source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Medium"]) -> typing.Union[MetaOapg.properties.Medium, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Campaign"]) -> typing.Union[MetaOapg.properties.Campaign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Content"]) -> typing.Union[MetaOapg.properties.Content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Source", "Medium", "Campaign", "Content", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Source: typing.Union[MetaOapg.properties.Source, str, schemas.Unset] = schemas.unset,
        Medium: typing.Union[MetaOapg.properties.Medium, str, schemas.Unset] = schemas.unset,
        Campaign: typing.Union[MetaOapg.properties.Campaign, str, schemas.Unset] = schemas.unset,
        Content: typing.Union[MetaOapg.properties.Content, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Utm':
        return super().__new__(
            cls,
            *_args,
            Source=Source,
            Medium=Medium,
            Campaign=Campaign,
            Content=Content,
            _configuration=_configuration,
            **kwargs,
        )
