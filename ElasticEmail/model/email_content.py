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


class EmailContent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Proper e-mail content
    """


    class MetaOapg:
        required = {
            "From",
        }
        
        class properties:
            _from = schemas.StrSchema
            
            
            class Body(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BodyPart']:
                        return BodyPart
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['BodyPart'], typing.List['BodyPart']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Body':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BodyPart':
                    return super().__getitem__(i)
            
            
            class Merge(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'Merge':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class Attachments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MessageAttachment']:
                        return MessageAttachment
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['MessageAttachment'], typing.List['MessageAttachment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Attachments':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MessageAttachment':
                    return super().__getitem__(i)
            
            
            class Headers(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'Headers':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            Postback = schemas.StrSchema
            EnvelopeFrom = schemas.StrSchema
            ReplyTo = schemas.StrSchema
            Subject = schemas.StrSchema
            TemplateName = schemas.StrSchema
            
            
            class AttachFiles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AttachFiles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def Utm() -> typing.Type['Utm']:
                return Utm
            __annotations__ = {
                "From": _from,
                "Body": Body,
                "Merge": Merge,
                "Attachments": Attachments,
                "Headers": Headers,
                "Postback": Postback,
                "EnvelopeFrom": EnvelopeFrom,
                "ReplyTo": ReplyTo,
                "Subject": Subject,
                "TemplateName": TemplateName,
                "AttachFiles": AttachFiles,
                "Utm": Utm,
            }
    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["From"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Body"]) -> MetaOapg.properties.Body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Merge"]) -> MetaOapg.properties.Merge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Attachments"]) -> MetaOapg.properties.Attachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Headers"]) -> MetaOapg.properties.Headers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Postback"]) -> MetaOapg.properties.Postback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EnvelopeFrom"]) -> MetaOapg.properties.EnvelopeFrom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ReplyTo"]) -> MetaOapg.properties.ReplyTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Subject"]) -> MetaOapg.properties.Subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TemplateName"]) -> MetaOapg.properties.TemplateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AttachFiles"]) -> MetaOapg.properties.AttachFiles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Utm"]) -> 'Utm': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["From", "Body", "Merge", "Attachments", "Headers", "Postback", "EnvelopeFrom", "ReplyTo", "Subject", "TemplateName", "AttachFiles", "Utm", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["From"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Body"]) -> typing.Union[MetaOapg.properties.Body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Merge"]) -> typing.Union[MetaOapg.properties.Merge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Attachments"]) -> typing.Union[MetaOapg.properties.Attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Headers"]) -> typing.Union[MetaOapg.properties.Headers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Postback"]) -> typing.Union[MetaOapg.properties.Postback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EnvelopeFrom"]) -> typing.Union[MetaOapg.properties.EnvelopeFrom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ReplyTo"]) -> typing.Union[MetaOapg.properties.ReplyTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Subject"]) -> typing.Union[MetaOapg.properties.Subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TemplateName"]) -> typing.Union[MetaOapg.properties.TemplateName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AttachFiles"]) -> typing.Union[MetaOapg.properties.AttachFiles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Utm"]) -> typing.Union['Utm', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["From", "Body", "Merge", "Attachments", "Headers", "Postback", "EnvelopeFrom", "ReplyTo", "Subject", "TemplateName", "AttachFiles", "Utm", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Body: typing.Union[MetaOapg.properties.Body, list, tuple, schemas.Unset] = schemas.unset,
        Merge: typing.Union[MetaOapg.properties.Merge, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        Attachments: typing.Union[MetaOapg.properties.Attachments, list, tuple, schemas.Unset] = schemas.unset,
        Headers: typing.Union[MetaOapg.properties.Headers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        Postback: typing.Union[MetaOapg.properties.Postback, str, schemas.Unset] = schemas.unset,
        EnvelopeFrom: typing.Union[MetaOapg.properties.EnvelopeFrom, str, schemas.Unset] = schemas.unset,
        ReplyTo: typing.Union[MetaOapg.properties.ReplyTo, str, schemas.Unset] = schemas.unset,
        Subject: typing.Union[MetaOapg.properties.Subject, str, schemas.Unset] = schemas.unset,
        TemplateName: typing.Union[MetaOapg.properties.TemplateName, str, schemas.Unset] = schemas.unset,
        AttachFiles: typing.Union[MetaOapg.properties.AttachFiles, list, tuple, schemas.Unset] = schemas.unset,
        Utm: typing.Union['Utm', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmailContent':
        return super().__new__(
            cls,
            *_args,
            Body=Body,
            Merge=Merge,
            Attachments=Attachments,
            Headers=Headers,
            Postback=Postback,
            EnvelopeFrom=EnvelopeFrom,
            ReplyTo=ReplyTo,
            Subject=Subject,
            TemplateName=TemplateName,
            AttachFiles=AttachFiles,
            Utm=Utm,
            _configuration=_configuration,
            **kwargs,
        )

from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.message_attachment import MessageAttachment
from ElasticEmail.model.utm import Utm
