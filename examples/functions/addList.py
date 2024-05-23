import ElasticEmail
from ElasticEmail.apis.tags import lists_api
from ElasticEmail.model.list_payload import ListPayload
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Add list
Example api call that creates a new contacts list.
Emails – An array of existing contact emails that should be added to this list. Leave empty for all contacts
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)

    list_payload = ListPayload(
        ListName="Best contacts",
        AllowUnsubscribe=True,
        Emails=[
            "johnsmith@domain.com",
        ],
    )  # ListPayload |

    try:
        api_response = api_instance.lists_post(body = list_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_post: %s\n" % e)
