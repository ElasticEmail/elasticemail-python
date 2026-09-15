# Delete Campaign

This example is aligned with the current SDK and can be run directly from `examples/functions/deleteCampaign.py`.

```python
import ElasticEmail

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

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

Run with:

```bash
py -3 deleteCampaign.py
```
