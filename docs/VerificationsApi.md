# ElasticEmail.VerificationsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifications_by_email_delete**](VerificationsApi.md#verifications_by_email_delete) | **DELETE** /verifications/{email} | Delete Email Verification Result
[**verifications_by_email_get**](VerificationsApi.md#verifications_by_email_get) | **GET** /verifications/{email} | Get Email Verification Result
[**verifications_by_email_post**](VerificationsApi.md#verifications_by_email_post) | **POST** /verifications/{email} | Verify Email
[**verifications_files_by_id_delete**](VerificationsApi.md#verifications_files_by_id_delete) | **DELETE** /verifications/files/{id} | Delete File Verification Result
[**verifications_files_by_id_result_download_get**](VerificationsApi.md#verifications_files_by_id_result_download_get) | **GET** /verifications/files/{id}/result/download | Download File Verification Result
[**verifications_files_by_id_result_get**](VerificationsApi.md#verifications_files_by_id_result_get) | **GET** /verifications/files/{id}/result | Get Detailed File Verification Result
[**verifications_files_post**](VerificationsApi.md#verifications_files_post) | **POST** /verifications/files | Verify From File
[**verifications_files_result_get**](VerificationsApi.md#verifications_files_result_get) | **GET** /verifications/files/result | Get Simple Files Verification Results
[**verifications_get**](VerificationsApi.md#verifications_get) | **GET** /verifications | Get Emails Verification Results


# **verifications_by_email_delete**
> verifications_by_email_delete(email)

Delete Email Verification Result

Delete a result with given email if exists. Required Access Level: VerifyEmails

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
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
    api_instance = verifications_api.VerificationsApi(api_client)
    email = "email_example" # str | Email address to verification

    # example passing only required values which don't have defaults set
    try:
        # Delete Email Verification Result
        api_instance.verifications_by_email_delete(email)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_by_email_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address to verification |

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

# **verifications_by_email_get**
> EmailValidationResult verifications_by_email_get(email)

Get Email Verification Result

Returns a result of verified email. Required Access Level: ViewEmailVerifications

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
from ElasticEmail.model.email_validation_result import EmailValidationResult
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
    api_instance = verifications_api.VerificationsApi(api_client)
    email = "email_example" # str | Email address to view verification result of

    # example passing only required values which don't have defaults set
    try:
        # Get Email Verification Result
        api_response = api_instance.verifications_by_email_get(email)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_by_email_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address to view verification result of |

### Return type

[**EmailValidationResult**](EmailValidationResult.md)

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

# **verifications_by_email_post**
> EmailValidationResult verifications_by_email_post(email)

Verify Email

Verify single email address and returns result of verification. Required Access Level: VerifyEmails

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
from ElasticEmail.model.email_validation_result import EmailValidationResult
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
    api_instance = verifications_api.VerificationsApi(api_client)
    email = "email_example" # str | Email address to verify

    # example passing only required values which don't have defaults set
    try:
        # Verify Email
        api_response = api_instance.verifications_by_email_post(email)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_by_email_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address to verify |

### Return type

[**EmailValidationResult**](EmailValidationResult.md)

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

# **verifications_files_by_id_delete**
> verifications_files_by_id_delete(id)

Delete File Verification Result

Delete Verification Results if they exist. Required Access Level: VerifyEmails

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
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
    api_instance = verifications_api.VerificationsApi(api_client)
    id = "E33EBA7A-C20D-4D3D-8F2F-5EEF42F58E6F" # str | ID of the exported file

    # example passing only required values which don't have defaults set
    try:
        # Delete File Verification Result
        api_instance.verifications_files_by_id_delete(id)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_files_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the exported file |

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

# **verifications_files_by_id_result_download_get**
> file_type verifications_files_by_id_result_download_get(id)

Download File Verification Result

Download verification results as a ZIP file. Required Access Level: VerifyEmails

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
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
    api_instance = verifications_api.VerificationsApi(api_client)
    id = "id_example" # str | Verification ID to download

    # example passing only required values which don't have defaults set
    try:
        # Download File Verification Result
        api_response = api_instance.verifications_files_by_id_result_download_get(id)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_files_by_id_result_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Verification ID to download |

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
**200** | A ZIP file with verification details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifications_files_by_id_result_get**
> VerificationFileResultDetails verifications_files_by_id_result_get(id)

Get Detailed File Verification Result

Returns status and results (if verified) of file with given ID. Required Access Level: ViewEmailVerifications

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
from ElasticEmail.model.verification_file_result_details import VerificationFileResultDetails
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
    api_instance = verifications_api.VerificationsApi(api_client)
    id = "id_example" # str | ID of the Verification to display status of
    limit = 1 # int | Maximum number of returned email verification results (optional)
    offset = 1 # int | How many result items should be returned ahead (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Detailed File Verification Result
        api_response = api_instance.verifications_files_by_id_result_get(id)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_files_by_id_result_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Detailed File Verification Result
        api_response = api_instance.verifications_files_by_id_result_get(id, limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_files_by_id_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Verification to display status of |
 **limit** | **int**| Maximum number of returned email verification results | [optional]
 **offset** | **int**| How many result items should be returned ahead | [optional]

### Return type

[**VerificationFileResultDetails**](VerificationFileResultDetails.md)

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

# **verifications_files_post**
> VerificationFileResult verifications_files_post()

Verify From File

Uploads a CSV file with list of emails to verify. An 'email' column is required. Required Access Level: VerifyEmails

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
from ElasticEmail.model.verification_file_result import VerificationFileResult
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
    api_instance = verifications_api.VerificationsApi(api_client)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Verify From File
        api_response = api_instance.verifications_files_post(file=file)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_files_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**|  | [optional]

### Return type

[**VerificationFileResult**](VerificationFileResult.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifications_files_result_get**
> [VerificationFileResult] verifications_files_result_get()

Get Simple Files Verification Results

Returns a list of uploaded files, their statuses and results. Required Access Level: ViewEmailVerifications

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
from ElasticEmail.model.verification_file_result import VerificationFileResult
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
    api_instance = verifications_api.VerificationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Simple Files Verification Results
        api_response = api_instance.verifications_files_result_get()
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_files_result_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[VerificationFileResult]**](VerificationFileResult.md)

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

# **verifications_get**
> [EmailValidationResult] verifications_get()

Get Emails Verification Results

Returns a results of all verified single emails. Required Access Level: ViewEmailVerifications

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import verifications_api
from ElasticEmail.model.email_validation_result import EmailValidationResult
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
    api_instance = verifications_api.VerificationsApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Emails Verification Results
        api_response = api_instance.verifications_get(limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling VerificationsApi->verifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[EmailValidationResult]**](EmailValidationResult.md)

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

