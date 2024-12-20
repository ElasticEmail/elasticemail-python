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

from ElasticEmail.models.domain_data import DomainData

class TestDomainData(unittest.TestCase):
    """DomainData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainData:
        """Test DomainData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainData`
        """
        model = DomainData()
        if include_optional:
            return DomainData(
                validation_log = '',
                domain = 'example.com',
                default_domain = True,
                spf = True,
                dkim = True,
                mx = True,
                dmarc = True,
                is_rewrite_domain_valid = True,
                verify = True,
                type = 'None',
                tracking_status = 'Validated',
                certificate_status = 'ErrorOccured',
                certificate_validation_error = '',
                tracking_type_user_request = 'None',
                verp = True,
                custom_bounces_domain = '',
                is_custom_bounces_domain_default = True,
                is_marked_for_deletion = True,
                ownership = 'Current'
            )
        else:
            return DomainData(
        )
        """

    def testDomainData(self):
        """Test DomainData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
