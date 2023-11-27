# Add Campaign

This guide will walk you through the process of creating your first campaign using the Python library. 

*Required Access Level: ModifyCampaigns*

## What's a campaign?
When using Elastic Email, when you send an email to any group of contacts we call that a "campaign".

To send a campaign you need a template (which becomes the email body itself) and you need contacts (the recipients who receive the email).

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
from ElasticEmail.api import campaigns_api
from ElasticEmail.model.campaign import Campaign
from ElasticEmail.model.campaign_recipient import CampaignRecipient
from ElasticEmail.model.campaign_status import CampaignStatus
from ElasticEmail.model.campaign_template import CampaignTemplate
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

Create an instance of CampaignsApi that will be used to create a campaign.

```python
    api_instance = campaigns_api.CampaignsApi(api_client)
```

Create an example campaign object:
- Name: defines campaign name by which you can identify it later
- Recipients: define your audience
- Conent: define your message details
- Status: define status in which campaign should be created

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/campaignsPost

Send will be triggered immediately or postponed, depending on given options. 
Because we define `Status` as `Draft`, so in this case it will be postponed and campaign will be added to drafts.


```python
    campaign = Campaign(
        content=[
            CampaignTemplate(
                _from="karol.szczycinski@elasticemail.com",
                reply_to="karol.szczycinski@elasticemail.com",
                subject="Hello",
                template_name="hello_template",
            ),
        ],
        name="hello campaign",
        status=CampaignStatus("Draft"),
        recipients=CampaignRecipient(
            list_names=[
                "my list name",
            ],
        ),
    )
```

Use try & except block to call `campaigns_post` method from the API to create a campaign: 

```python
    try:
        api_response = api_instance.campaigns_post(campaign)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_post: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.api import campaigns_api
from ElasticEmail.model.campaign import Campaign
from ElasticEmail.model.campaign_recipient import CampaignRecipient
from ElasticEmail.model.campaign_status import CampaignStatus
from ElasticEmail.model.campaign_template import CampaignTemplate
from pprint import pprint

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = campaigns_api.CampaignsApi(api_client)

    campaign = Campaign(
        content=[
            CampaignTemplate(
                _from="karol.szczycinski@elasticemail.com",
                reply_to="karol.szczycinski@elasticemail.com",
                subject="Hello",
                template_name="hello_template",
            ),
        ],
        name="hello campaign",
        status=CampaignStatus("Draft"),
        recipients=CampaignRecipient(
            list_names=[
                "my list name",
            ],
        ),
    )

    try:
        api_response = api_instance.campaigns_post(campaign)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_post: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
