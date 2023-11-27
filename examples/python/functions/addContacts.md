# Add Contacts

This guide will walk you through the process of adding new contacts to your account using the Python library. 

*Required Access Level: ModifyContacts*

## What's contact?
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
from ElasticEmail.api import contacts_api
from ElasticEmail.model.contact_status import ContactStatus
from ElasticEmail.model.contact_payload import ContactPayload
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

Create an instance of ContactsApi that will be used to add contacts.

```python
    api_instance = contacts_api.ContactsApi(api_client)
```

Create an array with new contacts.

You can pass an array with up to 1000 contacts.

The `Email` field is mandatory, the rest is optional.

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/contactsPost


```python
    contact_payload = [
        ContactPayload(
            email="johnsmith@domain.com",
            status=ContactStatus("Active"),
            first_name="John",
            last_name="Smith",
        ),
    ]
```

Specify an existing list name in options, otherwise contacts will be added to all contacts.

```python
    list_names = [
        "New list",
    ]
```


Use try & except block to call `contacts_post` method from the API to add contacts: 

```python
    try:
        api_response = api_instance.contacts_post(contact_payload, listnames=list_names)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.contact_status import ContactStatus
from ElasticEmail.model.contact_payload import ContactPayload
from pprint import pprint

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = contacts_api.ContactsApi(api_client)
    contact_payload = [
        ContactPayload(
            email="johnsmith@domain.com",
            status=ContactStatus("Active"),
            first_name="John",
            last_name="Smith",
        ),
    ]

    list_names = [
        "New list",
    ]

    try:
        api_response = api_instance.contacts_post(contact_payload, listnames=list_names)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_post: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
