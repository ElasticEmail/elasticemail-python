# ElasticEmail.EventsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_by_transactionid_get**](EventsApi.md#events_by_transactionid_get) | **GET** /events/{transactionid} | Load Email Events
[**events_channels_by_name_export_post**](EventsApi.md#events_channels_by_name_export_post) | **POST** /events/channels/{name}/export | Export Channel Events
[**events_channels_by_name_get**](EventsApi.md#events_channels_by_name_get) | **GET** /events/channels/{name} | Load Channel Events
[**events_channels_export_by_id_status_get**](EventsApi.md#events_channels_export_by_id_status_get) | **GET** /events/channels/export/{id}/status | Check Channel Export Status
[**events_export_by_id_status_get**](EventsApi.md#events_export_by_id_status_get) | **GET** /events/export/{id}/status | Check Export Status
[**events_export_post**](EventsApi.md#events_export_post) | **POST** /events/export | Export Events
[**events_get**](EventsApi.md#events_get) | **GET** /events | Load Events


# **events_by_transactionid_get**
> [RecipientEvent] events_by_transactionid_get(transactionid)

Load Email Events

Returns a log of delivery events for the specific transaction ID. Required Access Level: ViewReports

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import events_api
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
    transactionid = "TransactionID" # str | ID number of transaction
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Starting date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Ending date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    order_by = EventsOrderBy("DateDescending") # EventsOrderBy |  (optional)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Load Email Events
        api_response = api_instance.events_by_transactionid_get(transactionid)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_by_transactionid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Load Email Events
        api_response = api_instance.events_by_transactionid_get(transactionid, _from=_from, to=to, order_by=order_by, limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_by_transactionid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionid** | **str**| ID number of transaction |
 **_from** | **datetime, none_type**| Starting date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **to** | **datetime, none_type**| Ending date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **order_by** | **EventsOrderBy**|  | [optional]
 **limit** | **int**| Maximum number of returned items. | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[RecipientEvent]**](RecipientEvent.md)

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

# **events_channels_by_name_export_post**
> ExportLink events_channels_by_name_export_post(name)

Export Channel Events

Export delivery events log information to the specified file format. Required Access Level: Export

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import events_api
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
    name = "Channel01" # str | Name of selected channel.
    event_types = [
        EventType("Submission"),
    ] # [EventType] | Types of Events to return (optional)
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Starting date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Ending date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    file_format = ExportFileFormats("Csv") # ExportFileFormats | Format of the exported file (optional)
    compression_format = CompressionFormat("None") # CompressionFormat | FileResponse compression format. None or Zip. (optional)
    file_name = "filename.txt" # str | Name of your file including extension. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export Channel Events
        api_response = api_instance.events_channels_by_name_export_post(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_by_name_export_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Channel Events
        api_response = api_instance.events_channels_by_name_export_post(name, event_types=event_types, _from=_from, to=to, file_format=file_format, compression_format=compression_format, file_name=file_name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_by_name_export_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of selected channel. |
 **event_types** | [**[EventType]**](EventType.md)| Types of Events to return | [optional]
 **_from** | **datetime, none_type**| Starting date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **to** | **datetime, none_type**| Ending date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **file_format** | **ExportFileFormats**| Format of the exported file | [optional]
 **compression_format** | **CompressionFormat**| FileResponse compression format. None or Zip. | [optional]
 **file_name** | **str**| Name of your file including extension. | [optional]

### Return type

[**ExportLink**](ExportLink.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_channels_by_name_get**
> [RecipientEvent] events_channels_by_name_get(name)

Load Channel Events

Returns a log of delivery events filtered by specified parameters. Required Access Level: ViewReports

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import events_api
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
    name = "Channel01" # str | Name of selected channel.
    event_types = [
        EventType("Submission"),
    ] # [EventType] | Types of Events to return (optional)
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Starting date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Ending date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    order_by = EventsOrderBy("DateDescending") # EventsOrderBy |  (optional)
    limit = 1 # int | How many items to load. Maximum for this request is 1000 items (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Load Channel Events
        api_response = api_instance.events_channels_by_name_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_by_name_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Load Channel Events
        api_response = api_instance.events_channels_by_name_get(name, event_types=event_types, _from=_from, to=to, order_by=order_by, limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_by_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of selected channel. |
 **event_types** | [**[EventType]**](EventType.md)| Types of Events to return | [optional]
 **_from** | **datetime, none_type**| Starting date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **to** | **datetime, none_type**| Ending date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **order_by** | **EventsOrderBy**|  | [optional]
 **limit** | **int**| How many items to load. Maximum for this request is 1000 items | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[RecipientEvent]**](RecipientEvent.md)

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

# **events_channels_export_by_id_status_get**
> ExportStatus events_channels_export_by_id_status_get(id)

Check Channel Export Status

Check the current status of the channel export. Required Access Level: Export

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import events_api
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
    id = "E33EBA7A-C20D-4D3D-8F2F-5EEF42F58E6F" # str | ID of the exported file

    # example passing only required values which don't have defaults set
    try:
        # Check Channel Export Status
        api_response = api_instance.events_channels_export_by_id_status_get(id)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_channels_export_by_id_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the exported file |

### Return type

[**ExportStatus**](ExportStatus.md)

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

# **events_export_by_id_status_get**
> ExportStatus events_export_by_id_status_get(id)

Check Export Status

Check the current status of the export. Required Access Level: Export

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import events_api
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
    id = "E33EBA7A-C20D-4D3D-8F2F-5EEF42F58E6F" # str | ID of the exported file

    # example passing only required values which don't have defaults set
    try:
        # Check Export Status
        api_response = api_instance.events_export_by_id_status_get(id)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_export_by_id_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the exported file |

### Return type

[**ExportStatus**](ExportStatus.md)

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

# **events_export_post**
> ExportLink events_export_post()

Export Events

Export delivery events log information to the specified file format. Required Access Level: Export

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import events_api
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
    event_types = [
        EventType("Submission"),
    ] # [EventType] | Types of Events to return (optional)
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Starting date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Ending date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    file_format = ExportFileFormats("Csv") # ExportFileFormats | Format of the exported file (optional)
    compression_format = CompressionFormat("None") # CompressionFormat | FileResponse compression format. None or Zip. (optional)
    file_name = "filename.txt" # str | Name of your file including extension. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Events
        api_response = api_instance.events_export_post(event_types=event_types, _from=_from, to=to, file_format=file_format, compression_format=compression_format, file_name=file_name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_export_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_types** | [**[EventType]**](EventType.md)| Types of Events to return | [optional]
 **_from** | **datetime, none_type**| Starting date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **to** | **datetime, none_type**| Ending date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **file_format** | **ExportFileFormats**| Format of the exported file | [optional]
 **compression_format** | **CompressionFormat**| FileResponse compression format. None or Zip. | [optional]
 **file_name** | **str**| Name of your file including extension. | [optional]

### Return type

[**ExportLink**](ExportLink.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get**
> [RecipientEvent] events_get()

Load Events

Returns a log of delivery events filtered by specified parameters. Required Access Level: ViewReports

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import events_api
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
    event_types = [
        EventType("Submission"),
    ] # [EventType] | Types of Events to return (optional)
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Starting date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | Ending date for search in YYYY-MM-DDThh:mm:ss format. (optional)
    order_by = EventsOrderBy("DateDescending") # EventsOrderBy |  (optional)
    limit = 1 # int | How many items to load. Maximum for this request is 1000 items (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Load Events
        api_response = api_instance.events_get(event_types=event_types, _from=_from, to=to, order_by=order_by, limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EventsApi->events_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_types** | [**[EventType]**](EventType.md)| Types of Events to return | [optional]
 **_from** | **datetime, none_type**| Starting date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **to** | **datetime, none_type**| Ending date for search in YYYY-MM-DDThh:mm:ss format. | [optional]
 **order_by** | **EventsOrderBy**|  | [optional]
 **limit** | **int**| How many items to load. Maximum for this request is 1000 items | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[RecipientEvent]**](RecipientEvent.md)

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

