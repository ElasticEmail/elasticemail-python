# Upload Contacts

This guide will walk you through the process of adding new contacts to your account, by uploading them from a CSV file, using the Python library. 

*Required Access Level: ModifyContacts*

## What's a contact?
When using Elastic Email, you send emails to contacts – recipients who receive your emails. Contacts can be grouped by created segments or lists.

## Preparation
Install Python 3.

Install `elasticemail-python` lib

Eg. run in terminal `pip install git+https://github.com/elasticemail/elasticemail-python.git`

Create a new Python file `snippet.py` and open it in editor of your preference eg. PyCharm (https://www.jetbrains.com/pycharm/download/)

## Let's dig into the code

Put the below code to your file.

Load libraries using below code:

```python
import ElasticEmail
from ElasticEmail.api import contacts_api
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

Create an instance of ContactsApi that will be used to upload contacts.

```python
    api_instance = contacts_api.ContactsApi(api_client)
```


Create options
- file encoding
- optionaly a list name to which contacts should be added, otherwise contacts will be added to all contacts.

```python
    list_name = "Best contacts"

    encoding_name = "utf-8"
```

The simplest CSV file requires only one column `Email`, eg.:

```
Email
john@johnsmith.com
```

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/contactsImportPost

Load file

```python
    file = open('./files/contacts.csv', 'rb')
```

Use try & except block to call `contacts_import_post` method from the API to upload contacts: 

```python
    try:
        api_instance.contacts_import_post(list_name=list_name, encoding_name=encoding_name, file=file)
        print("Contacts uploaded.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_import_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.api import contacts_api

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = contacts_api.ContactsApi(api_client)

    list_name = "Best contacts"

    encoding_name = "utf-8"

    file = open('./files/contacts.csv', 'rb')

    try:
        api_instance.contacts_import_post(list_name=list_name, encoding_name=encoding_name, file=file)
        print("Contacts uploaded.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_import_post: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
