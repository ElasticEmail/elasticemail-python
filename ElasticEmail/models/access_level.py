# coding: utf-8

"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.    To start using this API, you will need your Access Token (available <a target=\"_blank\" href=\"https://app.elasticemail.com/marketing/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    Downloadable library clients can be found in our Github repository <a target=\"_blank\" href=\"https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme\">here</a>

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AccessLevel(str, Enum):
    """
    AccessLevel
    """

    """
    allowed enum values
    """
    NONE = 'None'
    VIEWACCOUNT = 'ViewAccount'
    VIEWCONTACTS = 'ViewContacts'
    VIEWFORMS = 'ViewForms'
    VIEWTEMPLATES = 'ViewTemplates'
    VIEWCAMPAIGNS = 'ViewCampaigns'
    VIEWCHANNELS = 'ViewChannels'
    VIEWAUTOMATIONS = 'ViewAutomations'
    VIEWSURVEYS = 'ViewSurveys'
    VIEWSETTINGS = 'ViewSettings'
    VIEWBILLING = 'ViewBilling'
    VIEWSUBACCOUNTS = 'ViewSubAccounts'
    VIEWUSERS = 'ViewUsers'
    VIEWFILES = 'ViewFiles'
    VIEWREPORTS = 'ViewReports'
    MODIFYACCOUNT = 'ModifyAccount'
    MODIFYCONTACTS = 'ModifyContacts'
    MODIFYFORMS = 'ModifyForms'
    MODIFYTEMPLATES = 'ModifyTemplates'
    MODIFYCAMPAIGNS = 'ModifyCampaigns'
    MODIFYCHANNELS = 'ModifyChannels'
    MODIFYAUTOMATIONS = 'ModifyAutomations'
    MODIFYSURVEYS = 'ModifySurveys'
    MODIFYFILES = 'ModifyFiles'
    EXPORT = 'Export'
    SENDSMTP = 'SendSmtp'
    SENDSMS = 'SendSMS'
    MODIFYSETTINGS = 'ModifySettings'
    MODIFYBILLING = 'ModifyBilling'
    MODIFYPROFILE = 'ModifyProfile'
    MODIFYSUBACCOUNTS = 'ModifySubAccounts'
    MODIFYUSERS = 'ModifyUsers'
    SECURITY = 'Security'
    MODIFYLANGUAGE = 'ModifyLanguage'
    VIEWSUPPORT = 'ViewSupport'
    SENDHTTP = 'SendHttp'
    MODIFY2FAEMAIL = 'Modify2FAEmail'
    MODIFYSUPPORT = 'ModifySupport'
    VIEWCUSTOMFIELDS = 'ViewCustomFields'
    MODIFYCUSTOMFIELDS = 'ModifyCustomFields'
    MODIFYWEBNOTIFICATIONS = 'ModifyWebNotifications'
    EXTENDEDLOGS = 'ExtendedLogs'
    VERIFYEMAILS = 'VerifyEmails'
    MODIFY2FASMS = 'Modify2FASms'
    MODIFYLANDINGPAGES = 'ModifyLandingPages'
    VIEWLANDINGPAGES = 'ViewLandingPages'
    MODIFYSUPPRESSIONS = 'ModifySuppressions'
    VIEWSUPPRESSIONS = 'ViewSuppressions'
    VIEWDRAGDROPEDITOR = 'ViewDragDropEditor'
    VIEWTEMPLATEEDITOR = 'ViewTemplateEditor'
    VIEWAITOOLS = 'ViewAITools'
    MODIFYSUBSCRIPTIONANTISPAM = 'ModifySubscriptionAntiSpam'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccessLevel from a JSON string"""
        return cls(json.loads(json_str))

