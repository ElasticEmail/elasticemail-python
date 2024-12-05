# ElasticEmail.FilesApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_by_name_delete**](FilesApi.md#files_by_name_delete) | **DELETE** /files/{name} | Delete File
[**files_by_name_get**](FilesApi.md#files_by_name_get) | **GET** /files/{name} | Download File
[**files_by_name_info_get**](FilesApi.md#files_by_name_info_get) | **GET** /files/{name}/info | Load File Details
[**files_get**](FilesApi.md#files_get) | **GET** /files | List Files
[**files_post**](FilesApi.md#files_post) | **POST** /files | Upload File


# **files_by_name_delete**
> files_by_name_delete(name)

Delete File

Permanently deletes the file from your Account. Required Access Level: ModifyFiles

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
    api_instance = ElasticEmail.FilesApi(api_client)
    name = 'filename.txt' # str | Name of your file including extension.

    try:
        # Delete File
        api_instance.files_by_name_delete(name)
    except Exception as e:
        print("Exception when calling FilesApi->files_by_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your file including extension. | 

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

# **files_by_name_get**
> bytearray files_by_name_get(name)

Download File

Gets content of the specified File. Required Access Level: ViewFiles

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
    api_instance = ElasticEmail.FilesApi(api_client)
    name = 'filename.txt' # str | Name of your file including extension.

    try:
        # Download File
        api_response = api_instance.files_by_name_get(name)
        print("The response of FilesApi->files_by_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_by_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your file including extension. | 

### Return type

**bytearray**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_by_name_info_get**
> FileInfo files_by_name_info_get(name)

Load File Details

Returns the specified File's details. Required Access Level: ViewFiles

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.file_info import FileInfo
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
    api_instance = ElasticEmail.FilesApi(api_client)
    name = 'filename.txt' # str | Name of your file including extension.

    try:
        # Load File Details
        api_response = api_instance.files_by_name_info_get(name)
        print("The response of FilesApi->files_by_name_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_by_name_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your file including extension. | 

### Return type

[**FileInfo**](FileInfo.md)

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

# **files_get**
> List[FileInfo] files_get(limit=limit, offset=offset)

List Files

Returns a list of all your available files. Required Access Level: ViewFiles

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.file_info import FileInfo
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
    api_instance = ElasticEmail.FilesApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # List Files
        api_response = api_instance.files_get(limit=limit, offset=offset)
        print("The response of FilesApi->files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[FileInfo]**](FileInfo.md)

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

# **files_post**
> FileInfo files_post(file_payload, expires_after_days=expires_after_days)

Upload File

Uploads selected file to the server. Required Access Level: ModifyFiles

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.file_info import FileInfo
from ElasticEmail.models.file_payload import FilePayload
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
    api_instance = ElasticEmail.FilesApi(api_client)
    file_payload = ElasticEmail.FilePayload() # FilePayload | 
    expires_after_days = 56 # int | After how many days should the file be deleted. (optional)

    try:
        # Upload File
        api_response = api_instance.files_post(file_payload, expires_after_days=expires_after_days)
        print("The response of FilesApi->files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_payload** | [**FilePayload**](FilePayload.md)|  | 
 **expires_after_days** | **int**| After how many days should the file be deleted. | [optional] 

### Return type

[**FileInfo**](FileInfo.md)

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

