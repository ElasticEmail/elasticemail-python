# Load Statistics

This example is aligned with the current SDK and can be run directly from `examples/functions/loadStatistics.py`.

```python
from datetime import datetime
import ElasticEmail
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

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

Run with:

```bash
py -3 loadStatistics.py
```
