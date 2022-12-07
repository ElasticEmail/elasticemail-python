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


class SubaccountEmailSettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Settings related to sending emails
    """


    class MetaOapg:
        
        class properties:
            MonthlyRefillCredits = schemas.Int32Schema
            RequiresEmailCredits = schemas.BoolSchema
            EmailSizeLimit = schemas.Int32Schema
            DailySendLimit = schemas.Int32Schema
            MaxContacts = schemas.Int32Schema
            EnablePrivateIPPurchase = schemas.BoolSchema
            PoolName = schemas.StrSchema
            
            
            class ValidSenderDomainOnly(
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
                ) -> 'ValidSenderDomainOnly':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "MonthlyRefillCredits": MonthlyRefillCredits,
                "RequiresEmailCredits": RequiresEmailCredits,
                "EmailSizeLimit": EmailSizeLimit,
                "DailySendLimit": DailySendLimit,
                "MaxContacts": MaxContacts,
                "EnablePrivateIPPurchase": EnablePrivateIPPurchase,
                "PoolName": PoolName,
                "ValidSenderDomainOnly": ValidSenderDomainOnly,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MonthlyRefillCredits"]) -> MetaOapg.properties.MonthlyRefillCredits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RequiresEmailCredits"]) -> MetaOapg.properties.RequiresEmailCredits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmailSizeLimit"]) -> MetaOapg.properties.EmailSizeLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DailySendLimit"]) -> MetaOapg.properties.DailySendLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MaxContacts"]) -> MetaOapg.properties.MaxContacts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EnablePrivateIPPurchase"]) -> MetaOapg.properties.EnablePrivateIPPurchase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PoolName"]) -> MetaOapg.properties.PoolName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ValidSenderDomainOnly"]) -> MetaOapg.properties.ValidSenderDomainOnly: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["MonthlyRefillCredits", "RequiresEmailCredits", "EmailSizeLimit", "DailySendLimit", "MaxContacts", "EnablePrivateIPPurchase", "PoolName", "ValidSenderDomainOnly", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MonthlyRefillCredits"]) -> typing.Union[MetaOapg.properties.MonthlyRefillCredits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RequiresEmailCredits"]) -> typing.Union[MetaOapg.properties.RequiresEmailCredits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmailSizeLimit"]) -> typing.Union[MetaOapg.properties.EmailSizeLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DailySendLimit"]) -> typing.Union[MetaOapg.properties.DailySendLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MaxContacts"]) -> typing.Union[MetaOapg.properties.MaxContacts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EnablePrivateIPPurchase"]) -> typing.Union[MetaOapg.properties.EnablePrivateIPPurchase, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PoolName"]) -> typing.Union[MetaOapg.properties.PoolName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ValidSenderDomainOnly"]) -> typing.Union[MetaOapg.properties.ValidSenderDomainOnly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["MonthlyRefillCredits", "RequiresEmailCredits", "EmailSizeLimit", "DailySendLimit", "MaxContacts", "EnablePrivateIPPurchase", "PoolName", "ValidSenderDomainOnly", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        MonthlyRefillCredits: typing.Union[MetaOapg.properties.MonthlyRefillCredits, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        RequiresEmailCredits: typing.Union[MetaOapg.properties.RequiresEmailCredits, bool, schemas.Unset] = schemas.unset,
        EmailSizeLimit: typing.Union[MetaOapg.properties.EmailSizeLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        DailySendLimit: typing.Union[MetaOapg.properties.DailySendLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        MaxContacts: typing.Union[MetaOapg.properties.MaxContacts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        EnablePrivateIPPurchase: typing.Union[MetaOapg.properties.EnablePrivateIPPurchase, bool, schemas.Unset] = schemas.unset,
        PoolName: typing.Union[MetaOapg.properties.PoolName, str, schemas.Unset] = schemas.unset,
        ValidSenderDomainOnly: typing.Union[MetaOapg.properties.ValidSenderDomainOnly, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubaccountEmailSettings':
        return super().__new__(
            cls,
            *args,
            MonthlyRefillCredits=MonthlyRefillCredits,
            RequiresEmailCredits=RequiresEmailCredits,
            EmailSizeLimit=EmailSizeLimit,
            DailySendLimit=DailySendLimit,
            MaxContacts=MaxContacts,
            EnablePrivateIPPurchase=EnablePrivateIPPurchase,
            PoolName=PoolName,
            ValidSenderDomainOnly=ValidSenderDomainOnly,
            _configuration=_configuration,
            **kwargs,
        )
