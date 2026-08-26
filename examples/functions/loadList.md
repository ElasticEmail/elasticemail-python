# Load List

This guide will walk you through the process of loading details about contacts list on your account using the Python library. 

*Required Access Level: ViewContacts*

## What's a list?
When using Elastic Email, you send emails to contacts – recipients who receive your emails. Contacts can be grouped by created segments or lists. Segments add contacts automatically when specfied conditions are met, and contacts on lists are managed manually.

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
from ElasticEmail.apis.tags import lists_api
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

Create an instance of ListsApi that will be used to load list.

```python
    api_instance = lists_api.ListsApi(api_client)
```

The only thing needed is a list name.

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/listsByNameGet


```python
    name = "Best contacts"
```

Use try & except block to call `lists_by_name_get` method from the API to fetch a list: 

```python
    try:
        api_response = api_instance.lists_by_name_get({'name': name})
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_get: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.apis.tags import lists_api
from pprint import pprint

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = lists_api.ListsApi(api_client)

    name = "Best contacts"

    try:
        api_response = api_instance.lists_by_name_get({'name': name})
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_get: %s\n" % e)

```

## Run the code
```
python3 snippet.py
```
