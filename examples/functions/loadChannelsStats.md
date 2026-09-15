# Load Channels Stats

This example is aligned with the current SDK and can be run directly from `examples/functions/loadChannelsStats.py`.

```python
import ElasticEmail
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Load channels stats
Example api call that loads a list of your channels' stats.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.StatisticsApi(api_client)

    try:
        api_response = api_instance.statistics_channels_get(limit=100, offset=0)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_channels_get: %s\n" % e)
```

Run with:

```bash
py -3 loadChannelsStats.py
```
