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


class AccessLevel(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "None": "NONE",
            "ViewAccount": "VIEW_ACCOUNT",
            "ViewContacts": "VIEW_CONTACTS",
            "ViewForms": "VIEW_FORMS",
            "ViewTemplates": "VIEW_TEMPLATES",
            "ViewCampaigns": "VIEW_CAMPAIGNS",
            "ViewChannels": "VIEW_CHANNELS",
            "ViewAutomations": "VIEW_AUTOMATIONS",
            "ViewSurveys": "VIEW_SURVEYS",
            "ViewSettings": "VIEW_SETTINGS",
            "ViewBilling": "VIEW_BILLING",
            "ViewSubAccounts": "VIEW_SUB_ACCOUNTS",
            "ViewUsers": "VIEW_USERS",
            "ViewFiles": "VIEW_FILES",
            "ViewReports": "VIEW_REPORTS",
            "ModifyAccount": "MODIFY_ACCOUNT",
            "ModifyContacts": "MODIFY_CONTACTS",
            "ModifyForms": "MODIFY_FORMS",
            "ModifyTemplates": "MODIFY_TEMPLATES",
            "ModifyCampaigns": "MODIFY_CAMPAIGNS",
            "ModifyChannels": "MODIFY_CHANNELS",
            "ModifyAutomations": "MODIFY_AUTOMATIONS",
            "ModifySurveys": "MODIFY_SURVEYS",
            "ModifyFiles": "MODIFY_FILES",
            "Export": "EXPORT",
            "SendSmtp": "SEND_SMTP",
            "SendSMS": "SEND_SMS",
            "ModifySettings": "MODIFY_SETTINGS",
            "ModifyBilling": "MODIFY_BILLING",
            "ModifyProfile": "MODIFY_PROFILE",
            "ModifySubAccounts": "MODIFY_SUB_ACCOUNTS",
            "ModifyUsers": "MODIFY_USERS",
            "Security": "SECURITY",
            "ModifyLanguage": "MODIFY_LANGUAGE",
            "ViewSupport": "VIEW_SUPPORT",
            "SendHttp": "SEND_HTTP",
            "Modify2FAEmail": "MODIFY2FAEMAIL",
            "ModifySupport": "MODIFY_SUPPORT",
            "ViewCustomFields": "VIEW_CUSTOM_FIELDS",
            "ModifyCustomFields": "MODIFY_CUSTOM_FIELDS",
            "ModifyWebNotifications": "MODIFY_WEB_NOTIFICATIONS",
            "ExtendedLogs": "EXTENDED_LOGS",
            "VerifyEmails": "VERIFY_EMAILS",
            "Modify2FASms": "MODIFY2FASMS",
            "DisableContactsStore": "DISABLE_CONTACTS_STORE",
            "ModifyLandingPages": "MODIFY_LANDING_PAGES",
            "ViewLandingPages": "VIEW_LANDING_PAGES",
            "ModifySuppressions": "MODIFY_SUPPRESSIONS",
            "ViewSuppressions": "VIEW_SUPPRESSIONS",
            "ViewDragDropEditor": "VIEW_DRAG_DROP_EDITOR",
            "ViewTemplateEditor": "VIEW_TEMPLATE_EDITOR",
        }
    
    @schemas.classproperty
    def NONE(cls):
        return cls("None")
    
    @schemas.classproperty
    def VIEW_ACCOUNT(cls):
        return cls("ViewAccount")
    
    @schemas.classproperty
    def VIEW_CONTACTS(cls):
        return cls("ViewContacts")
    
    @schemas.classproperty
    def VIEW_FORMS(cls):
        return cls("ViewForms")
    
    @schemas.classproperty
    def VIEW_TEMPLATES(cls):
        return cls("ViewTemplates")
    
    @schemas.classproperty
    def VIEW_CAMPAIGNS(cls):
        return cls("ViewCampaigns")
    
    @schemas.classproperty
    def VIEW_CHANNELS(cls):
        return cls("ViewChannels")
    
    @schemas.classproperty
    def VIEW_AUTOMATIONS(cls):
        return cls("ViewAutomations")
    
    @schemas.classproperty
    def VIEW_SURVEYS(cls):
        return cls("ViewSurveys")
    
    @schemas.classproperty
    def VIEW_SETTINGS(cls):
        return cls("ViewSettings")
    
    @schemas.classproperty
    def VIEW_BILLING(cls):
        return cls("ViewBilling")
    
    @schemas.classproperty
    def VIEW_SUB_ACCOUNTS(cls):
        return cls("ViewSubAccounts")
    
    @schemas.classproperty
    def VIEW_USERS(cls):
        return cls("ViewUsers")
    
    @schemas.classproperty
    def VIEW_FILES(cls):
        return cls("ViewFiles")
    
    @schemas.classproperty
    def VIEW_REPORTS(cls):
        return cls("ViewReports")
    
    @schemas.classproperty
    def MODIFY_ACCOUNT(cls):
        return cls("ModifyAccount")
    
    @schemas.classproperty
    def MODIFY_CONTACTS(cls):
        return cls("ModifyContacts")
    
    @schemas.classproperty
    def MODIFY_FORMS(cls):
        return cls("ModifyForms")
    
    @schemas.classproperty
    def MODIFY_TEMPLATES(cls):
        return cls("ModifyTemplates")
    
    @schemas.classproperty
    def MODIFY_CAMPAIGNS(cls):
        return cls("ModifyCampaigns")
    
    @schemas.classproperty
    def MODIFY_CHANNELS(cls):
        return cls("ModifyChannels")
    
    @schemas.classproperty
    def MODIFY_AUTOMATIONS(cls):
        return cls("ModifyAutomations")
    
    @schemas.classproperty
    def MODIFY_SURVEYS(cls):
        return cls("ModifySurveys")
    
    @schemas.classproperty
    def MODIFY_FILES(cls):
        return cls("ModifyFiles")
    
    @schemas.classproperty
    def EXPORT(cls):
        return cls("Export")
    
    @schemas.classproperty
    def SEND_SMTP(cls):
        return cls("SendSmtp")
    
    @schemas.classproperty
    def SEND_SMS(cls):
        return cls("SendSMS")
    
    @schemas.classproperty
    def MODIFY_SETTINGS(cls):
        return cls("ModifySettings")
    
    @schemas.classproperty
    def MODIFY_BILLING(cls):
        return cls("ModifyBilling")
    
    @schemas.classproperty
    def MODIFY_PROFILE(cls):
        return cls("ModifyProfile")
    
    @schemas.classproperty
    def MODIFY_SUB_ACCOUNTS(cls):
        return cls("ModifySubAccounts")
    
    @schemas.classproperty
    def MODIFY_USERS(cls):
        return cls("ModifyUsers")
    
    @schemas.classproperty
    def SECURITY(cls):
        return cls("Security")
    
    @schemas.classproperty
    def MODIFY_LANGUAGE(cls):
        return cls("ModifyLanguage")
    
    @schemas.classproperty
    def VIEW_SUPPORT(cls):
        return cls("ViewSupport")
    
    @schemas.classproperty
    def SEND_HTTP(cls):
        return cls("SendHttp")
    
    @schemas.classproperty
    def MODIFY2FAEMAIL(cls):
        return cls("Modify2FAEmail")
    
    @schemas.classproperty
    def MODIFY_SUPPORT(cls):
        return cls("ModifySupport")
    
    @schemas.classproperty
    def VIEW_CUSTOM_FIELDS(cls):
        return cls("ViewCustomFields")
    
    @schemas.classproperty
    def MODIFY_CUSTOM_FIELDS(cls):
        return cls("ModifyCustomFields")
    
    @schemas.classproperty
    def MODIFY_WEB_NOTIFICATIONS(cls):
        return cls("ModifyWebNotifications")
    
    @schemas.classproperty
    def EXTENDED_LOGS(cls):
        return cls("ExtendedLogs")
    
    @schemas.classproperty
    def VERIFY_EMAILS(cls):
        return cls("VerifyEmails")
    
    @schemas.classproperty
    def MODIFY2FASMS(cls):
        return cls("Modify2FASms")
    
    @schemas.classproperty
    def DISABLE_CONTACTS_STORE(cls):
        return cls("DisableContactsStore")
    
    @schemas.classproperty
    def MODIFY_LANDING_PAGES(cls):
        return cls("ModifyLandingPages")
    
    @schemas.classproperty
    def VIEW_LANDING_PAGES(cls):
        return cls("ViewLandingPages")
    
    @schemas.classproperty
    def MODIFY_SUPPRESSIONS(cls):
        return cls("ModifySuppressions")
    
    @schemas.classproperty
    def VIEW_SUPPRESSIONS(cls):
        return cls("ViewSuppressions")
    
    @schemas.classproperty
    def VIEW_DRAG_DROP_EDITOR(cls):
        return cls("ViewDragDropEditor")
    
    @schemas.classproperty
    def VIEW_TEMPLATE_EDITOR(cls):
        return cls("ViewTemplateEditor")
