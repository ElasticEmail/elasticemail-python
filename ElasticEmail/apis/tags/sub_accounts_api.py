# coding: utf-8

"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.    To start using this API, you will need your Access Token (available <a target=\"_blank\" href=\"https://app.elasticemail.com/marketing/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    Downloadable library clients can be found in our Github repository <a target=\"_blank\" href=\"https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme\">here</a>  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""

from ElasticEmail.paths.subaccounts_email_credits.patch import SubaccountsByEmailCreditsPatch
from ElasticEmail.paths.subaccounts_email.delete import SubaccountsByEmailDelete
from ElasticEmail.paths.subaccounts_email.get import SubaccountsByEmailGet
from ElasticEmail.paths.subaccounts_email_settings_email.put import SubaccountsByEmailSettingsEmailPut
from ElasticEmail.paths.subaccounts.get import SubaccountsGet
from ElasticEmail.paths.subaccounts.post import SubaccountsPost


class SubAccountsApi(
    SubaccountsByEmailCreditsPatch,
    SubaccountsByEmailDelete,
    SubaccountsByEmailGet,
    SubaccountsByEmailSettingsEmailPut,
    SubaccountsGet,
    SubaccountsPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
