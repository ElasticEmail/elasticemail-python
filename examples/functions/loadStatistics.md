# Load Statistics

This guide will walk you through steps of loading basic delivery statistics from your account using the Python library. 

*Required Access Level: ViewReports*

## What statistics are returned?
When using Elastic Email you send emails to your contacts from that we create some statistics reports for you eg. number of emails sent, number of delivered messages, number of bounced messages, number of unsubscribed messages etc.

## Preparation
Install Python 3.

Install ElasticEmail library.

Eg. run in terminal `pip install ElasticEmail` to install from PyPi repository.

Create a new Python file `snippet.py` and open it in editor of your preference eg. PyCharm (https://www.jetbrains.com/pycharm/download/)

## Let's dig into the code

Put the below code to your file.

Load libraries using below code:

```python
from datetime import datetime
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

Create an instance of StatisticsApi that will be used to get basic send statistics.

```python
    api_instance = ElasticEmail.StatisticsApi(api_client)
```

First you need to specify a date range:
- from date
- to date – optional

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/statisticsGet


```python
    _from = datetime(2022,1,1,00,00,00)
    to = datetime(2022,1,30,00,00,00)
```

Use try & except block to call `statistics_get` method from the API to load a statistics with only `from` date given: 

```python
    try:
        # Load Statistics
        api_response = api_instance.statistics_get(var_from=_from)
        print("From %s" % _from)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_get: %s\n" % e)
```

Use try & except block to call `statistics_get` method from the API to load a statistics with `from` and `to` dates given: 

```python
    try:
        api_response = api_instance.statistics_get(var_from=_from, to=to)
        print(f"\nFrom {_from} To {to}")
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_get: %s\n" % e)
```


## The whole code to copy and paste:

```python
from datetime import datetime
import ElasticEmail
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Load statistics
Example api call that loads basic statistics.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.StatisticsApi(api_client)
    
    _from = datetime(2022,1,1,00,00,00)  # datetime | Starting date for search in YYYY-MM-DDThh:mm:ss format.
    to = datetime(2022,1,30,00,00,00)  # datetime | Ending date for search in YYYY-MM-DDThh:mm:ss format. (optional)

    # only from date:
    try:
        # Load Statistics
        api_response = api_instance.statistics_get(var_from=_from)
        print("From %s" % _from)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_get: %s\n" % e)

    # from and to dates:
    try:
        api_response = api_instance.statistics_get(var_from=_from, to=to)
        print(f"\nFrom {_from} To {to}")
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_get: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
