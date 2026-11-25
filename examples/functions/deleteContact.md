# Delete Contact

This guide will walk you through steps of deleting one contact from your account using the Python library. 

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

Create an instance of ContactsApi that will be used to delete the contact.

```python
    api_instance = ElasticEmail.ContactsApi(api_client)
```

Specify the email address of the contact to delete. To delete many contacts in one call, see [deleteContacts](deleteContacts.md).

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/contactsByEmailDelete

```python
    email = "johnsmith@domain.com"
```

Use try & except block to call `contacts_by_email_delete` method from the API to delete the contact: 

```python
    try:
        # Delete Contact
        api_instance.contacts_by_email_delete(email)
        print("Contact deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_by_email_delete: %s\n" % e)
```


## The whole code to copy and paste:

```python
import os
import sys
import ElasticEmail

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Read the API key from the ELASTICEMAIL_API_KEY environment variable
api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key

"""
Delete contact
Example api call that deletes one contact by its email address.
Required Access Level: ModifyContacts
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ContactsApi(api_client)

    email = "johnsmith@domain.com"  # str | Proper email address.

    try:
        # Delete Contact
        api_instance.contacts_by_email_delete(email)
        print("Contact deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_by_email_delete: %s\n" % e)
```

## Run the code
Set your API key in the environment, then run the file:
```
export ELASTICEMAIL_API_KEY=...
python3 snippet.py
```
