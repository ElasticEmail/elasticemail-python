# ElasticEmail.SecurityApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**security_apikeys_by_name_delete**](SecurityApi.md#security_apikeys_by_name_delete) | **DELETE** /security/apikeys/{name} | Delete ApiKey
[**security_apikeys_by_name_get**](SecurityApi.md#security_apikeys_by_name_get) | **GET** /security/apikeys/{name} | Load ApiKey
[**security_apikeys_by_name_put**](SecurityApi.md#security_apikeys_by_name_put) | **PUT** /security/apikeys/{name} | Update ApiKey
[**security_apikeys_get**](SecurityApi.md#security_apikeys_get) | **GET** /security/apikeys | List ApiKeys
[**security_apikeys_post**](SecurityApi.md#security_apikeys_post) | **POST** /security/apikeys | Add ApiKey
[**security_smtp_by_name_delete**](SecurityApi.md#security_smtp_by_name_delete) | **DELETE** /security/smtp/{name} | Delete SMTP Credential
[**security_smtp_by_name_get**](SecurityApi.md#security_smtp_by_name_get) | **GET** /security/smtp/{name} | Load SMTP Credential
[**security_smtp_by_name_put**](SecurityApi.md#security_smtp_by_name_put) | **PUT** /security/smtp/{name} | Update SMTP Credential
[**security_smtp_get**](SecurityApi.md#security_smtp_get) | **GET** /security/smtp | List SMTP Credentials
[**security_smtp_post**](SecurityApi.md#security_smtp_post) | **POST** /security/smtp | Add SMTP Credential


# **security_apikeys_by_name_delete**
> security_apikeys_by_name_delete(name, subaccount=subaccount)

Delete ApiKey

Delete your existing ApiKey. Required Access Level: ModifyAccessTokens

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
    api_instance = ElasticEmail.SecurityApi(api_client)
    name = 'name_example' # str | Name of the ApiKey
    subaccount = 'subaccount_example' # str | Email of the subaccount of which ApiKey should be deleted (optional)

    try:
        # Delete ApiKey
        api_instance.security_apikeys_by_name_delete(name, subaccount=subaccount)
    except Exception as e:
        print("Exception when calling SecurityApi->security_apikeys_by_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the ApiKey | 
 **subaccount** | **str**| Email of the subaccount of which ApiKey should be deleted | [optional] 

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

# **security_apikeys_by_name_get**
> ApiKey security_apikeys_by_name_get(name, subaccount=subaccount)

Load ApiKey

Load your existing ApiKey info. Required Access Level: Security

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.api_key import ApiKey
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
    api_instance = ElasticEmail.SecurityApi(api_client)
    name = 'name_example' # str | Name of the ApiKey
    subaccount = 'subaccount_example' # str | Email of the subaccount of which ApiKey should be loaded (optional)

    try:
        # Load ApiKey
        api_response = api_instance.security_apikeys_by_name_get(name, subaccount=subaccount)
        print("The response of SecurityApi->security_apikeys_by_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->security_apikeys_by_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the ApiKey | 
 **subaccount** | **str**| Email of the subaccount of which ApiKey should be loaded | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

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

# **security_apikeys_by_name_put**
> ApiKey security_apikeys_by_name_put(name, api_key_payload)

Update ApiKey

Update your existing ApiKey. Required Access Level: ModifyAccessTokens

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.api_key import ApiKey
from ElasticEmail.models.api_key_payload import ApiKeyPayload
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
    api_instance = ElasticEmail.SecurityApi(api_client)
    name = 'name_example' # str | Name of the ApiKey
    api_key_payload = ElasticEmail.ApiKeyPayload() # ApiKeyPayload | 

    try:
        # Update ApiKey
        api_response = api_instance.security_apikeys_by_name_put(name, api_key_payload)
        print("The response of SecurityApi->security_apikeys_by_name_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->security_apikeys_by_name_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the ApiKey | 
 **api_key_payload** | [**ApiKeyPayload**](ApiKeyPayload.md)|  | 

### Return type

[**ApiKey**](ApiKey.md)

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

# **security_apikeys_get**
> List[ApiKey] security_apikeys_get(subaccount=subaccount)

List ApiKeys

List all your existing ApiKeys. Required Access Level: Security

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.api_key import ApiKey
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
    api_instance = ElasticEmail.SecurityApi(api_client)
    subaccount = 'subaccount_example' # str | Email of the subaccount of which ApiKeys should be loaded (optional)

    try:
        # List ApiKeys
        api_response = api_instance.security_apikeys_get(subaccount=subaccount)
        print("The response of SecurityApi->security_apikeys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->security_apikeys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount** | **str**| Email of the subaccount of which ApiKeys should be loaded | [optional] 

### Return type

[**List[ApiKey]**](ApiKey.md)

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

# **security_apikeys_post**
> NewApiKey security_apikeys_post(api_key_payload)

Add ApiKey

Add a new ApiKey. Required Access Level: ModifyAccessTokens

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.api_key_payload import ApiKeyPayload
from ElasticEmail.models.new_api_key import NewApiKey
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
    api_instance = ElasticEmail.SecurityApi(api_client)
    api_key_payload = ElasticEmail.ApiKeyPayload() # ApiKeyPayload | 

    try:
        # Add ApiKey
        api_response = api_instance.security_apikeys_post(api_key_payload)
        print("The response of SecurityApi->security_apikeys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->security_apikeys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_payload** | [**ApiKeyPayload**](ApiKeyPayload.md)|  | 

### Return type

[**NewApiKey**](NewApiKey.md)

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

# **security_smtp_by_name_delete**
> security_smtp_by_name_delete(name, subaccount=subaccount)

Delete SMTP Credential

Delete your existing SMTP Credentials. Required Access Level: ModifyAccessTokens

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
    api_instance = ElasticEmail.SecurityApi(api_client)
    name = 'name_example' # str | Name of the SMTP Credential
    subaccount = 'subaccount_example' # str | Email of the subaccount of which credential should be deleted (optional)

    try:
        # Delete SMTP Credential
        api_instance.security_smtp_by_name_delete(name, subaccount=subaccount)
    except Exception as e:
        print("Exception when calling SecurityApi->security_smtp_by_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the SMTP Credential | 
 **subaccount** | **str**| Email of the subaccount of which credential should be deleted | [optional] 

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

# **security_smtp_by_name_get**
> SmtpCredentials security_smtp_by_name_get(name, subaccount=subaccount)

Load SMTP Credential

Load your existing SMTP Credential info. Required Access Level: Security

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.smtp_credentials import SmtpCredentials
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
    api_instance = ElasticEmail.SecurityApi(api_client)
    name = 'name_example' # str | Name of the SMTP Credential
    subaccount = 'subaccount_example' # str | Email of the subaccount of which credential should be loaded (optional)

    try:
        # Load SMTP Credential
        api_response = api_instance.security_smtp_by_name_get(name, subaccount=subaccount)
        print("The response of SecurityApi->security_smtp_by_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->security_smtp_by_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the SMTP Credential | 
 **subaccount** | **str**| Email of the subaccount of which credential should be loaded | [optional] 

### Return type

[**SmtpCredentials**](SmtpCredentials.md)

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

# **security_smtp_by_name_put**
> SmtpCredentials security_smtp_by_name_put(name, smtp_credentials_payload)

Update SMTP Credential

Update your existing SMTP Credentials. Required Access Level: ModifyAccessTokens

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.smtp_credentials import SmtpCredentials
from ElasticEmail.models.smtp_credentials_payload import SmtpCredentialsPayload
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
    api_instance = ElasticEmail.SecurityApi(api_client)
    name = 'name_example' # str | Name of the SMTP Credential
    smtp_credentials_payload = ElasticEmail.SmtpCredentialsPayload() # SmtpCredentialsPayload | 

    try:
        # Update SMTP Credential
        api_response = api_instance.security_smtp_by_name_put(name, smtp_credentials_payload)
        print("The response of SecurityApi->security_smtp_by_name_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->security_smtp_by_name_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the SMTP Credential | 
 **smtp_credentials_payload** | [**SmtpCredentialsPayload**](SmtpCredentialsPayload.md)|  | 

### Return type

[**SmtpCredentials**](SmtpCredentials.md)

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

# **security_smtp_get**
> List[SmtpCredentials] security_smtp_get(subaccount=subaccount)

List SMTP Credentials

List all your existing SMTP Credentials. Required Access Level: Security

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.smtp_credentials import SmtpCredentials
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
    api_instance = ElasticEmail.SecurityApi(api_client)
    subaccount = 'subaccount_example' # str | Email of the subaccount of which credentials should be listed (optional)

    try:
        # List SMTP Credentials
        api_response = api_instance.security_smtp_get(subaccount=subaccount)
        print("The response of SecurityApi->security_smtp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->security_smtp_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount** | **str**| Email of the subaccount of which credentials should be listed | [optional] 

### Return type

[**List[SmtpCredentials]**](SmtpCredentials.md)

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

# **security_smtp_post**
> NewSmtpCredentials security_smtp_post(smtp_credentials_payload)

Add SMTP Credential

Add new SMTP Credential. Required Access Level: ModifyAccessTokens

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.new_smtp_credentials import NewSmtpCredentials
from ElasticEmail.models.smtp_credentials_payload import SmtpCredentialsPayload
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
    api_instance = ElasticEmail.SecurityApi(api_client)
    smtp_credentials_payload = ElasticEmail.SmtpCredentialsPayload() # SmtpCredentialsPayload | 

    try:
        # Add SMTP Credential
        api_response = api_instance.security_smtp_post(smtp_credentials_payload)
        print("The response of SecurityApi->security_smtp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->security_smtp_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smtp_credentials_payload** | [**SmtpCredentialsPayload**](SmtpCredentialsPayload.md)|  | 

### Return type

[**NewSmtpCredentials**](NewSmtpCredentials.md)

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

