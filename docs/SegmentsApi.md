# ElasticEmail.SegmentsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**segments_by_name_delete**](SegmentsApi.md#segments_by_name_delete) | **DELETE** /segments/{name} | Delete Segment
[**segments_by_name_get**](SegmentsApi.md#segments_by_name_get) | **GET** /segments/{name} | Load Segment
[**segments_by_name_put**](SegmentsApi.md#segments_by_name_put) | **PUT** /segments/{name} | Update Segment
[**segments_get**](SegmentsApi.md#segments_get) | **GET** /segments | Load Segments
[**segments_post**](SegmentsApi.md#segments_post) | **POST** /segments | Add Segment


# **segments_by_name_delete**
> segments_by_name_delete(name)

Delete Segment

Delete an existing segment. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.rest import ApiException
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
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.SegmentsApi(api_client)
    name = 'My Segment 1' # str | Name of your segment.

    try:
        # Delete Segment
        api_instance.segments_by_name_delete(name)
    except Exception as e:
        print("Exception when calling SegmentsApi->segments_by_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your segment. | 

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

# **segments_by_name_get**
> Segment segments_by_name_get(name)

Load Segment

Returns details for the specified segment. Required Access Level: ViewContacts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.segment import Segment
from ElasticEmail.rest import ApiException
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
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.SegmentsApi(api_client)
    name = 'name_example' # str | Name of the segment you want to load. Will load all contacts if the 'All Contacts' name has been provided

    try:
        # Load Segment
        api_response = api_instance.segments_by_name_get(name)
        print("The response of SegmentsApi->segments_by_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->segments_by_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the segment you want to load. Will load all contacts if the &#39;All Contacts&#39; name has been provided | 

### Return type

[**Segment**](Segment.md)

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

# **segments_by_name_put**
> Segment segments_by_name_put(name, segment_payload)

Update Segment

Rename or change RULE for your segment. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.segment import Segment
from ElasticEmail.models.segment_payload import SegmentPayload
from ElasticEmail.rest import ApiException
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
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.SegmentsApi(api_client)
    name = 'My Segment 1' # str | Name of your segment.
    segment_payload = ElasticEmail.SegmentPayload() # SegmentPayload | 

    try:
        # Update Segment
        api_response = api_instance.segments_by_name_put(name, segment_payload)
        print("The response of SegmentsApi->segments_by_name_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->segments_by_name_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your segment. | 
 **segment_payload** | [**SegmentPayload**](SegmentPayload.md)|  | 

### Return type

[**Segment**](Segment.md)

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

# **segments_get**
> List[Segment] segments_get(limit=limit, offset=offset)

Load Segments

Returns a list of all your available Segments. Required Access Level: ViewContacts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.segment import Segment
from ElasticEmail.rest import ApiException
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
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.SegmentsApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Load Segments
        api_response = api_instance.segments_get(limit=limit, offset=offset)
        print("The response of SegmentsApi->segments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->segments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[Segment]**](Segment.md)

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

# **segments_post**
> Segment segments_post(segment_payload)

Add Segment

Add a new segment, based on specified RULE. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.segment import Segment
from ElasticEmail.models.segment_payload import SegmentPayload
from ElasticEmail.rest import ApiException
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
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.SegmentsApi(api_client)
    segment_payload = ElasticEmail.SegmentPayload() # SegmentPayload | 

    try:
        # Add Segment
        api_response = api_instance.segments_post(segment_payload)
        print("The response of SegmentsApi->segments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->segments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_payload** | [**SegmentPayload**](SegmentPayload.md)|  | 

### Return type

[**Segment**](Segment.md)

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

