# Send Transactional Emails

This guide will walk you through steps of sending a transactional email using the Python library. 

*Required Access Level: SendHttp*

## What's a transactional email?
When using Elastic Email you send emails to your contacts. One of options is to send transational emails. Transactional emails can be described that they are emails generated as a response to a particular actions done by the subscriber eg. account changes, purchase receipts, other confirmations.

A transactional email have a limit of 50 maximum recipients.


## Preparation
Install Python 3.

Install ElasticEmail library.

Eg. run in terminal `pip install ElasticEmail` to install from PyPi repository.

Create a new Python file `snippet.py` and open it in editor of your preference eg. PyCharm (https://www.jetbrains.com/pycharm/download/)

## Let's dig into the code

Put the below code to your file.

Load libraries using below code:

```python
import ElasticEmail
from ElasticEmail.apis.tags import emails_api
from ElasticEmail.model.email_content import EmailContent
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.transactional_recipient import TransactionalRecipient
from ElasticEmail.model.email_transactional_message_data import EmailTransactionalMessageData
from pprint import pprint
```

Generate and use your API key (remember to check a required access level).

Defining the host is optional and defaults to https://api.elasticemail.com/v4

```python
configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
```

Pass configuration to an api client and make it instance available under `api_client` name:
```
with ElasticEmail.ApiClient(configuration) as api_client:
```

Create an instance of EmailsApi that will be used to send a transactional email.

```python
    api_instance = emails_api.EmailsApi(api_client)
```

First you need to specify email details:
- email recipients
- email content:
    - body parts – in HTML, PlainText or in both
    - from email – it needs to be your validated email address
    - email subject

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/emailsTransactionalPost


```python
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
    )
```

Use try & except block to call `emails_transactional_post` method from the API to send an email: 

```python
    try:
        api_response = api_instance.emails_transactional_post(email_transactional_message_data)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_transactional_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.apis.tags import emails_api
from ElasticEmail.model.email_content import EmailContent
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.transactional_recipient import TransactionalRecipient
from ElasticEmail.model.email_transactional_message_data import EmailTransactionalMessageData
from pprint import pprint

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
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
    )

    try:
        api_response = api_instance.emails_transactional_post(email_transactional_message_data)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_transactional_post: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
