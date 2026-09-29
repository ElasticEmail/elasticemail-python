# Load Campaign

This guide will walk you through the process of loading details about an existing campaign in your account using the Python library. Example details you can get are like: name, status, recipients, subject etc.

*Required Access Level: ViewCampaigns*

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

Create an instance of CampaignsApi that will be used to load a campaign.

```python
    api_instance = ElasticEmail.CampaignsApi(api_client)
```

The only thing you need to specify is a campaign name

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/campaignsGet


```python
    name = "hello campaign"
```

Use try & except block to call `campaigns_by_name_get` method from the API to fetch campaign details: 

```python
    try:
        # Load Campaign
        api_response = api_instance.campaigns_by_name_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_get: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Load Campaign
Example api call that fetches details about single campaign like: name, status, recipients, subject etc.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.CampaignsApi(api_client)

    name = "hello campaign"  # str | Name of Campaign to get

    # Call api
    try:
        # Load Campaign
        api_response = api_instance.campaigns_by_name_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_get: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
