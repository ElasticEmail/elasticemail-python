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


class NewSmtpCredentials(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Newly generated SMTP Credentials with Token
    """


    class MetaOapg:
        
        class properties:
            Token = schemas.StrSchema
        
            @staticmethod
            def AccessLevel() -> typing.Type['AccessLevel']:
                return AccessLevel
            Name = schemas.StrSchema
            DateCreated = schemas.DateTimeSchema
            
            
            class LastUse(
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
                ) -> 'LastUse':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class Expires(
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
                ) -> 'Expires':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class RestrictAccessToIPRange(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'RestrictAccessToIPRange':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "Token": Token,
                "AccessLevel": AccessLevel,
                "Name": Name,
                "DateCreated": DateCreated,
                "LastUse": LastUse,
                "Expires": Expires,
                "RestrictAccessToIPRange": RestrictAccessToIPRange,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Token"]) -> MetaOapg.properties.Token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccessLevel"]) -> 'AccessLevel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateCreated"]) -> MetaOapg.properties.DateCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastUse"]) -> MetaOapg.properties.LastUse: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Expires"]) -> MetaOapg.properties.Expires: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RestrictAccessToIPRange"]) -> MetaOapg.properties.RestrictAccessToIPRange: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Token", "AccessLevel", "Name", "DateCreated", "LastUse", "Expires", "RestrictAccessToIPRange", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Token"]) -> typing.Union[MetaOapg.properties.Token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccessLevel"]) -> typing.Union['AccessLevel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateCreated"]) -> typing.Union[MetaOapg.properties.DateCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastUse"]) -> typing.Union[MetaOapg.properties.LastUse, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Expires"]) -> typing.Union[MetaOapg.properties.Expires, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RestrictAccessToIPRange"]) -> typing.Union[MetaOapg.properties.RestrictAccessToIPRange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Token", "AccessLevel", "Name", "DateCreated", "LastUse", "Expires", "RestrictAccessToIPRange", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Token: typing.Union[MetaOapg.properties.Token, str, schemas.Unset] = schemas.unset,
        AccessLevel: typing.Union['AccessLevel', schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        DateCreated: typing.Union[MetaOapg.properties.DateCreated, str, datetime, schemas.Unset] = schemas.unset,
        LastUse: typing.Union[MetaOapg.properties.LastUse, None, str, datetime, schemas.Unset] = schemas.unset,
        Expires: typing.Union[MetaOapg.properties.Expires, None, str, datetime, schemas.Unset] = schemas.unset,
        RestrictAccessToIPRange: typing.Union[MetaOapg.properties.RestrictAccessToIPRange, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewSmtpCredentials':
        return super().__new__(
            cls,
            *_args,
            Token=Token,
            AccessLevel=AccessLevel,
            Name=Name,
            DateCreated=DateCreated,
            LastUse=LastUse,
            Expires=Expires,
            RestrictAccessToIPRange=RestrictAccessToIPRange,
            _configuration=_configuration,
            **kwargs,
        )

from ElasticEmail.model.access_level import AccessLevel
