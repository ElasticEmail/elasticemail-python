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


class LogJobStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def ALL(cls):
        return cls("All")
    
    @schemas.classproperty
    def READY_TO_SEND(cls):
        return cls("ReadyToSend")
    
    @schemas.classproperty
    def WAITING_TO_RETRY(cls):
        return cls("WaitingToRetry")
    
    @schemas.classproperty
    def SENDING(cls):
        return cls("Sending")
    
    @schemas.classproperty
    def ERROR(cls):
        return cls("Error")
    
    @schemas.classproperty
    def SENT(cls):
        return cls("Sent")
    
    @schemas.classproperty
    def OPENED(cls):
        return cls("Opened")
    
    @schemas.classproperty
    def CLICKED(cls):
        return cls("Clicked")
    
    @schemas.classproperty
    def UNSUBSCRIBED(cls):
        return cls("Unsubscribed")
    
    @schemas.classproperty
    def ABUSE_REPORT(cls):
        return cls("AbuseReport")
