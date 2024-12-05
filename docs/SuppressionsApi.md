# ElasticEmail.SuppressionsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suppressions_bounces_get**](SuppressionsApi.md#suppressions_bounces_get) | **GET** /suppressions/bounces | Get Bounce List
[**suppressions_bounces_import_post**](SuppressionsApi.md#suppressions_bounces_import_post) | **POST** /suppressions/bounces/import | Add Bounces Async
[**suppressions_bounces_post**](SuppressionsApi.md#suppressions_bounces_post) | **POST** /suppressions/bounces | Add Bounces
[**suppressions_by_email_delete**](SuppressionsApi.md#suppressions_by_email_delete) | **DELETE** /suppressions/{email} | Delete Suppression
[**suppressions_by_email_get**](SuppressionsApi.md#suppressions_by_email_get) | **GET** /suppressions/{email} | Get Suppression
[**suppressions_complaints_get**](SuppressionsApi.md#suppressions_complaints_get) | **GET** /suppressions/complaints | Get Complaints List
[**suppressions_complaints_import_post**](SuppressionsApi.md#suppressions_complaints_import_post) | **POST** /suppressions/complaints/import | Add Complaints Async
[**suppressions_complaints_post**](SuppressionsApi.md#suppressions_complaints_post) | **POST** /suppressions/complaints | Add Complaints
[**suppressions_get**](SuppressionsApi.md#suppressions_get) | **GET** /suppressions | Get Suppressions
[**suppressions_unsubscribes_get**](SuppressionsApi.md#suppressions_unsubscribes_get) | **GET** /suppressions/unsubscribes | Get Unsubscribes List
[**suppressions_unsubscribes_import_post**](SuppressionsApi.md#suppressions_unsubscribes_import_post) | **POST** /suppressions/unsubscribes/import | Add Unsubscribes Async
[**suppressions_unsubscribes_post**](SuppressionsApi.md#suppressions_unsubscribes_post) | **POST** /suppressions/unsubscribes | Add Unsubscribes


# **suppressions_bounces_get**
> List[Suppression] suppressions_bounces_get(search=search, limit=limit, offset=offset)

Get Bounce List

Retrieve your list of bounced emails. Required Access Level: ViewContacts, ViewSuppressions

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.suppression import Suppression
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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    search = 'text' # str | Text fragment used for searching. (optional)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Get Bounce List
        api_response = api_instance.suppressions_bounces_get(search=search, limit=limit, offset=offset)
        print("The response of SuppressionsApi->suppressions_bounces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_bounces_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Text fragment used for searching. | [optional] 
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[Suppression]**](Suppression.md)

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

# **suppressions_bounces_import_post**
> suppressions_bounces_import_post(file=file)

Add Bounces Async

Add Bounced. Required Access Level: ModifyContacts, ModifySuppressions

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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Add Bounces Async
        api_instance.suppressions_bounces_import_post(file=file)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_bounces_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppressions_bounces_post**
> List[Suppression] suppressions_bounces_post(request_body)

Add Bounces

Add Bounced. Required Access Level: ModifyContacts, ModifySuppressions

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.suppression import Suppression
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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    request_body = ['request_body_example'] # List[str] | Emails to add as bounces. Limited to 1000 per request

    try:
        # Add Bounces
        api_response = api_instance.suppressions_bounces_post(request_body)
        print("The response of SuppressionsApi->suppressions_bounces_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_bounces_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Emails to add as bounces. Limited to 1000 per request | 

### Return type

[**List[Suppression]**](Suppression.md)

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

# **suppressions_by_email_delete**
> suppressions_by_email_delete(email)

Delete Suppression

Delete Suppression. Required Access Level: ViewContacts, ViewSuppressions

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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    email = 'mail@example.com' # str | Proper email address.

    try:
        # Delete Suppression
        api_instance.suppressions_by_email_delete(email)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_by_email_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Proper email address. | 

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

# **suppressions_by_email_get**
> Suppression suppressions_by_email_get(email)

Get Suppression

Retrieve your suppression. Required Access Level: ViewContacts, ViewSuppressions

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.suppression import Suppression
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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    email = 'mail@example.com' # str | Proper email address.

    try:
        # Get Suppression
        api_response = api_instance.suppressions_by_email_get(email)
        print("The response of SuppressionsApi->suppressions_by_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_by_email_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Proper email address. | 

### Return type

[**Suppression**](Suppression.md)

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

# **suppressions_complaints_get**
> List[Suppression] suppressions_complaints_get(search=search, limit=limit, offset=offset)

Get Complaints List

Retrieve your list of complaints. Required Access Level: ViewContacts, ViewSuppressions

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.suppression import Suppression
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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    search = 'text' # str | Text fragment used for searching. (optional)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Get Complaints List
        api_response = api_instance.suppressions_complaints_get(search=search, limit=limit, offset=offset)
        print("The response of SuppressionsApi->suppressions_complaints_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_complaints_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Text fragment used for searching. | [optional] 
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[Suppression]**](Suppression.md)

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

# **suppressions_complaints_import_post**
> suppressions_complaints_import_post(file=file)

Add Complaints Async

Add Complaints. Required Access Level: ModifyContacts, ModifySuppressions

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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Add Complaints Async
        api_instance.suppressions_complaints_import_post(file=file)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_complaints_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppressions_complaints_post**
> List[Suppression] suppressions_complaints_post(request_body)

Add Complaints

Add Complaints. Required Access Level: ModifyContacts, ModifySuppressions

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.suppression import Suppression
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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    request_body = ['request_body_example'] # List[str] | Emails to add as complaints. Limited to 1000 per request

    try:
        # Add Complaints
        api_response = api_instance.suppressions_complaints_post(request_body)
        print("The response of SuppressionsApi->suppressions_complaints_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_complaints_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Emails to add as complaints. Limited to 1000 per request | 

### Return type

[**List[Suppression]**](Suppression.md)

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

# **suppressions_get**
> List[Suppression] suppressions_get(limit=limit, offset=offset)

Get Suppressions

Retrieve your suppressions. Required Access Level: ViewContacts, ViewSuppressions

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.suppression import Suppression
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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Get Suppressions
        api_response = api_instance.suppressions_get(limit=limit, offset=offset)
        print("The response of SuppressionsApi->suppressions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[Suppression]**](Suppression.md)

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

# **suppressions_unsubscribes_get**
> List[Suppression] suppressions_unsubscribes_get(search=search, limit=limit, offset=offset)

Get Unsubscribes List

Retrieve your list of unsubscribes. Required Access Level: ViewContacts, ViewSuppressions

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.suppression import Suppression
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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    search = 'text' # str | Text fragment used for searching. (optional)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Get Unsubscribes List
        api_response = api_instance.suppressions_unsubscribes_get(search=search, limit=limit, offset=offset)
        print("The response of SuppressionsApi->suppressions_unsubscribes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_unsubscribes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Text fragment used for searching. | [optional] 
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[Suppression]**](Suppression.md)

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

# **suppressions_unsubscribes_import_post**
> suppressions_unsubscribes_import_post(file=file)

Add Unsubscribes Async

Add Unsubscribes. Required Access Level: ModifyContacts, ModifySuppressions

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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Add Unsubscribes Async
        api_instance.suppressions_unsubscribes_import_post(file=file)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_unsubscribes_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppressions_unsubscribes_post**
> List[Suppression] suppressions_unsubscribes_post(request_body)

Add Unsubscribes

Add Unsubscribes. Required Access Level: ModifyContacts, ModifySuppressions

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.suppression import Suppression
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
    api_instance = ElasticEmail.SuppressionsApi(api_client)
    request_body = ['request_body_example'] # List[str] | Emails to add as unsubscribes. Limited to 1000 per request

    try:
        # Add Unsubscribes
        api_response = api_instance.suppressions_unsubscribes_post(request_body)
        print("The response of SuppressionsApi->suppressions_unsubscribes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->suppressions_unsubscribes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Emails to add as unsubscribes. Limited to 1000 per request | 

### Return type

[**List[Suppression]**](Suppression.md)

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

