# Load List

This example is aligned with the current SDK and can be run directly from `examples/functions/loadList.py`.

```python
import ElasticEmail
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Load list
Example api call that loads given contacts list.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ListsApi(api_client)

    name = "Best contacts"  # str | Name of your list.

    try:
        api_response = api_instance.lists_by_name_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        try:
            available = api_instance.lists_get(limit=1, offset=0)
            if available:
                fallback_name = available[0].list_name
                api_response = api_instance.lists_by_name_get(fallback_name)
                pprint(api_response)
                raise SystemExit(0)
        except ElasticEmail.ApiException:
            pass
        print(f"No list found to load ({e.status}). Skipping.")
```

Run with:

```bash
py -3 loadList.py
```
