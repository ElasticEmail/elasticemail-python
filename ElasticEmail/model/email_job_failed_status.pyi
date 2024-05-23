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


class EmailJobFailedStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            Address = schemas.StrSchema
            Error = schemas.StrSchema
            ErrorCode = schemas.Int32Schema
            Category = schemas.StrSchema
            __annotations__ = {
                "Address": Address,
                "Error": Error,
                "ErrorCode": ErrorCode,
                "Category": Category,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address"]) -> MetaOapg.properties.Address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Error"]) -> MetaOapg.properties.Error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ErrorCode"]) -> MetaOapg.properties.ErrorCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Category"]) -> MetaOapg.properties.Category: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Address", "Error", "ErrorCode", "Category", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address"]) -> typing.Union[MetaOapg.properties.Address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Error"]) -> typing.Union[MetaOapg.properties.Error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ErrorCode"]) -> typing.Union[MetaOapg.properties.ErrorCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Category"]) -> typing.Union[MetaOapg.properties.Category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Address", "Error", "ErrorCode", "Category", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Address: typing.Union[MetaOapg.properties.Address, str, schemas.Unset] = schemas.unset,
        Error: typing.Union[MetaOapg.properties.Error, str, schemas.Unset] = schemas.unset,
        ErrorCode: typing.Union[MetaOapg.properties.ErrorCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Category: typing.Union[MetaOapg.properties.Category, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmailJobFailedStatus':
        return super().__new__(
            cls,
            *_args,
            Address=Address,
            Error=Error,
            ErrorCode=ErrorCode,
            Category=Category,
            _configuration=_configuration,
            **kwargs,
        )
