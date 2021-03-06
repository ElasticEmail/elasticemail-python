"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    To start using this API, you will need your Access Token (available <a href=\"https://elasticemail.com/account#/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    This is the documentation for REST API. If you’d like to read our legacy documentation regarding Web API v2 click <a href=\"https://api.elasticemail.com/public/help\">here</a>.  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ElasticEmail
from ElasticEmail.api.contacts_api import ContactsApi  # noqa: E501


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self):
        self.api = ContactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_contacts_by_email_delete(self):
        """Test case for contacts_by_email_delete

        Delete Contact  # noqa: E501
        """
        pass

    def test_contacts_by_email_get(self):
        """Test case for contacts_by_email_get

        Load Contact  # noqa: E501
        """
        pass

    def test_contacts_by_email_history_get(self):
        """Test case for contacts_by_email_history_get

        Load History  # noqa: E501
        """
        pass

    def test_contacts_by_email_put(self):
        """Test case for contacts_by_email_put

        Update Contact  # noqa: E501
        """
        pass

    def test_contacts_delete_post(self):
        """Test case for contacts_delete_post

        Delete Contacts Bulk  # noqa: E501
        """
        pass

    def test_contacts_export_by_id_status_get(self):
        """Test case for contacts_export_by_id_status_get

        Check Export Status  # noqa: E501
        """
        pass

    def test_contacts_export_post(self):
        """Test case for contacts_export_post

        Export Contacts  # noqa: E501
        """
        pass

    def test_contacts_get(self):
        """Test case for contacts_get

        Load Contacts  # noqa: E501
        """
        pass

    def test_contacts_import_post(self):
        """Test case for contacts_import_post

        Upload Contacts  # noqa: E501
        """
        pass

    def test_contacts_post(self):
        """Test case for contacts_post

        Add Contact  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
