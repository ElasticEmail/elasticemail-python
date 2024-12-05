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

from ElasticEmail.api.statistics_api import StatisticsApi


class TestStatisticsApi(unittest.TestCase):
    """StatisticsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StatisticsApi()

    def tearDown(self) -> None:
        pass

    def test_statistics_campaigns_by_name_get(self) -> None:
        """Test case for statistics_campaigns_by_name_get

        Load Campaign Stats
        """
        pass

    def test_statistics_campaigns_get(self) -> None:
        """Test case for statistics_campaigns_get

        Load Campaigns Stats
        """
        pass

    def test_statistics_channels_by_name_get(self) -> None:
        """Test case for statistics_channels_by_name_get

        Load Channel Stats
        """
        pass

    def test_statistics_channels_get(self) -> None:
        """Test case for statistics_channels_get

        Load Channels Stats
        """
        pass

    def test_statistics_get(self) -> None:
        """Test case for statistics_get

        Load Statistics
        """
        pass


if __name__ == '__main__':
    unittest.main()