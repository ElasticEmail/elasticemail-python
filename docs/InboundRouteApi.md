# ElasticEmail.InboundRouteApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inboundroute_by_id_delete**](InboundRouteApi.md#inboundroute_by_id_delete) | **DELETE** /inboundroute/{id} | Delete Route
[**inboundroute_by_id_get**](InboundRouteApi.md#inboundroute_by_id_get) | **GET** /inboundroute/{id} | Get Route
[**inboundroute_by_id_put**](InboundRouteApi.md#inboundroute_by_id_put) | **PUT** /inboundroute/{id} | Update Route
[**inboundroute_get**](InboundRouteApi.md#inboundroute_get) | **GET** /inboundroute | Get Routes
[**inboundroute_order_put**](InboundRouteApi.md#inboundroute_order_put) | **PUT** /inboundroute/order | Update Sorting
[**inboundroute_post**](InboundRouteApi.md#inboundroute_post) | **POST** /inboundroute | Create Route


# **inboundroute_by_id_delete**
> inboundroute_by_id_delete(id)

Delete Route

Deletes the Inbound Route. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import inbound_route_api
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
    api_instance = inbound_route_api.InboundRouteApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Route
        api_instance.inboundroute_by_id_delete(id)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_by_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **inboundroute_by_id_get**
> InboundRoute inboundroute_by_id_get(id)

Get Route

Load an Inbound Route. Required Access Level: ViewSettings

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import inbound_route_api
from ElasticEmail.model.inbound_route import InboundRoute
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
    api_instance = inbound_route_api.InboundRouteApi(api_client)
    id = "123456" # str | ID number of your attachment

    # example passing only required values which don't have defaults set
    try:
        # Get Route
        api_response = api_instance.inboundroute_by_id_get(id)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_by_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID number of your attachment |

### Return type

[**InboundRoute**](InboundRoute.md)

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

# **inboundroute_by_id_put**
> InboundRoute inboundroute_by_id_put(id, inbound_payload)

Update Route

Update the Inbound Route. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import inbound_route_api
from ElasticEmail.model.inbound_payload import InboundPayload
from ElasticEmail.model.inbound_route import InboundRoute
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
    api_instance = inbound_route_api.InboundRouteApi(api_client)
    id = "id_example" # str | 
    inbound_payload = InboundPayload(
        filter="filter_example",
        name="name_example",
        filter_type=,
        action_type=,
        email_address="email_address_example",
        http_address="http_address_example",
    ) # InboundPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update Route
        api_response = api_instance.inboundroute_by_id_put(id, inbound_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_by_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **inbound_payload** | [**InboundPayload**](InboundPayload.md)|  |

### Return type

[**InboundRoute**](InboundRoute.md)

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

# **inboundroute_get**
> [InboundRoute] inboundroute_get()

Get Routes

Get all your Inbound Routes. Required Access Level: ViewSettings

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import inbound_route_api
from ElasticEmail.model.inbound_route import InboundRoute
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
    api_instance = inbound_route_api.InboundRouteApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Routes
        api_response = api_instance.inboundroute_get()
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[InboundRoute]**](InboundRoute.md)

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

# **inboundroute_order_put**
> [InboundRoute] inboundroute_order_put(sort_order_item)

Update Sorting

Required Access Level: ViewSettings

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import inbound_route_api
from ElasticEmail.model.sort_order_item import SortOrderItem
from ElasticEmail.model.inbound_route import InboundRoute
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
    api_instance = inbound_route_api.InboundRouteApi(api_client)
    sort_order_item = [
        SortOrderItem(
            public_inbound_id="public_inbound_id_example",
            sort_order=1,
        ),
    ] # [SortOrderItem] | Change the ordering of inbound routes for when matching the inbound

    # example passing only required values which don't have defaults set
    try:
        # Update Sorting
        api_response = api_instance.inboundroute_order_put(sort_order_item)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_order_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_order_item** | [**[SortOrderItem]**](SortOrderItem.md)| Change the ordering of inbound routes for when matching the inbound |

### Return type

[**[InboundRoute]**](InboundRoute.md)

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

# **inboundroute_post**
> InboundRoute inboundroute_post(inbound_payload)

Create Route

Create new Inbound Route. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import inbound_route_api
from ElasticEmail.model.inbound_payload import InboundPayload
from ElasticEmail.model.inbound_route import InboundRoute
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
    api_instance = inbound_route_api.InboundRouteApi(api_client)
    inbound_payload = InboundPayload(
        filter="filter_example",
        name="name_example",
        filter_type=,
        action_type=,
        email_address="email_address_example",
        http_address="http_address_example",
    ) # InboundPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create Route
        api_response = api_instance.inboundroute_post(inbound_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_payload** | [**InboundPayload**](InboundPayload.md)|  |

### Return type

[**InboundRoute**](InboundRoute.md)

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

