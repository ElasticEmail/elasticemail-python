# Send Bulk Emails

This guide will walk you through steps of sending a bulk email using the Python library. 

*Required Access Level: SendHttp*

## What's a bulk email?
When using Elastic Email you send emails to your contacts. One of options is to send bulk emails. Bulk email can be described as a single email message send to a large group at once.


## Preparation
Install Python 3.

Install ElasticEmail library.

Eg. run in terminal `pip install ElasticEmail` to install from PyPi repository.

Create a new Python file `snippet.py` and open it in editor of your preference eg. PyCharm (https://www.jetbrains.com/pycharm/download/)

## Let's dig into the code

Put the below code to your file.

Load libraries using below code:

```python
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
```

Read your API key from the `ELASTICEMAIL_API_KEY` environment variable and stop with a clear message if it isn't set (remember to check a required access level).

Defining the host is optional and defaults to https://api.elasticemail.com/v4

```python
configuration = ElasticEmail.Configuration()
api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key
```

Pass configuration to an api client and make it instance available under `api_client` name:
```python
with ElasticEmail.ApiClient(configuration) as api_client:
```

Create an instance of EmailsApi that will be used to send a bulk email.

```python
    api_instance = ElasticEmail.EmailsApi(api_client)
```

First you need to specify email details:
- email recipients:
    - this example demostrates merge fields usage, for each recipient `{name}` will be changed to recipient's name
- email content:
    - body parts – in HTML, PlainText or in both
    - from email – it needs to be your validated email address
    - email subject

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/emailsPost


```python
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
    )
```

Create an idempotency key for this send. If the request times out, retry it with the same data and the same key, and the email won't be delivered twice.

```python
    idempotency_key = str(uuid.uuid4())
```

Use try & except block to call `emails_post` method from the API to send an email, passing the idempotency key, and print the `TransactionID` next to the key: 

```python
    try:
        # Send Bulk Emails
        api_response = api_instance.emails_post(email_message_data, idempotency_key=idempotency_key)
        pprint(api_response)
        print(f"TransactionID: {api_response.transaction_id}, Idempotency-Key: {idempotency_key}")
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
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

    idempotency_key = str(uuid.uuid4())


    try:
        # Send Bulk Emails
        api_response = api_instance.emails_post(email_message_data, idempotency_key=idempotency_key)
        pprint(api_response)
        print(f"TransactionID: {api_response.transaction_id}, Idempotency-Key: {idempotency_key}")
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_post: %s\n" % e)
```

## Run the code
Set your API key in the environment, then run the file:
```
export ELASTICEMAIL_API_KEY=...
python3 snippet.py
```
