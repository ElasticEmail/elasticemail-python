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

from ElasticEmail.api.contacts_api import ContactsApi


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContactsApi()

    def tearDown(self) -> None:
        pass

    def test_contacts_by_email_delete(self) -> None:
        """Test case for contacts_by_email_delete

        Delete Contact
        """
        pass

    def test_contacts_by_email_get(self) -> None:
        """Test case for contacts_by_email_get

        Load Contact
        """
        pass

    def test_contacts_by_email_put(self) -> None:
        """Test case for contacts_by_email_put

        Update Contact
        """
        pass

    def test_contacts_delete_post(self) -> None:
        """Test case for contacts_delete_post

        Delete Contacts Bulk
        """
        pass

    def test_contacts_export_by_id_status_get(self) -> None:
        """Test case for contacts_export_by_id_status_get

        Check Export Status
        """
        pass

    def test_contacts_export_post(self) -> None:
        """Test case for contacts_export_post

        Export Contacts
        """
        pass

    def test_contacts_get(self) -> None:
        """Test case for contacts_get

        Load Contacts
        """
        pass

    def test_contacts_import_post(self) -> None:
        """Test case for contacts_import_post

        Upload Contacts
        """
        pass

    def test_contacts_post(self) -> None:
        """Test case for contacts_post

        Add Contact
        """
        pass


if __name__ == '__main__':
    unittest.main()