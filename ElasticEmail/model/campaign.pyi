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


class Campaign(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "Recipients",
            "Name",
        }
        
        class properties:
            Name = schemas.StrSchema
        
            @staticmethod
            def Recipients() -> typing.Type['CampaignRecipient']:
                return CampaignRecipient
            
            
            class Content(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CampaignTemplate']:
                        return CampaignTemplate
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CampaignTemplate'], typing.List['CampaignTemplate']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Content':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CampaignTemplate':
                    return super().__getitem__(i)
        
            @staticmethod
            def Status() -> typing.Type['CampaignStatus']:
                return CampaignStatus
        
            @staticmethod
            def Options() -> typing.Type['CampaignOptions']:
                return CampaignOptions
            __annotations__ = {
                "Name": Name,
                "Recipients": Recipients,
                "Content": Content,
                "Status": Status,
                "Options": Options,
            }
    
    Recipients: 'CampaignRecipient'
    Name: MetaOapg.properties.Name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Recipients"]) -> 'CampaignRecipient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Content"]) -> MetaOapg.properties.Content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> 'CampaignStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Options"]) -> 'CampaignOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Name", "Recipients", "Content", "Status", "Options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Recipients"]) -> 'CampaignRecipient': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Content"]) -> typing.Union[MetaOapg.properties.Content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> typing.Union['CampaignStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Options"]) -> typing.Union['CampaignOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Name", "Recipients", "Content", "Status", "Options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Recipients: 'CampaignRecipient',
        Name: typing.Union[MetaOapg.properties.Name, str, ],
        Content: typing.Union[MetaOapg.properties.Content, list, tuple, schemas.Unset] = schemas.unset,
        Status: typing.Union['CampaignStatus', schemas.Unset] = schemas.unset,
        Options: typing.Union['CampaignOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Campaign':
        return super().__new__(
            cls,
            *args,
            Recipients=Recipients,
            Name=Name,
            Content=Content,
            Status=Status,
            Options=Options,
            _configuration=_configuration,
            **kwargs,
        )

from ElasticEmail.model.campaign_options import CampaignOptions
from ElasticEmail.model.campaign_recipient import CampaignRecipient
from ElasticEmail.model.campaign_status import CampaignStatus
from ElasticEmail.model.campaign_template import CampaignTemplate
