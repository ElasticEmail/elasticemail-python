# Load Campaigns Statistics

This guide will walk you through steps of loading statistics for each campaign from your account using the Python library. 

*Required Access Level: ViewChannels*

## What statistics are returned?
When using Elastic Email you send email campaigns to your contacts. From that we create statistics reports for you eg. number of emails sent, number of delivered messages,Number of opened messages, number of unsubscribed messages, number of clicked messages etc.

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
from ElasticEmail.api import statistics_api
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

Create an instance of StatisticsApi that will be used to get basic send statistics.

```python
    api_instance = statistics_api.StatisticsApi(api_client)
```

Campaigns statistics reponse is paginated you need to specfiy pagination options:
- limit – maximum returned items, `limit = 0` means to return everything till the end of the list
- offset – how many items should be skipped from begging

Eg. to return second page of elements paginated 20 elements per page specify pagination options as follows
```
    limit = 20
    offset = 20
```

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/statisticsCampaignsByNameGet

Let's fetch first 100 campaigns:

```python
    limit = 100
    offset = 0 
```

Use try & except block to call `statistics_campaigns_get` method from the API to fetch statistics: 

```python
    try:
        api_response = api_instance.statistics_campaigns_get(limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_campaigns_get: %s\n" % e)
```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.api import statistics_api
from pprint import pprint

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = statistics_api.StatisticsApi(api_client)

    limit = 100
    offset = 0

    try:
        api_response = api_instance.statistics_campaigns_get(limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_campaigns_get: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
