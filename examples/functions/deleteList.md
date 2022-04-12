# Delete List

This guide will walk you through steps of removing contacts list from your account using the Python library. 

*Required Access Level: ModifyContacts*

## What's a list?
When using Elastic Email, you send emails to contacts – recipients who receive your emails. Contacts can be grouped by created segments or lists. Segments add contacts automatically when specfied conditions are met, and contacts on lists are managed manually.

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
from ElasticEmail.api import lists_api
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

Create an instance of ListsApi that will be used to delete list.

```python
    api_instance = lists_api.ListsApi(api_client)
```

The only thing needed is a list name.

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/listsByNameDelete


```python
    name = "Best contacts"
```

Use try & except block to call `lists_by_name_delete` method from the API to delete a list: 

```python
    try:
        api_instance.lists_by_name_delete(name)
        print("List deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_delete: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.api import lists_api

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = lists_api.ListsApi(api_client)

    name = "Best contacts"

    try:
        api_instance.lists_by_name_delete(name)
        print("List deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_delete: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
