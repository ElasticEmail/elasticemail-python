import ElasticEmail
from ElasticEmail.apis.tags import emails_api
from ElasticEmail.model.email_content import EmailContent
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.transactional_recipient import TransactionalRecipient
from ElasticEmail.model.email_transactional_message_data import EmailTransactionalMessageData
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Send transactional emails
Example api call that sends transactional email.
Limit of 50 maximum recipients.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emails_api.EmailsApi(api_client)

    email_transactional_message_data = EmailTransactionalMessageData(
        Recipients=TransactionalRecipient(
            To=[
                "johnsmith@domain.com",
            ],
        ),
        Content=EmailContent(
            Body=[
                BodyPart(
                    ContentType=BodyContentType("HTML"),
                    Content="<strong>Mail content.<strong>",
                    Charset="utf-8",
                ),
                BodyPart(
                    ContentType=BodyContentType("PlainText"),
                    Content="Mail content.",
                    Charset="utf-8",
                ),
            ],
            From="myemail@domain.com",
            ReplyTo="myemail@domain.com",
            Subject="Example transactional email",
        ),
    ) # EmailTransactionalMessageData | Email data

    try:
        # Send Transactional Email
        api_response = api_instance.emails_transactional_post(email_transactional_message_data)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_transactional_post: %s\n" % e)
