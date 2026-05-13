# ElasticEmail.WebhookApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_by_publicid_delete**](WebhookApi.md#webhook_by_publicid_delete) | **DELETE** /webhook/{publicid} | Delete Webhook
[**webhook_by_publicid_get**](WebhookApi.md#webhook_by_publicid_get) | **GET** /webhook/{publicid} | Load Webhook
[**webhook_by_publicid_put**](WebhookApi.md#webhook_by_publicid_put) | **PUT** /webhook/{publicid} | Update Webhook
[**webhook_get**](WebhookApi.md#webhook_get) | **GET** /webhook | Load Webhooks
[**webhook_post**](WebhookApi.md#webhook_post) | **POST** /webhook | Add Webhook


# **webhook_by_publicid_delete**
> webhook_by_publicid_delete(publicid)

Delete Webhook

Delete the specified notifications webhook. Required Access Level: ModifyWebNotifications

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
    api_instance = ElasticEmail.WebhookApi(api_client)
    publicid = 'publicid_example' # str | 

    try:
        # Delete Webhook
        api_instance.webhook_by_publicid_delete(publicid)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_by_publicid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicid** | **str**|  | 

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

# **webhook_by_publicid_get**
> Webhook webhook_by_publicid_get(publicid)

Load Webhook

Load notifications webhook details. Required Access Level: ViewWebNotifications

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.webhook import Webhook
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
    api_instance = ElasticEmail.WebhookApi(api_client)
    publicid = 'publicid_example' # str | 

    try:
        # Load Webhook
        api_response = api_instance.webhook_by_publicid_get(publicid)
        print("The response of WebhookApi->webhook_by_publicid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_by_publicid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicid** | **str**|  | 

### Return type

[**Webhook**](Webhook.md)

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

# **webhook_by_publicid_put**
> Webhook webhook_by_publicid_put(publicid, webhook_update_payload)

Update Webhook

Update notification webhook. Required Access Level: ModifyWebNotifications

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.webhook import Webhook
from ElasticEmail.models.webhook_update_payload import WebhookUpdatePayload
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
    api_instance = ElasticEmail.WebhookApi(api_client)
    publicid = 'publicid_example' # str | 
    webhook_update_payload = ElasticEmail.WebhookUpdatePayload() # WebhookUpdatePayload | 

    try:
        # Update Webhook
        api_response = api_instance.webhook_by_publicid_put(publicid, webhook_update_payload)
        print("The response of WebhookApi->webhook_by_publicid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_by_publicid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicid** | **str**|  | 
 **webhook_update_payload** | [**WebhookUpdatePayload**](WebhookUpdatePayload.md)|  | 

### Return type

[**Webhook**](Webhook.md)

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

# **webhook_get**
> List[Webhook] webhook_get(limit=limit, offset=offset)

Load Webhooks

Returns a list of notification webhooks. Required Access Level: ViewWebNotifications

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.webhook import Webhook
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
    api_instance = ElasticEmail.WebhookApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Load Webhooks
        api_response = api_instance.webhook_get(limit=limit, offset=offset)
        print("The response of WebhookApi->webhook_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[Webhook]**](Webhook.md)

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

# **webhook_post**
> Webhook webhook_post(webhook_create_payload)

Add Webhook

Add a notification webhook. Required Access Level: ModifyWebNotifications

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.webhook import Webhook
from ElasticEmail.models.webhook_create_payload import WebhookCreatePayload
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
    api_instance = ElasticEmail.WebhookApi(api_client)
    webhook_create_payload = ElasticEmail.WebhookCreatePayload() # WebhookCreatePayload | 

    try:
        # Add Webhook
        api_response = api_instance.webhook_post(webhook_create_payload)
        print("The response of WebhookApi->webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_create_payload** | [**WebhookCreatePayload**](WebhookCreatePayload.md)|  | 

### Return type

[**Webhook**](Webhook.md)

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

