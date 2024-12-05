# ElasticEmail.DomainsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domains_by_domain_delete**](DomainsApi.md#domains_by_domain_delete) | **DELETE** /domains/{domain} | Delete Domain
[**domains_by_domain_get**](DomainsApi.md#domains_by_domain_get) | **GET** /domains/{domain} | Load Domain
[**domains_by_domain_put**](DomainsApi.md#domains_by_domain_put) | **PUT** /domains/{domain} | Update Domain
[**domains_by_domain_restricted_get**](DomainsApi.md#domains_by_domain_restricted_get) | **GET** /domains/{domain}/restricted | Check for domain restriction
[**domains_by_domain_verification_put**](DomainsApi.md#domains_by_domain_verification_put) | **PUT** /domains/{domain}/verification | Verify Domain
[**domains_by_email_default_patch**](DomainsApi.md#domains_by_email_default_patch) | **PATCH** /domains/{email}/default | Set Default
[**domains_get**](DomainsApi.md#domains_get) | **GET** /domains | Load Domains
[**domains_post**](DomainsApi.md#domains_post) | **POST** /domains | Add Domain


# **domains_by_domain_delete**
> domains_by_domain_delete(domain)

Delete Domain

Deletes configured domain from Account. Required Access Level: ModifySettings

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
    api_instance = ElasticEmail.DomainsApi(api_client)
    domain = 'domain_example' # str | Name of the given domain

    try:
        # Delete Domain
        api_instance.domains_by_domain_delete(domain)
    except Exception as e:
        print("Exception when calling DomainsApi->domains_by_domain_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Name of the given domain | 

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

# **domains_by_domain_get**
> DomainData domains_by_domain_get(domain)

Load Domain

Retrieve a domain configured for this Account. Required Access Level: ViewSettings

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.domain_data import DomainData
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
    api_instance = ElasticEmail.DomainsApi(api_client)
    domain = 'domain_example' # str | Name of the given domain

    try:
        # Load Domain
        api_response = api_instance.domains_by_domain_get(domain)
        print("The response of DomainsApi->domains_by_domain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domains_by_domain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Name of the given domain | 

### Return type

[**DomainData**](DomainData.md)

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

# **domains_by_domain_put**
> DomainDetail domains_by_domain_put(domain, domain_update_payload)

Update Domain

Updates the specified domain. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.domain_detail import DomainDetail
from ElasticEmail.models.domain_update_payload import DomainUpdatePayload
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
    api_instance = ElasticEmail.DomainsApi(api_client)
    domain = 'domain_example' # str | Name of the given domain
    domain_update_payload = ElasticEmail.DomainUpdatePayload() # DomainUpdatePayload | Updated Domain resource

    try:
        # Update Domain
        api_response = api_instance.domains_by_domain_put(domain, domain_update_payload)
        print("The response of DomainsApi->domains_by_domain_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domains_by_domain_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Name of the given domain | 
 **domain_update_payload** | [**DomainUpdatePayload**](DomainUpdatePayload.md)| Updated Domain resource | 

### Return type

[**DomainDetail**](DomainDetail.md)

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

# **domains_by_domain_restricted_get**
> bool domains_by_domain_restricted_get(domain)

Check for domain restriction

Checking if domain is from free provider, or restricted. Required Access Level: ViewSettings

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
    api_instance = ElasticEmail.DomainsApi(api_client)
    domain = 'domain_example' # str | Name of the given domain

    try:
        # Check for domain restriction
        api_response = api_instance.domains_by_domain_restricted_get(domain)
        print("The response of DomainsApi->domains_by_domain_restricted_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domains_by_domain_restricted_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Name of the given domain | 

### Return type

**bool**

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

# **domains_by_domain_verification_put**
> DomainData domains_by_domain_verification_put(domain, body)

Verify Domain

Verifies that required DNS records exist for specified domain. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.domain_data import DomainData
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
    api_instance = ElasticEmail.DomainsApi(api_client)
    domain = 'domain_example' # str | Name of the given domain
    body = 'body_example' # str | Tracking type used in the Tracking verification

    try:
        # Verify Domain
        api_response = api_instance.domains_by_domain_verification_put(domain, body)
        print("The response of DomainsApi->domains_by_domain_verification_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domains_by_domain_verification_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Name of the given domain | 
 **body** | **str**| Tracking type used in the Tracking verification | 

### Return type

[**DomainData**](DomainData.md)

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

# **domains_by_email_default_patch**
> DomainDetail domains_by_email_default_patch(email)

Set Default

Sets a verified email address as default sender. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.domain_detail import DomainDetail
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
    api_instance = ElasticEmail.DomainsApi(api_client)
    email = 'email_example' # str | Default email sender, example: mail@yourdomain.com

    try:
        # Set Default
        api_response = api_instance.domains_by_email_default_patch(email)
        print("The response of DomainsApi->domains_by_email_default_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domains_by_email_default_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Default email sender, example: mail@yourdomain.com | 

### Return type

[**DomainDetail**](DomainDetail.md)

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

# **domains_get**
> List[DomainDetail] domains_get()

Load Domains

Returns a list of all domains configured for this Account. Required Access Level: ViewSettings

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.domain_detail import DomainDetail
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
    api_instance = ElasticEmail.DomainsApi(api_client)

    try:
        # Load Domains
        api_response = api_instance.domains_get()
        print("The response of DomainsApi->domains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domains_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DomainDetail]**](DomainDetail.md)

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

# **domains_post**
> DomainDetail domains_post(domain_payload)

Add Domain

Add new domain to Account. Required Access Level: ModifySettings

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.domain_detail import DomainDetail
from ElasticEmail.models.domain_payload import DomainPayload
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
    api_instance = ElasticEmail.DomainsApi(api_client)
    domain_payload = ElasticEmail.DomainPayload() # DomainPayload | Domain to add

    try:
        # Add Domain
        api_response = api_instance.domains_post(domain_payload)
        print("The response of DomainsApi->domains_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->domains_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_payload** | [**DomainPayload**](DomainPayload.md)| Domain to add | 

### Return type

[**DomainDetail**](DomainDetail.md)

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

