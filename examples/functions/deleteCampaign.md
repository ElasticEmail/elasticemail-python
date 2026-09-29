# Delete Campaign

This guide will walk you through steps to delete an existing campaign from your account.

*Required Access Level: ModifyCampaigns*

## What's a campaign?
When using Elastic Email, when you send an email to any group of contacts we call that a "campaign".

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

Create an instance of CampaignsApi that will be used to delete a campaign.

```python
    api_instance = ElasticEmail.CampaignsApi(api_client)
```

The only thing you need to specify is a campaign name

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/campaignsByNameDelete


```python
    name = "hello campaign"
```

Use try & except block to call `campaigns_by_name_delete` method from the API to delete a campaign: 

```python
    try:
        # Delete Campaign
        api_instance.campaigns_by_name_delete(name)
        print("Campaign deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_delete: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Delete Campaign
Example api call that deletes an existing campaign.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.CampaignsApi(api_client)

    name = "hello campaign"

    try:
        # Delete Campaign
        api_instance.campaigns_by_name_delete(name)
        print("Campaign deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_delete: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
