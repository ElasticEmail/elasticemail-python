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
import ElasticEmail
from ElasticEmail.apis.tags import contacts_api
from ElasticEmail.model.emails_payload import EmailsPayload
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

Create an instance of ContactsApi that will be used to delete contacts.

```python
    api_instance = contacts_api.ContactsApi(api_client)
```

Create an object with an array of contacts to delete.

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/contactsByEmailDelete

```python
    emails_payload = EmailsPayload(
        Emails=["johnsmith@domain.com"],
    )
```

Use try & except block to call `contacts_delete_post` method from the API to delete contacts: 

```python
    try:
        api_instance.contacts_delete_post(emails_payload)
        print("Contacts deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_delete_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.apis.tags import contacts_api
from ElasticEmail.model.emails_payload import EmailsPayload

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = contacts_api.ContactsApi(api_client)

    emails_payload = EmailsPayload(
        Emails=["johnsmith@domain.com"],
    )

    try:
        api_instance.contacts_delete_post(emails_payload)
        print("Contacts deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_delete_post: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
