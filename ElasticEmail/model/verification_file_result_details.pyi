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


class VerificationFileResultDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Detailed verification file result info
    """


    class MetaOapg:
        
        class properties:
            
            
            class VerificationResult(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmailValidationResult']:
                        return EmailValidationResult
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['EmailValidationResult'], typing.List['EmailValidationResult']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'VerificationResult':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmailValidationResult':
                    return super().__getitem__(i)
            VerificationID = schemas.StrSchema
            Filename = schemas.StrSchema
        
            @staticmethod
            def VerificationStatus() -> typing.Type['VerificationStatus']:
                return VerificationStatus
        
            @staticmethod
            def FileUploadResult() -> typing.Type['FileUploadResult']:
                return FileUploadResult
            DateAdded = schemas.DateTimeSchema
            Source = schemas.StrSchema
            __annotations__ = {
                "VerificationResult": VerificationResult,
                "VerificationID": VerificationID,
                "Filename": Filename,
                "VerificationStatus": VerificationStatus,
                "FileUploadResult": FileUploadResult,
                "DateAdded": DateAdded,
                "Source": Source,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["VerificationResult"]) -> MetaOapg.properties.VerificationResult: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["VerificationID"]) -> MetaOapg.properties.VerificationID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Filename"]) -> MetaOapg.properties.Filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["VerificationStatus"]) -> 'VerificationStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FileUploadResult"]) -> 'FileUploadResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateAdded"]) -> MetaOapg.properties.DateAdded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Source"]) -> MetaOapg.properties.Source: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["VerificationResult", "VerificationID", "Filename", "VerificationStatus", "FileUploadResult", "DateAdded", "Source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["VerificationResult"]) -> typing.Union[MetaOapg.properties.VerificationResult, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["VerificationID"]) -> typing.Union[MetaOapg.properties.VerificationID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Filename"]) -> typing.Union[MetaOapg.properties.Filename, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["VerificationStatus"]) -> typing.Union['VerificationStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FileUploadResult"]) -> typing.Union['FileUploadResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateAdded"]) -> typing.Union[MetaOapg.properties.DateAdded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Source"]) -> typing.Union[MetaOapg.properties.Source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["VerificationResult", "VerificationID", "Filename", "VerificationStatus", "FileUploadResult", "DateAdded", "Source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        VerificationResult: typing.Union[MetaOapg.properties.VerificationResult, list, tuple, schemas.Unset] = schemas.unset,
        VerificationID: typing.Union[MetaOapg.properties.VerificationID, str, schemas.Unset] = schemas.unset,
        Filename: typing.Union[MetaOapg.properties.Filename, str, schemas.Unset] = schemas.unset,
        VerificationStatus: typing.Union['VerificationStatus', schemas.Unset] = schemas.unset,
        FileUploadResult: typing.Union['FileUploadResult', schemas.Unset] = schemas.unset,
        DateAdded: typing.Union[MetaOapg.properties.DateAdded, str, datetime, schemas.Unset] = schemas.unset,
        Source: typing.Union[MetaOapg.properties.Source, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VerificationFileResultDetails':
        return super().__new__(
            cls,
            *_args,
            VerificationResult=VerificationResult,
            VerificationID=VerificationID,
            Filename=Filename,
            VerificationStatus=VerificationStatus,
            FileUploadResult=FileUploadResult,
            DateAdded=DateAdded,
            Source=Source,
            _configuration=_configuration,
            **kwargs,
        )

from ElasticEmail.model.email_validation_result import EmailValidationResult
from ElasticEmail.model.file_upload_result import FileUploadResult
from ElasticEmail.model.verification_status import VerificationStatus
