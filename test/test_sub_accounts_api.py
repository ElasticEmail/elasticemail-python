# coding: utf-8

"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.    To start using this API, you will need your Access Token (available <a target=\"_blank\" href=\"https://app.elasticemail.com/marketing/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    Downloadable library clients can be found in our Github repository <a target=\"_blank\" href=\"https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme\">here</a>

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ElasticEmail.api.sub_accounts_api import SubAccountsApi


class TestSubAccountsApi(unittest.TestCase):
    """SubAccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SubAccountsApi()

    def tearDown(self) -> None:
        pass

    def test_subaccounts_by_email_credits_patch(self) -> None:
        """Test case for subaccounts_by_email_credits_patch

        Add, Subtract Email Credits
        """
        pass

    def test_subaccounts_by_email_delete(self) -> None:
        """Test case for subaccounts_by_email_delete

        Delete SubAccount
        """
        pass

    def test_subaccounts_by_email_get(self) -> None:
        """Test case for subaccounts_by_email_get

        Load SubAccount
        """
        pass

    def test_subaccounts_by_email_settings_email_put(self) -> None:
        """Test case for subaccounts_by_email_settings_email_put

        Update SubAccount Email Settings
        """
        pass

    def test_subaccounts_get(self) -> None:
        """Test case for subaccounts_get

        Load SubAccounts
        """
        pass

    def test_subaccounts_post(self) -> None:
        """Test case for subaccounts_post

        Add SubAccount
        """
        pass


if __name__ == '__main__':
    unittest.main()
