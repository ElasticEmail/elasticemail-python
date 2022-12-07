# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import ElasticEmail
from ElasticEmail.paths.subaccounts_email_credits import patch  # noqa: E501
from ElasticEmail import configuration, schemas, api_client

from .. import ApiTestMixin


class TestSubaccountsEmailCredits(ApiTestMixin, unittest.TestCase):
    """
    SubaccountsEmailCredits unit test stubs
        Add, Subtract Email Credits  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''




if __name__ == '__main__':
    unittest.main()