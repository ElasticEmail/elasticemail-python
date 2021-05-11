"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    To start using this API, you will need your Access Token (available <a href=\"https://elasticemail.com/account#/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    This is the documentation for REST API. If you’d like to read our legacy documentation regarding Web API v2 click <a href=\"https://api.elasticemail.com/public/help\">here</a>.  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ElasticEmail
from ElasticEmail.api.suppressions_api import SuppressionsApi  # noqa: E501


class TestSuppressionsApi(unittest.TestCase):
    """SuppressionsApi unit test stubs"""

    def setUp(self):
        self.api = SuppressionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_suppressions_bounces_get(self):
        """Test case for suppressions_bounces_get

        Get Bounce List  # noqa: E501
        """
        pass

    def test_suppressions_bounces_import_post(self):
        """Test case for suppressions_bounces_import_post

        Add Bounces Async  # noqa: E501
        """
        pass

    def test_suppressions_bounces_post(self):
        """Test case for suppressions_bounces_post

        Add Bounces  # noqa: E501
        """
        pass

    def test_suppressions_by_email_delete(self):
        """Test case for suppressions_by_email_delete

        Delete Suppression  # noqa: E501
        """
        pass

    def test_suppressions_by_email_get(self):
        """Test case for suppressions_by_email_get

        Get Suppression  # noqa: E501
        """
        pass

    def test_suppressions_complaints_get(self):
        """Test case for suppressions_complaints_get

        Get Complaints List  # noqa: E501
        """
        pass

    def test_suppressions_complaints_import_post(self):
        """Test case for suppressions_complaints_import_post

        Add Complaints Async  # noqa: E501
        """
        pass

    def test_suppressions_complaints_post(self):
        """Test case for suppressions_complaints_post

        Add Complaints  # noqa: E501
        """
        pass

    def test_suppressions_get(self):
        """Test case for suppressions_get

        Get Suppressions  # noqa: E501
        """
        pass

    def test_suppressions_unsubscribes_get(self):
        """Test case for suppressions_unsubscribes_get

        Get Unsubscribes List  # noqa: E501
        """
        pass

    def test_suppressions_unsubscribes_import_post(self):
        """Test case for suppressions_unsubscribes_import_post

        Add Unsubscribes Async  # noqa: E501
        """
        pass

    def test_suppressions_unsubscribes_post(self):
        """Test case for suppressions_unsubscribes_post

        Add Unsubscribes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
