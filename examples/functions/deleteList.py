import ElasticEmail
from ElasticEmail.apis.tags import lists_api

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Delete list
Example api call that loads given contacts list.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)

    name = "Best contacts"  # str | Name of your list.

    try:
        api_instance.lists_by_name_delete({'name': name})
        print("List deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_delete: %s\n" % e)
