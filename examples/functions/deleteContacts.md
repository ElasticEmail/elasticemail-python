# Delete Contacts

This guide will walk you through steps of deleting contact(s) from your account using the Python library. 

*Required Access Level: ModifyContacts*

## What's a contact?
When using Elastic Email, you send emails to contacts – recipients who receive your emails. Contacts can be grouped by created segments or lists.

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
import ElasticEmail
from ElasticEmail.models.emails_payload import EmailsPayload
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
```
with ElasticEmail.ApiClient(configuration) as api_client:
```

Create an instance of ContactsApi that will be used to delete contacts.

```python
    api_instance = ElasticEmail.ContactsApi(api_client)
```

Create an object with an array of email addresses of the contacts to delete. To delete a single contact, see [deleteContact](deleteContact.md).

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/contactsDeletePost

```python
    emails_payload = EmailsPayload(
        Emails=["johnsmith@domain.com"],
    )
```

Use try & except block to call `contacts_delete_post` method from the API to delete contacts: 

```python
    try:
        # Delete Contacts Bulk
        api_instance.contacts_delete_post(emails_payload)
        print("Contacts deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_delete_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
import os
import sys
import ElasticEmail
from ElasticEmail.models.emails_payload import EmailsPayload

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Read the API key from the ELASTICEMAIL_API_KEY environment variable
api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key

"""
Delete contacts
Example api call that deletes contacts in bulk, by a list of email addresses.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ContactsApi(api_client)

    emails_payload = EmailsPayload(
        Emails=["johnsmith@domain.com"],
    )  # EmailsPayload | Provide either rule or a list of emails, not both.

    try:
        # Delete Contacts Bulk
        api_instance.contacts_delete_post(emails_payload)
        print("Contacts deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_delete_post: %s\n" % e)
```

## Run the code
Set your API key in the environment, then run the file:
```
export ELASTICEMAIL_API_KEY=...
python3 snippet.py
```
