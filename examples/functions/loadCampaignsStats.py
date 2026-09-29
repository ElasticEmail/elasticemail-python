import ElasticEmail
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Load Campaigns Stats
Example api call that loads a list of your campaigns' stats.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.StatisticsApi(api_client)

    try:
        api_response = api_instance.statistics_campaigns_get(limit=100, offset=0)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_campaigns_get: %s\n" % e)
