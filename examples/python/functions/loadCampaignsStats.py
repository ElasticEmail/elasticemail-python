import ElasticEmail
from ElasticEmail.api import statistics_api
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
    api_instance = statistics_api.StatisticsApi(api_client)

    limit = 100  # int | Maximum number of returned items. (optional)
    offset = 0  # int | How many items should be returned ahead. (optional)

    try:
        api_response = api_instance.statistics_campaigns_get(limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling StatisticsApi->statistics_campaigns_get: %s\n" % e)
