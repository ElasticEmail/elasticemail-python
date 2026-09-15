# Load Campaign

This example is aligned with the current SDK and can be run directly from `examples/functions/loadCampaign.py`.

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

Run with:

```bash
py -3 loadCampaign.py
```
