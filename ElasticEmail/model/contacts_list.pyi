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


class ContactsList(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List of Lists, with detailed data about its contents.
    """


    class MetaOapg:
        
        class properties:
            ListName = schemas.StrSchema
            
            
            class PublicListID(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'guid'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PublicListID':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            DateAdded = schemas.DateTimeSchema
            AllowUnsubscribe = schemas.BoolSchema
            __annotations__ = {
                "ListName": ListName,
                "PublicListID": PublicListID,
                "DateAdded": DateAdded,
                "AllowUnsubscribe": AllowUnsubscribe,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ListName"]) -> MetaOapg.properties.ListName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PublicListID"]) -> MetaOapg.properties.PublicListID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateAdded"]) -> MetaOapg.properties.DateAdded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AllowUnsubscribe"]) -> MetaOapg.properties.AllowUnsubscribe: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ListName", "PublicListID", "DateAdded", "AllowUnsubscribe", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ListName"]) -> typing.Union[MetaOapg.properties.ListName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PublicListID"]) -> typing.Union[MetaOapg.properties.PublicListID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateAdded"]) -> typing.Union[MetaOapg.properties.DateAdded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AllowUnsubscribe"]) -> typing.Union[MetaOapg.properties.AllowUnsubscribe, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ListName", "PublicListID", "DateAdded", "AllowUnsubscribe", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ListName: typing.Union[MetaOapg.properties.ListName, str, schemas.Unset] = schemas.unset,
        PublicListID: typing.Union[MetaOapg.properties.PublicListID, None, str, schemas.Unset] = schemas.unset,
        DateAdded: typing.Union[MetaOapg.properties.DateAdded, str, datetime, schemas.Unset] = schemas.unset,
        AllowUnsubscribe: typing.Union[MetaOapg.properties.AllowUnsubscribe, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContactsList':
        return super().__new__(
            cls,
            *_args,
            ListName=ListName,
            PublicListID=PublicListID,
            DateAdded=DateAdded,
            AllowUnsubscribe=AllowUnsubscribe,
            _configuration=_configuration,
            **kwargs,
        )
