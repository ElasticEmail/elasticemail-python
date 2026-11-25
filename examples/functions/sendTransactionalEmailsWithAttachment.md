# Send Transactional Emails With Attachment

This guide will walk you through steps of sending a transactional email with an attachment using the Python library. 

*Required Access Level: SendHttp*

## What's a transactional email?
When using Elastic Email you send emails to your contacts. One of options is to send transational emails. Transactional emails can be described that they are emails generated as a response to a particular actions done by the subscriber eg. account changes, purchase receipts, other confirmations.

A transactional email have a limit of 50 maximum recipients.


## Preparation
Install Python 3.

Install ElasticEmail library.

Eg. run in terminal `pip install ElasticEmail` to install from PyPi repository.

Create a new Python file `snippet.py` and open it in editor of your preference eg. PyCharm (https://www.jetbrains.com/pycharm/download/)

Put the file you want to attach, eg. `invoice.pdf`, in the same folder as `snippet.py`.

## Let's dig into the code

Put the below code to your file.

Load libraries using below code:

```python
import os
import sys
import uuid
import ElasticEmail
from pprint import pprint
import base64
from pathlib import Path
```

Read your API key from the `ELASTICEMAIL_API_KEY` environment variable and stop with a clear message if it isn't set (remember to check a required access level).

Defining the host is optional and defaults to https://api.elasticemail.com/v4

```python
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key
```

Pass configuration to an api client and make it instance available under `api_client` name:
```
with ElasticEmail.ApiClient(configuration) as api_client:
```

Create an instance of EmailsApi that will be used to send a transactional email.

```python
    api_instance = ElasticEmail.EmailsApi(api_client)
```

Load the file you want to attach. The snippet looks for `invoice.pdf` next to your script and stops if it's not there.

```python
    invoice_path = Path(__file__).with_name("invoice.pdf")
    if not invoice_path.exists():
        print(f"Attachment file not found: {invoice_path}. Skipping send.")
        raise SystemExit(0)

    with open(invoice_path, 'rb') as file:
        binData = file.read()
```

Next you need to specify email details:
- email recipients
- email content:
    - body parts – in HTML, PlainText or in both
    - from email – it needs to be your validated email address
    - email subject
    - attachments – file content encoded in base64 and the file name the recipient will see

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/emailsTransactionalPost


```python
    email_transactional_message_data = ElasticEmail.EmailTransactionalMessageData(
        Recipients=ElasticEmail.TransactionalRecipient(
            To=[
                "RECIPIENT@EMAIL.ADDRESS",
            ],
        ),
        Content=ElasticEmail.EmailContent(
            Body=[
                ElasticEmail.BodyPart(
                    ContentType=ElasticEmail.BodyContentType("HTML"),
                    Content="<strong>Mail content.<strong>",
                    Charset="utf-8",
                ),
                ElasticEmail.BodyPart(
                    ContentType=ElasticEmail.BodyContentType("PlainText"),
                    Content="Mail content.",
                    Charset="utf-8",
                ),
            ],
            From="SENDER@EMAIL.ADDRESS",
            ReplyTo="SENDER@EMAIL.ADDRESS",
            Subject="Example transactional email with attachment",
            Attachments=[
                ElasticEmail.MessageAttachment(
                    BinaryContent=base64.b64encode(binData).decode('utf-8'),
                    Name="Invoice.pdf"
                )
            ]
        ),
    )
```

Create an idempotency key for this send. If the request times out, retry it with the same data and the same key, and the email won't be delivered twice.

```python
    idempotency_key = str(uuid.uuid4())
```

Use try & except block to call `emails_transactional_post` method from the API to send an email, passing the idempotency key, and print the `TransactionID` next to the key: 

```python
    try:
        api_response = api_instance.emails_transactional_post(email_transactional_message_data, idempotency_key=idempotency_key)
        print("The response of EmailsApi->emails_transactional_post:\n")
        pprint(api_response)
        print(f"TransactionID: {api_response.transaction_id}, Idempotency-Key: {idempotency_key}")
    except Exception as e:
        print("Exception when calling EmailsApi->emails_transactional_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
import os
import sys
import uuid
import ElasticEmail
from pprint import pprint
import base64
from pathlib import Path

configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = ElasticEmail.EmailsApi(api_client)

    invoice_path = Path(__file__).with_name("invoice.pdf")
    if not invoice_path.exists():
        print(f"Attachment file not found: {invoice_path}. Skipping send.")
        raise SystemExit(0)

    with open(invoice_path, 'rb') as file:
        binData = file.read()

    email_transactional_message_data = ElasticEmail.EmailTransactionalMessageData(
        Recipients=ElasticEmail.TransactionalRecipient(
            To=[
                "RECIPIENT@EMAIL.ADDRESS",
            ],
        ),
        Content=ElasticEmail.EmailContent(
            Body=[
                ElasticEmail.BodyPart(
                    ContentType=ElasticEmail.BodyContentType("HTML"),
                    Content="<strong>Mail content.<strong>",
                    Charset="utf-8",
                ),
                ElasticEmail.BodyPart(
                    ContentType=ElasticEmail.BodyContentType("PlainText"),
                    Content="Mail content.",
                    Charset="utf-8",
                ),
            ],
            From="SENDER@EMAIL.ADDRESS",
            ReplyTo="SENDER@EMAIL.ADDRESS",
            Subject="Example transactional email with attachment",
            Attachments=[
                ElasticEmail.MessageAttachment(
                    BinaryContent=base64.b64encode(binData).decode('utf-8'),
                    Name="Invoice.pdf"
                )
            ]
        ),
    )

    idempotency_key = str(uuid.uuid4())

    try:
        api_response = api_instance.emails_transactional_post(email_transactional_message_data, idempotency_key=idempotency_key)
        print("The response of EmailsApi->emails_transactional_post:\n")
        pprint(api_response)
        print(f"TransactionID: {api_response.transaction_id}, Idempotency-Key: {idempotency_key}")
    except Exception as e:
        print("Exception when calling EmailsApi->emails_transactional_post: %s\n" % e)
```

## Run the code
Set your API key in the environment, then run the file:
```
export ELASTICEMAIL_API_KEY=...
python3 snippet.py
```
