# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import ElasticEmail
from ElasticEmail.paths.contacts_import import post  # noqa: E501
from ElasticEmail import configuration, schemas, api_client

from .. import ApiTestMixin


class TestContactsImport(ApiTestMixin, unittest.TestCase):
    """
    ContactsImport unit test stubs
        Upload Contacts  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 202
    response_body = ''


if __name__ == '__main__':
    unittest.main()
