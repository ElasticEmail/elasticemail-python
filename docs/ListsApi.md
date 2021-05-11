# ElasticEmail.ListsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lists_by_name_contacts_post**](ListsApi.md#lists_by_name_contacts_post) | **POST** /lists/{name}/contacts | Add Contacts to List
[**lists_by_name_contacts_remove_post**](ListsApi.md#lists_by_name_contacts_remove_post) | **POST** /lists/{name}/contacts/remove | Remove Contacts from List
[**lists_by_name_delete**](ListsApi.md#lists_by_name_delete) | **DELETE** /lists/{name} | Delete List
[**lists_by_name_get**](ListsApi.md#lists_by_name_get) | **GET** /lists/{name} | Load List
[**lists_by_name_put**](ListsApi.md#lists_by_name_put) | **PUT** /lists/{name} | Update List
[**lists_get**](ListsApi.md#lists_get) | **GET** /lists | Load Lists
[**lists_post**](ListsApi.md#lists_post) | **POST** /lists | Add List


# **lists_by_name_contacts_post**
> ContactsList lists_by_name_contacts_post(name, emails_payload)

Add Contacts to List

Add existing Contacts to specified list. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import lists_api
from ElasticEmail.model.emails_payload import EmailsPayload
from ElasticEmail.model.contacts_list import ContactsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.elasticemail.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)
    name = "My List 1" # str | Name of your list.
    emails_payload = EmailsPayload(
        rule="rule_example",
        emails=[
            "emails_example",
        ],
    ) # EmailsPayload | Provide either rule or a list of emails, not both.

    # example passing only required values which don't have defaults set
    try:
        # Add Contacts to List
        api_response = api_instance.lists_by_name_contacts_post(name, emails_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_contacts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your list. |
 **emails_payload** | [**EmailsPayload**](EmailsPayload.md)| Provide either rule or a list of emails, not both. |

### Return type

[**ContactsList**](ContactsList.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_by_name_contacts_remove_post**
> lists_by_name_contacts_remove_post(name, emails_payload)

Remove Contacts from List

Remove specified Contacts from your list. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import lists_api
from ElasticEmail.model.emails_payload import EmailsPayload
from pprint import pprint
# Defining the host is optional and defaults to https://api.elasticemail.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)
    name = "My List 1" # str | Name of your list.
    emails_payload = EmailsPayload(
        rule="rule_example",
        emails=[
            "emails_example",
        ],
    ) # EmailsPayload | Provide either rule or a list of emails, not both.

    # example passing only required values which don't have defaults set
    try:
        # Remove Contacts from List
        api_instance.lists_by_name_contacts_remove_post(name, emails_payload)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_contacts_remove_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your list. |
 **emails_payload** | [**EmailsPayload**](EmailsPayload.md)| Provide either rule or a list of emails, not both. |

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_by_name_delete**
> lists_by_name_delete(name)

Delete List

Deletes List and removes all the Contacts from it (does not delete Contacts). Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import lists_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.elasticemail.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)
    name = "My List 1" # str | Name of your list.

    # example passing only required values which don't have defaults set
    try:
        # Delete List
        api_instance.lists_by_name_delete(name)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your list. |

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_by_name_get**
> ContactsList lists_by_name_get(name)

Load List

Returns detailed information about specified list. Required Access Level: ViewContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import lists_api
from ElasticEmail.model.contacts_list import ContactsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.elasticemail.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)
    name = "My List 1" # str | Name of your list.

    # example passing only required values which don't have defaults set
    try:
        # Load List
        api_response = api_instance.lists_by_name_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your list. |

### Return type

[**ContactsList**](ContactsList.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_by_name_put**
> ContactsList lists_by_name_put(name, list_update_payload)

Update List

Update existing list. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import lists_api
from ElasticEmail.model.list_update_payload import ListUpdatePayload
from ElasticEmail.model.contacts_list import ContactsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.elasticemail.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)
    name = "My List 1" # str | Name of your list.
    list_update_payload = ListUpdatePayload(
        new_list_name="My List 2",
        allow_unsubscribe=False,
    ) # ListUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update List
        api_response = api_instance.lists_by_name_put(name, list_update_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_by_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your list. |
 **list_update_payload** | [**ListUpdatePayload**](ListUpdatePayload.md)|  |

### Return type

[**ContactsList**](ContactsList.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_get**
> [ContactsList] lists_get()

Load Lists

Returns all your existing lists. Required Access Level: ViewContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import lists_api
from ElasticEmail.model.contacts_list import ContactsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.elasticemail.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Load Lists
        api_response = api_instance.lists_get(limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[ContactsList]**](ContactsList.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_post**
> ContactsList lists_post(list_payload)

Add List

Add a new list. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import lists_api
from ElasticEmail.model.contacts_list import ContactsList
from ElasticEmail.model.list_payload import ListPayload
from pprint import pprint
# Defining the host is optional and defaults to https://api.elasticemail.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lists_api.ListsApi(api_client)
    list_payload = ListPayload(
        list_name="My List 1",
        allow_unsubscribe=False,
        emails=[
            "emails_example",
        ],
    ) # ListPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Add List
        api_response = api_instance.lists_post(list_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ListsApi->lists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_payload** | [**ListPayload**](ListPayload.md)|  |

### Return type

[**ContactsList**](ContactsList.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

