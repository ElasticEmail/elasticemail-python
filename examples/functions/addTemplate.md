# Add Template

This guide will walk you through the process of adding a new template to your account using the Python library. 

*Required Access Level: ModifyTemplates*

## What's a tempalte?
When using Elastic Email you send emails to your contacts. A single template is a body of  email prepared and saved under given name. Till it's deleted it can be reused to send any number of emails.

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
from ElasticEmail.apis.tags import templates_api
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.template_payload import TemplatePayload
from ElasticEmail.model.template_scope import TemplateScope
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

Create an instance of TemplatesApi that will be used to create a new template.

```python
    api_instance = templates_api.TemplatesApi(api_client)
```

Create an object with details about new template:
- Name – name of your template by which it can be identified and used
- Subject – specify default subject for this template
- Body – specify acctual body content eg. in HTML, PlainText or both
- TemplateScope – specify scope, "Personal" template won't be shared, "Global" template can be shared with your sub accounts.

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/templatesPost


```python
    template_payload = TemplatePayload(
        Name="My new template",
        Subject="Default subject",
        Body=[
            BodyPart(
                ContentType=BodyContentType("HTML"),
                Content="My template",
                Charset="utf-8",
            ),
        ],
        TemplateScope=TemplateScope("Personal"),
    )
```

Use try & except block to call `templates_post` method from the API to create a template: 

```python
    try:
        api_response = api_instance.templates_post(body = template_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.apis.tags import templates_api
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.template_payload import TemplatePayload
from ElasticEmail.model.template_scope import TemplateScope
from pprint import pprint

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = templates_api.TemplatesApi(api_client)

    template_payload = TemplatePayload(
        Name="My new template",
        Subject="Default subject",
        Body=[
            BodyPart(
                ContentType=BodyContentType("HTML"),
                Content="My template",
                Charset="utf-8",
            ),
        ],
        TemplateScope=TemplateScope("Personal"),
    )

    try:
        api_response = api_instance.templates_post(body = template_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_post: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
