# Add List

This example is aligned with the current SDK and can be run directly from `examples/functions/addList.py`.

```python
import ElasticEmail
from ElasticEmail.models.list_payload import ListPayload
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Add list
Example api call that creates a new contacts list.
Emails – An array of existing contact emails that should be added to this list. Leave empty for all contacts
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ListsApi(api_client)

    list_payload = ListPayload(
        ListName="Best contacts",
        AllowUnsubscribe=True,
        Emails=[
            "johnsmith@domain.com",
        ],
    )  # ListPayload |

    try:
        api_response = api_instance.lists_post(list_payload=list_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        if e.status == 400:
            print("List already exists. Skipping.")
        else:
            print("Exception when calling ListsApi->lists_post: %s\n" % e)
```

Run with:

```bash
py -3 addList.py
```
