<a name="__pageTop"></a>
# ElasticEmail.apis.tags.events_api.EventsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_by_transactionid_get**](#events_by_transactionid_get) | **get** /events/{transactionid} | Load Email Events
[**events_channels_by_name_export_post**](#events_channels_by_name_export_post) | **post** /events/channels/{name}/export | Export Channel Events
[**events_channels_by_name_get**](#events_channels_by_name_get) | **get** /events/channels/{name} | Load Channel Events
[**events_channels_export_by_id_status_get**](#events_channels_export_by_id_status_get) | **get** /events/channels/export/{id}/status | Check Channel Export Status
[**events_export_by_id_status_get**](#events_export_by_id_status_get) | **get** /events/export/{id}/status | Check Export Status
[**events_export_post**](#events_export_post) | **post** /events/export | Export Events
[**events_get**](#events_get) | **get** /events | Load Events

# **events_by_transactionid_get**
<a name="events_by_transactionid_get"></a>
> [RecipientEvent] events_by_transactionid_get(transactionid)

Load Email Events

Returns a log of delivery events for the specific transaction ID. Required Access Level: ViewReports

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import events_api
from ElasticEmail.model.recipient_event import RecipientEvent
from ElasticEmail.model.events_order_by import EventsOrderBy
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
    api_instance = events_api.EventsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transactionid': "TransactionID",
    }
    query_params = {
    }
    try:
        # Load Email Events
        api_response = api_instance.events_by_transactionid_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_by_transactionid_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transactionid': "TransactionID",
    }
    query_params = {
        'from': "1970-01-01T00:00:00.00Z",
        'to': "1970-01-01T00:00:00.00Z",
        'orderBy': EventsOrderBy("DateDescending"),
        'limit': 100,
        'offset': 20,
    }
    try:
        # Load Email Events
        api_response = api_instance.events_by_transactionid_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_by_transactionid_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
from | ModelFromSchema | | optional
to | ToSchema | | optional
orderBy | OrderBySchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# ModelFromSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# ToSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# OrderBySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**EventsOrderBy**](../../models/EventsOrderBy.md) |  | 


# LimitSchema

integer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | integer | value must be a 32 bit integer

# OffsetSchema

integer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | integer | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transactionid | TransactionidSchema | | 

# TransactionidSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#events_by_transactionid_get.ApiResponseFor200) | OK

#### events_by_transactionid_get.ApiResponseFor200
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
[**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) | [**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) | [**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) |  | 

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **events_channels_by_name_export_post**
<a name="events_channels_by_name_export_post"></a>
> ExportLink events_channels_by_name_export_post(name)

Export Channel Events

Export delivery events log information to the specified file format. Required Access Level: Export

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import events_api
from ElasticEmail.model.export_file_formats import ExportFileFormats
from ElasticEmail.model.compression_format import CompressionFormat
from ElasticEmail.model.export_link import ExportLink
from ElasticEmail.model.event_type import EventType
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
    api_instance = events_api.EventsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "Channel01",
    }
    query_params = {
    }
    try:
        # Export Channel Events
        api_response = api_instance.events_channels_by_name_export_post(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_by_name_export_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "Channel01",
    }
    query_params = {
        'eventTypes': [
        EventType("Submission")
    ],
        'from': "1970-01-01T00:00:00.00Z",
        'to': "1970-01-01T00:00:00.00Z",
        'fileFormat': ExportFileFormats("Csv"),
        'compressionFormat': CompressionFormat("None"),
        'fileName': "filename.txt",
    }
    try:
        # Export Channel Events
        api_response = api_instance.events_channels_by_name_export_post(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_by_name_export_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
eventTypes | EventTypesSchema | | optional
from | ModelFromSchema | | optional
to | ToSchema | | optional
fileFormat | FileFormatSchema | | optional
compressionFormat | CompressionFormatSchema | | optional
fileName | FileNameSchema | | optional


# EventTypesSchema

array

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | array | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EventType**]({{complexTypePrefix}}EventType.md) | [**EventType**]({{complexTypePrefix}}EventType.md) | [**EventType**]({{complexTypePrefix}}EventType.md) |  | 

# ModelFromSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# ToSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# FileFormatSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFormats**](../../models/ExportFileFormats.md) |  | 


# CompressionFormatSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**CompressionFormat**](../../models/CompressionFormat.md) |  | 


# FileNameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#events_channels_by_name_export_post.ApiResponseFor202) | Accepted

#### events_channels_by_name_export_post.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportLink**](../../models/ExportLink.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **events_channels_by_name_get**
<a name="events_channels_by_name_get"></a>
> [RecipientEvent] events_channels_by_name_get(name)

Load Channel Events

Returns a log of delivery events filtered by specified parameters. Required Access Level: ViewReports

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import events_api
from ElasticEmail.model.recipient_event import RecipientEvent
from ElasticEmail.model.events_order_by import EventsOrderBy
from ElasticEmail.model.event_type import EventType
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
    api_instance = events_api.EventsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "Channel01",
    }
    query_params = {
    }
    try:
        # Load Channel Events
        api_response = api_instance.events_channels_by_name_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_by_name_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "Channel01",
    }
    query_params = {
        'eventTypes': [
        EventType("Submission")
    ],
        'from': "1970-01-01T00:00:00.00Z",
        'to': "1970-01-01T00:00:00.00Z",
        'orderBy': EventsOrderBy("DateDescending"),
        'limit': 1,
        'offset': 20,
    }
    try:
        # Load Channel Events
        api_response = api_instance.events_channels_by_name_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_by_name_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
eventTypes | EventTypesSchema | | optional
from | ModelFromSchema | | optional
to | ToSchema | | optional
orderBy | OrderBySchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# EventTypesSchema

array

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | array | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EventType**]({{complexTypePrefix}}EventType.md) | [**EventType**]({{complexTypePrefix}}EventType.md) | [**EventType**]({{complexTypePrefix}}EventType.md) |  | 

# ModelFromSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# ToSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# OrderBySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**EventsOrderBy**](../../models/EventsOrderBy.md) |  | 


# LimitSchema

integer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | integer | value must be a 32 bit integer

# OffsetSchema

integer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | integer | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#events_channels_by_name_get.ApiResponseFor200) | OK

#### events_channels_by_name_get.ApiResponseFor200
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
[**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) | [**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) | [**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) |  | 

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **events_channels_export_by_id_status_get**
<a name="events_channels_export_by_id_status_get"></a>
> ExportStatus events_channels_export_by_id_status_get(id)

Check Channel Export Status

Check the current status of the channel export. Required Access Level: Export

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import events_api
from ElasticEmail.model.export_status import ExportStatus
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
    api_instance = events_api.EventsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "E33EBA7A-C20D-4D3D-8F2F-5EEF42F58E6F",
    }
    try:
        # Check Channel Export Status
        api_response = api_instance.events_channels_export_by_id_status_get(
            path_params=path_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_export_by_id_status_get: %s\n" % e)
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
200 | [ApiResponseFor200](#events_channels_export_by_id_status_get.ApiResponseFor200) | OK

#### events_channels_export_by_id_status_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportStatus**](../../models/ExportStatus.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **events_export_by_id_status_get**
<a name="events_export_by_id_status_get"></a>
> ExportStatus events_export_by_id_status_get(id)

Check Export Status

Check the current status of the export. Required Access Level: Export

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import events_api
from ElasticEmail.model.export_status import ExportStatus
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
    api_instance = events_api.EventsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "E33EBA7A-C20D-4D3D-8F2F-5EEF42F58E6F",
    }
    try:
        # Check Export Status
        api_response = api_instance.events_export_by_id_status_get(
            path_params=path_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_export_by_id_status_get: %s\n" % e)
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
200 | [ApiResponseFor200](#events_export_by_id_status_get.ApiResponseFor200) | OK

#### events_export_by_id_status_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportStatus**](../../models/ExportStatus.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **events_export_post**
<a name="events_export_post"></a>
> ExportLink events_export_post()

Export Events

Export delivery events log information to the specified file format. Required Access Level: Export

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import events_api
from ElasticEmail.model.export_file_formats import ExportFileFormats
from ElasticEmail.model.compression_format import CompressionFormat
from ElasticEmail.model.export_link import ExportLink
from ElasticEmail.model.event_type import EventType
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
    api_instance = events_api.EventsApi(api_client)

    # example passing only optional values
    query_params = {
        'eventTypes': [
        EventType("Submission")
    ],
        'from': "1970-01-01T00:00:00.00Z",
        'to': "1970-01-01T00:00:00.00Z",
        'fileFormat': ExportFileFormats("Csv"),
        'compressionFormat': CompressionFormat("None"),
        'fileName': "filename.txt",
    }
    try:
        # Export Events
        api_response = api_instance.events_export_post(
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_export_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
eventTypes | EventTypesSchema | | optional
from | ModelFromSchema | | optional
to | ToSchema | | optional
fileFormat | FileFormatSchema | | optional
compressionFormat | CompressionFormatSchema | | optional
fileName | FileNameSchema | | optional


# EventTypesSchema

array

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | array | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EventType**]({{complexTypePrefix}}EventType.md) | [**EventType**]({{complexTypePrefix}}EventType.md) | [**EventType**]({{complexTypePrefix}}EventType.md) |  | 

# ModelFromSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# ToSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# FileFormatSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFormats**](../../models/ExportFileFormats.md) |  | 


# CompressionFormatSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**CompressionFormat**](../../models/CompressionFormat.md) |  | 


# FileNameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#events_export_post.ApiResponseFor202) | Accepted

#### events_export_post.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportLink**](../../models/ExportLink.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **events_get**
<a name="events_get"></a>
> [RecipientEvent] events_get()

Load Events

Returns a log of delivery events filtered by specified parameters. Required Access Level: ViewReports

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import events_api
from ElasticEmail.model.recipient_event import RecipientEvent
from ElasticEmail.model.events_order_by import EventsOrderBy
from ElasticEmail.model.event_type import EventType
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
    api_instance = events_api.EventsApi(api_client)

    # example passing only optional values
    query_params = {
        'eventTypes': [
        EventType("Submission")
    ],
        'from': "1970-01-01T00:00:00.00Z",
        'to': "1970-01-01T00:00:00.00Z",
        'orderBy': EventsOrderBy("DateDescending"),
        'limit': 1,
        'offset': 20,
    }
    try:
        # Load Events
        api_response = api_instance.events_get(
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
eventTypes | EventTypesSchema | | optional
from | ModelFromSchema | | optional
to | ToSchema | | optional
orderBy | OrderBySchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# EventTypesSchema

array

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | array | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EventType**]({{complexTypePrefix}}EventType.md) | [**EventType**]({{complexTypePrefix}}EventType.md) | [**EventType**]({{complexTypePrefix}}EventType.md) |  | 

# ModelFromSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# ToSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | string | value must conform to RFC-3339 date-time

# OrderBySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**EventsOrderBy**](../../models/EventsOrderBy.md) |  | 


# LimitSchema

integer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | integer | value must be a 32 bit integer

# OffsetSchema

integer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | integer | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#events_get.ApiResponseFor200) | OK

#### events_get.ApiResponseFor200
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
[**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) | [**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) | [**RecipientEvent**]({{complexTypePrefix}}RecipientEvent.md) |  | 

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

