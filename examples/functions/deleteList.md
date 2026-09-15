# Delete List

This example is aligned with the current SDK and can be run directly from `examples/functions/deleteList.py`.

```python
import ElasticEmail

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Delete list
Example api call that loads given contacts list.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ListsApi(api_client)

    name = "Best contacts"  # str | Name of your list.

    try:
        api_instance.lists_by_name_delete(name)
        print("List deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_delete: %s\n" % e)
```

Run with:

```bash
py -3 deleteList.py
```
