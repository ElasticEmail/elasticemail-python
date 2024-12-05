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

from ElasticEmail.models.email_message_data import EmailMessageData

class TestEmailMessageData(unittest.TestCase):
    """EmailMessageData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailMessageData:
        """Test EmailMessageData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailMessageData`
        """
        model = EmailMessageData()
        if include_optional:
            return EmailMessageData(
                recipients = [
                    ElasticEmail.models.email_recipient.EmailRecipient(
                        email = 'mail@example.com', 
                        fields = {"city":"New York","age":"34"}, )
                    ],
                content = ElasticEmail.models.email_content.EmailContent(
                    body = [
                        ElasticEmail.models.body_part.BodyPart(
                            content_type = 'HTML', 
                            content = '', 
                            charset = '', )
                        ], 
                    merge = {"city":"New York","age":"34"}, 
                    attachments = [
                        ElasticEmail.models.message_attachment.MessageAttachment(
                            binary_content = 'YQ==', 
                            name = '', 
                            size = 100, )
                        ], 
                    headers = {"city":"New York","age":"34"}, 
                    postback = '', 
                    envelope_from = 'John Doe <email@domain.com>', 
                    from = 'John Doe <email@domain.com>', 
                    reply_to = 'John Doe <email@domain.com>', 
                    subject = 'Hello!', 
                    template_name = 'Template01', 
                    attach_files = ["preuploaded.jpg"], 
                    utm = ElasticEmail.models.utm.Utm(
                        source = '', 
                        medium = '', 
                        campaign = '', 
                        content = '', ), ),
                options = ElasticEmail.models.options.Options(
                    time_offset = 56, 
                    pool_name = 'My Custom Pool', 
                    channel_name = 'Channel01', 
                    encoding = 'UserProvided', 
                    track_opens = True, 
                    track_clicks = True, )
            )
        else:
            return EmailMessageData(
                recipients = [
                    ElasticEmail.models.email_recipient.EmailRecipient(
                        email = 'mail@example.com', 
                        fields = {"city":"New York","age":"34"}, )
                    ],
                content = ElasticEmail.models.email_content.EmailContent(
                    body = [
                        ElasticEmail.models.body_part.BodyPart(
                            content_type = 'HTML', 
                            content = '', 
                            charset = '', )
                        ], 
                    merge = {"city":"New York","age":"34"}, 
                    attachments = [
                        ElasticEmail.models.message_attachment.MessageAttachment(
                            binary_content = 'YQ==', 
                            name = '', 
                            size = 100, )
                        ], 
                    headers = {"city":"New York","age":"34"}, 
                    postback = '', 
                    envelope_from = 'John Doe <email@domain.com>', 
                    from = 'John Doe <email@domain.com>', 
                    reply_to = 'John Doe <email@domain.com>', 
                    subject = 'Hello!', 
                    template_name = 'Template01', 
                    attach_files = ["preuploaded.jpg"], 
                    utm = ElasticEmail.models.utm.Utm(
                        source = '', 
                        medium = '', 
                        campaign = '', 
                        content = '', ), ),
        )
        """

    def testEmailMessageData(self):
        """Test EmailMessageData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()