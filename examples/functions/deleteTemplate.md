# Delete Template

This guide will walk you through steps of deleting existing template from your account using the Python library. 

*Required Access Level: ModifyTemplates*

## What's a template?
When using Elastic Email you send emails to your contacts. A single template is a body of  email prepared and saved under given name. Till it's deleted it can be reused to send any number of emails.

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
from ElasticEmail.api import templates_api
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

Create an instance of TemplatesApi that will be used to delete existing template from your account.

```python
    api_instance = templates_api.TemplatesApi(api_client)
```

To delete a template you need to specfiy it's name:

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/templatesByNameDelete


```python
    name = "My template"
```

Use try & except block to call `templates_by_name_delete` method from the API to delete a template: 

```python
    try:
        api_instance.templates_by_name_delete(name)
        print("Template deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_by_name_delete: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.api import templates_api

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = templates_api.TemplatesApi(api_client)

    name = "My template"

    try:
        api_instance.templates_by_name_delete(name)
        print("Template deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_by_name_delete: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
