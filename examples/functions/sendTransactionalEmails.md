# Send Transactional Emails

This example is aligned with the current SDK and can be run directly from `examples/functions/sendTransactionalEmails.py`.

```python
import ElasticEmail
from ElasticEmail.models.email_content import EmailContent
from ElasticEmail.models.body_part import BodyPart
from ElasticEmail.models.body_content_type import BodyContentType
from ElasticEmail.models.transactional_recipient import TransactionalRecipient
from ElasticEmail.models.email_transactional_message_data import EmailTransactionalMessageData
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Send transactional emails
Example api call that sends transactional email.
Limit of 50 maximum recipients.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.EmailsApi(api_client)
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
```

Run with:

```bash
py -3 sendTransactionalEmails.py
```
