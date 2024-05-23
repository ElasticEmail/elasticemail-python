import ElasticEmail
from ElasticEmail.apis.tags import emails_api
from ElasticEmail.model.email_content import EmailContent
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.email_recipient import EmailRecipient
from ElasticEmail.model.email_message_data import EmailMessageData
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Send bulk emails
Example api call that sends bulk merge email.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emails_api.EmailsApi(api_client)
    email_message_data = EmailMessageData(
        Recipients=[
            EmailRecipient(
                Email="johnsmith@domain.com",
                Fields={
                    "name": "John",
                },
            ),
        ],
        Content=EmailContent(
            body=[
                BodyPart(
                    ContentType=BodyContentType("HTML"),
                    Content="<strong>Hi {name}!<strong>",
                    Charset="utf-8",
                ),
                BodyPart(
                    ContentType=BodyContentType("PlainText"),
                    Content="Hi {name}!",
                    Charset="utf-8",
                ),
            ],
            From="myemail@domain.com",
            ReplyTo="myemail@domain.com",
            Subject="Example email",
        ),
    ) # EmailMessageData | Email data

    try:
        # Send Bulk Emails
        api_response = api_instance.emails_post(email_message_data)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_post: %s\n" % e)
