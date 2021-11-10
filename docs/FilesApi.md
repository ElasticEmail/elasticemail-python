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
import time
import ElasticEmail
from ElasticEmail.api import files_api
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
    api_instance = files_api.FilesApi(api_client)
    name = "filename.txt" # str | Name of your file including extension.

    # example passing only required values which don't have defaults set
    try:
        # Delete File
        api_instance.files_by_name_delete(name)
    except ElasticEmail.ApiException as e:
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
> file_type files_by_name_get(name)

Download File

Gets content of the specified File. Required Access Level: ViewFiles

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import files_api
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
    api_instance = files_api.FilesApi(api_client)
    name = "filename.txt" # str | Name of your file including extension.

    # example passing only required values which don't have defaults set
    try:
        # Download File
        api_response = api_instance.files_by_name_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling FilesApi->files_by_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your file including extension. |

### Return type

**file_type**

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
import time
import ElasticEmail
from ElasticEmail.api import files_api
from ElasticEmail.model.file_info import FileInfo
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
    api_instance = files_api.FilesApi(api_client)
    name = "filename.txt" # str | Name of your file including extension.

    # example passing only required values which don't have defaults set
    try:
        # Load File Details
        api_response = api_instance.files_by_name_info_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
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
> [FileInfo] files_get()

List Files

Returns a list of all your available files. Required Access Level: ViewFiles

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import files_api
from ElasticEmail.model.file_info import FileInfo
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
    api_instance = files_api.FilesApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Files
        api_response = api_instance.files_get(limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling FilesApi->files_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[FileInfo]**](FileInfo.md)

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
> FileInfo files_post(file_payload)

Upload File

Uploads selected file to the server. Required Access Level: ModifyFiles

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import files_api
from ElasticEmail.model.file_info import FileInfo
from ElasticEmail.model.file_payload import FilePayload
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
    api_instance = files_api.FilesApi(api_client)
    file_payload = FilePayload(
        binary_content='YQ==',
        name="attachment.txt",
        content_type="content_type_example",
    ) # FilePayload | 
    expires_after_days = 1 # int, none_type | After how many days should the file be deleted. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload File
        api_response = api_instance.files_post(file_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling FilesApi->files_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload File
        api_response = api_instance.files_post(file_payload, expires_after_days=expires_after_days)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling FilesApi->files_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_payload** | [**FilePayload**](FilePayload.md)|  |
 **expires_after_days** | **int, none_type**| After how many days should the file be deleted. | [optional]

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

