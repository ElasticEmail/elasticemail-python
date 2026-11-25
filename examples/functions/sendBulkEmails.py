import os
import sys
import uuid
import ElasticEmail
from ElasticEmail.models.email_content import EmailContent
from ElasticEmail.models.body_part import BodyPart
from ElasticEmail.models.body_content_type import BodyContentType
from ElasticEmail.models.email_recipient import EmailRecipient
from ElasticEmail.models.email_message_data import EmailMessageData
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Read the API key from the ELASTICEMAIL_API_KEY environment variable
api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key

"""
Send bulk emails
Example api call that sends bulk merge email.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.EmailsApi(api_client)
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

    # One key per send. Reuse it only to retry this send with the same data.
    idempotency_key = str(uuid.uuid4())


    try:
        # Send Bulk Emails
        api_response = api_instance.emails_post(email_message_data, idempotency_key=idempotency_key)
        pprint(api_response)
        print(f"TransactionID: {api_response.transaction_id}, Idempotency-Key: {idempotency_key}")
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_post: %s\n" % e)
