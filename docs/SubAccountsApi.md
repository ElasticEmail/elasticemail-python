# ElasticEmail.SubAccountsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccounts_by_email_credits_patch**](SubAccountsApi.md#subaccounts_by_email_credits_patch) | **PATCH** /subaccounts/{email}/credits | Add, Subtract Email Credits
[**subaccounts_by_email_delete**](SubAccountsApi.md#subaccounts_by_email_delete) | **DELETE** /subaccounts/{email} | Delete SubAccount
[**subaccounts_by_email_get**](SubAccountsApi.md#subaccounts_by_email_get) | **GET** /subaccounts/{email} | Load SubAccount
[**subaccounts_by_email_settings_email_put**](SubAccountsApi.md#subaccounts_by_email_settings_email_put) | **PUT** /subaccounts/{email}/settings/email | Update SubAccount Email Settings
[**subaccounts_get**](SubAccountsApi.md#subaccounts_get) | **GET** /subaccounts | Load SubAccounts
[**subaccounts_post**](SubAccountsApi.md#subaccounts_post) | **POST** /subaccounts | Add SubAccount


# **subaccounts_by_email_credits_patch**
> subaccounts_by_email_credits_patch(email, subaccount_email_credits_payload)

Add, Subtract Email Credits

Update email credits of a subaccount by the given amount. Required Access Level: ModifySubAccounts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.subaccount_email_credits_payload import SubaccountEmailCreditsPayload
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
    api_instance = ElasticEmail.SubAccountsApi(api_client)
    email = 'mail@example.com' # str | Email address of Sub-Account
    subaccount_email_credits_payload = ElasticEmail.SubaccountEmailCreditsPayload() # SubaccountEmailCreditsPayload | Amount of email credits to add or subtract from the current SubAccount email credits pool (positive or negative value)

    try:
        # Add, Subtract Email Credits
        api_instance.subaccounts_by_email_credits_patch(email, subaccount_email_credits_payload)
    except Exception as e:
        print("Exception when calling SubAccountsApi->subaccounts_by_email_credits_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address of Sub-Account | 
 **subaccount_email_credits_payload** | [**SubaccountEmailCreditsPayload**](SubaccountEmailCreditsPayload.md)| Amount of email credits to add or subtract from the current SubAccount email credits pool (positive or negative value) | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subaccounts_by_email_delete**
> subaccounts_by_email_delete(email)

Delete SubAccount

Deletes specified SubAccount. An email will be sent to confirm this change. Required Access Level: ModifySubAccounts

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
    api_instance = ElasticEmail.SubAccountsApi(api_client)
    email = 'mail@example.com' # str | Email address of Sub-Account

    try:
        # Delete SubAccount
        api_instance.subaccounts_by_email_delete(email)
    except Exception as e:
        print("Exception when calling SubAccountsApi->subaccounts_by_email_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address of Sub-Account | 

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

# **subaccounts_by_email_get**
> SubAccountInfo subaccounts_by_email_get(email)

Load SubAccount

Returns details for the specified SubAccount. Required Access Level: ViewSubAccounts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.sub_account_info import SubAccountInfo
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
    api_instance = ElasticEmail.SubAccountsApi(api_client)
    email = 'mail@example.com' # str | Email address of Sub-Account

    try:
        # Load SubAccount
        api_response = api_instance.subaccounts_by_email_get(email)
        print("The response of SubAccountsApi->subaccounts_by_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountsApi->subaccounts_by_email_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address of Sub-Account | 

### Return type

[**SubAccountInfo**](SubAccountInfo.md)

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

# **subaccounts_by_email_settings_email_put**
> SubaccountEmailSettings subaccounts_by_email_settings_email_put(email, subaccount_email_settings)

Update SubAccount Email Settings

Update SubAccount email settings. Required Access Level: ModifySubAccounts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.subaccount_email_settings import SubaccountEmailSettings
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
    api_instance = ElasticEmail.SubAccountsApi(api_client)
    email = 'email_example' # str | 
    subaccount_email_settings = ElasticEmail.SubaccountEmailSettings() # SubaccountEmailSettings | Updated Email Settings

    try:
        # Update SubAccount Email Settings
        api_response = api_instance.subaccounts_by_email_settings_email_put(email, subaccount_email_settings)
        print("The response of SubAccountsApi->subaccounts_by_email_settings_email_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountsApi->subaccounts_by_email_settings_email_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **subaccount_email_settings** | [**SubaccountEmailSettings**](SubaccountEmailSettings.md)| Updated Email Settings | 

### Return type

[**SubaccountEmailSettings**](SubaccountEmailSettings.md)

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

# **subaccounts_get**
> List[SubAccountInfo] subaccounts_get(limit=limit, offset=offset)

Load SubAccounts

Returns a list of all your SubAccounts. Required Access Level: ViewSubAccounts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.sub_account_info import SubAccountInfo
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
    api_instance = ElasticEmail.SubAccountsApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Load SubAccounts
        api_response = api_instance.subaccounts_get(limit=limit, offset=offset)
        print("The response of SubAccountsApi->subaccounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountsApi->subaccounts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[SubAccountInfo]**](SubAccountInfo.md)

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

# **subaccounts_post**
> SubAccountInfo subaccounts_post(subaccount_payload)

Add SubAccount

Add a new SubAccount to your Account. To receive an access token for this SubAccount, make a POST security/apikeys request using the 'subaccount' parameter. Required Access Level: ModifySubAccounts

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.sub_account_info import SubAccountInfo
from ElasticEmail.models.subaccount_payload import SubaccountPayload
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
    api_instance = ElasticEmail.SubAccountsApi(api_client)
    subaccount_payload = ElasticEmail.SubaccountPayload() # SubaccountPayload | 

    try:
        # Add SubAccount
        api_response = api_instance.subaccounts_post(subaccount_payload)
        print("The response of SubAccountsApi->subaccounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubAccountsApi->subaccounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_payload** | [**SubaccountPayload**](SubaccountPayload.md)|  | 

### Return type

[**SubAccountInfo**](SubAccountInfo.md)

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

