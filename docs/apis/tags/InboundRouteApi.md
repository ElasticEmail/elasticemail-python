<a name="__pageTop"></a>
# ElasticEmail.apis.tags.inbound_route_api.InboundRouteApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inboundroute_by_id_delete**](#inboundroute_by_id_delete) | **delete** /inboundroute/{id} | Delete Route
[**inboundroute_by_id_get**](#inboundroute_by_id_get) | **get** /inboundroute/{id} | Get Route
[**inboundroute_by_id_put**](#inboundroute_by_id_put) | **put** /inboundroute/{id} | Update Route
[**inboundroute_get**](#inboundroute_get) | **get** /inboundroute | Get Routes
[**inboundroute_order_put**](#inboundroute_order_put) | **put** /inboundroute/order | Update Sorting
[**inboundroute_post**](#inboundroute_post) | **post** /inboundroute | Create Route

# **inboundroute_by_id_delete**
<a name="inboundroute_by_id_delete"></a>
> inboundroute_by_id_delete(id)

Delete Route

Deletes the Inbound Route. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import inbound_route_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete Route
        api_response = api_instance.inboundroute_by_id_delete(
            path_params=path_params,
        )
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_by_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#inboundroute_by_id_delete.ApiResponseFor200) | OK

#### inboundroute_by_id_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **inboundroute_by_id_get**
<a name="inboundroute_by_id_get"></a>
> InboundRoute inboundroute_by_id_get(id)

Get Route

Load an Inbound Route. Required Access Level: ViewSettings

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import inbound_route_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123456",
    }
    try:
        # Get Route
        api_response = api_instance.inboundroute_by_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_by_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#inboundroute_by_id_get.ApiResponseFor200) | OK

#### inboundroute_by_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InboundRoute**](../../models/InboundRoute.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **inboundroute_by_id_put**
<a name="inboundroute_by_id_put"></a>
> InboundRoute inboundroute_by_id_put(idinbound_payload)

Update Route

Update the Inbound Route. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import inbound_route_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = InboundPayload(
        filter="filter_example",
        name="name_example",
        filter_type=InboundRouteFilterType("EmailAddress"),
        action_type=InboundRouteActionType("ForwardToEmail"),
        email_address="email_address_example",
        http_address="http_address_example",
    )
    try:
        # Update Route
        api_response = api_instance.inboundroute_by_id_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_by_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InboundPayload**](../../models/InboundPayload.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#inboundroute_by_id_put.ApiResponseFor200) | OK

#### inboundroute_by_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InboundRoute**](../../models/InboundRoute.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **inboundroute_get**
<a name="inboundroute_get"></a>
> [InboundRoute] inboundroute_get()

Get Routes

Get all your Inbound Routes. Required Access Level: ViewSettings

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import inbound_route_api
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#inboundroute_get.ApiResponseFor200) | OK

#### inboundroute_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InboundRoute**]({{complexTypePrefix}}InboundRoute.md) | [**InboundRoute**]({{complexTypePrefix}}InboundRoute.md) | [**InboundRoute**]({{complexTypePrefix}}InboundRoute.md) |  | 

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **inboundroute_order_put**
<a name="inboundroute_order_put"></a>
> [InboundRoute] inboundroute_order_put(sort_order_item)

Update Sorting

Required Access Level: ViewSettings

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import inbound_route_api
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

    # example passing only required values which don't have defaults set
    body = [
        SortOrderItem(
            public_inbound_id="public_inbound_id_example",
            sort_order=1,
        )
    ]
    try:
        # Update Sorting
        api_response = api_instance.inboundroute_order_put(
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_order_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SortOrderItem**]({{complexTypePrefix}}SortOrderItem.md) | [**SortOrderItem**]({{complexTypePrefix}}SortOrderItem.md) | [**SortOrderItem**]({{complexTypePrefix}}SortOrderItem.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#inboundroute_order_put.ApiResponseFor200) | OK

#### inboundroute_order_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InboundRoute**]({{complexTypePrefix}}InboundRoute.md) | [**InboundRoute**]({{complexTypePrefix}}InboundRoute.md) | [**InboundRoute**]({{complexTypePrefix}}InboundRoute.md) |  | 

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **inboundroute_post**
<a name="inboundroute_post"></a>
> InboundRoute inboundroute_post(inbound_payload)

Create Route

Create new Inbound Route. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import inbound_route_api
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

    # example passing only required values which don't have defaults set
    body = InboundPayload(
        filter="filter_example",
        name="name_example",
        filter_type=InboundRouteFilterType("EmailAddress"),
        action_type=InboundRouteActionType("ForwardToEmail"),
        email_address="email_address_example",
        http_address="http_address_example",
    )
    try:
        # Create Route
        api_response = api_instance.inboundroute_post(
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling InboundRouteApi->inboundroute_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InboundPayload**](../../models/InboundPayload.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#inboundroute_post.ApiResponseFor200) | OK

#### inboundroute_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InboundRoute**](../../models/InboundRoute.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

