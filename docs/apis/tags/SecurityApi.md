<a name="__pageTop"></a>
# ElasticEmail.apis.tags.security_api.SecurityApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**security_apikeys_by_name_delete**](#security_apikeys_by_name_delete) | **delete** /security/apikeys/{name} | Delete ApiKey
[**security_apikeys_by_name_get**](#security_apikeys_by_name_get) | **get** /security/apikeys/{name} | Load ApiKey
[**security_apikeys_by_name_put**](#security_apikeys_by_name_put) | **put** /security/apikeys/{name} | Update ApiKey
[**security_apikeys_get**](#security_apikeys_get) | **get** /security/apikeys | List ApiKeys
[**security_apikeys_post**](#security_apikeys_post) | **post** /security/apikeys | Add ApiKey
[**security_smtp_by_name_delete**](#security_smtp_by_name_delete) | **delete** /security/smtp/{name} | Delete SMTP Credential
[**security_smtp_by_name_get**](#security_smtp_by_name_get) | **get** /security/smtp/{name} | Load SMTP Credential
[**security_smtp_by_name_put**](#security_smtp_by_name_put) | **put** /security/smtp/{name} | Update SMTP Credential
[**security_smtp_get**](#security_smtp_get) | **get** /security/smtp | List SMTP Credentials
[**security_smtp_post**](#security_smtp_post) | **post** /security/smtp | Add SMTP Credential

# **security_apikeys_by_name_delete**
<a name="security_apikeys_by_name_delete"></a>
> security_apikeys_by_name_delete(name)

Delete ApiKey

Delete your existing ApiKey. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        # Delete ApiKey
        api_response = api_instance.security_apikeys_by_name_delete(
            path_params=path_params,
            query_params=query_params,
        )
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_apikeys_by_name_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'subaccount': "subaccount_example",
    }
    try:
        # Delete ApiKey
        api_response = api_instance.security_apikeys_by_name_delete(
            path_params=path_params,
            query_params=query_params,
        )
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_apikeys_by_name_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
subaccount | SubaccountSchema | | optional


# SubaccountSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#security_apikeys_by_name_delete.ApiResponseFor200) | OK

#### security_apikeys_by_name_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_apikeys_by_name_get**
<a name="security_apikeys_by_name_get"></a>
> ApiKey security_apikeys_by_name_get(name)

Load ApiKey

Load your existing ApiKey info. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
from ElasticEmail.model.api_key import ApiKey
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        # Load ApiKey
        api_response = api_instance.security_apikeys_by_name_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_apikeys_by_name_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'subaccount': "subaccount_example",
    }
    try:
        # Load ApiKey
        api_response = api_instance.security_apikeys_by_name_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_apikeys_by_name_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
subaccount | SubaccountSchema | | optional


# SubaccountSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#security_apikeys_by_name_get.ApiResponseFor200) | OK

#### security_apikeys_by_name_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiKey**](../../models/ApiKey.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_apikeys_by_name_put**
<a name="security_apikeys_by_name_put"></a>
> ApiKey security_apikeys_by_name_put(nameapi_key_payload)

Update ApiKey

Update your existing ApiKey. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
from ElasticEmail.model.api_key import ApiKey
from ElasticEmail.model.api_key_payload import ApiKeyPayload
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    body = ApiKeyPayload(
        name="name_example",
        access_level=[
            AccessLevel("None")
        ],
        expires="1970-01-01T00:00:00.00Z",
        restrict_access_to_ip_range=[
            "restrict_access_to_ip_range_example"
        ],
        subaccount="subaccount_example",
    )
    try:
        # Update ApiKey
        api_response = api_instance.security_apikeys_by_name_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_apikeys_by_name_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiKeyPayload**](../../models/ApiKeyPayload.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#security_apikeys_by_name_put.ApiResponseFor200) | OK

#### security_apikeys_by_name_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiKey**](../../models/ApiKey.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_apikeys_get**
<a name="security_apikeys_get"></a>
> [ApiKey] security_apikeys_get()

List ApiKeys

List all your existing ApiKeys. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
from ElasticEmail.model.api_key import ApiKey
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only optional values
    query_params = {
        'subaccount': "subaccount_example",
    }
    try:
        # List ApiKeys
        api_response = api_instance.security_apikeys_get(
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_apikeys_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
subaccount | SubaccountSchema | | optional


# SubaccountSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#security_apikeys_get.ApiResponseFor200) | OK

#### security_apikeys_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiKey**]({{complexTypePrefix}}ApiKey.md) | [**ApiKey**]({{complexTypePrefix}}ApiKey.md) | [**ApiKey**]({{complexTypePrefix}}ApiKey.md) |  | 

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_apikeys_post**
<a name="security_apikeys_post"></a>
> NewApiKey security_apikeys_post(api_key_payload)

Add ApiKey

Add a new ApiKey. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
from ElasticEmail.model.new_api_key import NewApiKey
from ElasticEmail.model.api_key_payload import ApiKeyPayload
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    body = ApiKeyPayload(
        name="name_example",
        access_level=[
            AccessLevel("None")
        ],
        expires="1970-01-01T00:00:00.00Z",
        restrict_access_to_ip_range=[
            "restrict_access_to_ip_range_example"
        ],
        subaccount="subaccount_example",
    )
    try:
        # Add ApiKey
        api_response = api_instance.security_apikeys_post(
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_apikeys_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiKeyPayload**](../../models/ApiKeyPayload.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#security_apikeys_post.ApiResponseFor201) | Created

#### security_apikeys_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NewApiKey**](../../models/NewApiKey.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_smtp_by_name_delete**
<a name="security_smtp_by_name_delete"></a>
> security_smtp_by_name_delete(name)

Delete SMTP Credential

Delete your existing SMTP Credentials. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        # Delete SMTP Credential
        api_response = api_instance.security_smtp_by_name_delete(
            path_params=path_params,
            query_params=query_params,
        )
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_smtp_by_name_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'subaccount': "subaccount_example",
    }
    try:
        # Delete SMTP Credential
        api_response = api_instance.security_smtp_by_name_delete(
            path_params=path_params,
            query_params=query_params,
        )
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_smtp_by_name_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
subaccount | SubaccountSchema | | optional


# SubaccountSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#security_smtp_by_name_delete.ApiResponseFor200) | OK

#### security_smtp_by_name_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_smtp_by_name_get**
<a name="security_smtp_by_name_get"></a>
> SmtpCredentials security_smtp_by_name_get(name)

Load SMTP Credential

Load your existing SMTP Credential info. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
from ElasticEmail.model.smtp_credentials import SmtpCredentials
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        # Load SMTP Credential
        api_response = api_instance.security_smtp_by_name_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_smtp_by_name_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'subaccount': "subaccount_example",
    }
    try:
        # Load SMTP Credential
        api_response = api_instance.security_smtp_by_name_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_smtp_by_name_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
subaccount | SubaccountSchema | | optional


# SubaccountSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#security_smtp_by_name_get.ApiResponseFor200) | OK

#### security_smtp_by_name_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SmtpCredentials**](../../models/SmtpCredentials.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_smtp_by_name_put**
<a name="security_smtp_by_name_put"></a>
> SmtpCredentials security_smtp_by_name_put(namesmtp_credentials_payload)

Update SMTP Credential

Update your existing SMTP Credentials. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
from ElasticEmail.model.smtp_credentials import SmtpCredentials
from ElasticEmail.model.smtp_credentials_payload import SmtpCredentialsPayload
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    body = SmtpCredentialsPayload(
        name="name_example",
        expires="1970-01-01T00:00:00.00Z",
        restrict_access_to_ip_range=[
            "restrict_access_to_ip_range_example"
        ],
        subaccount="subaccount_example",
    )
    try:
        # Update SMTP Credential
        api_response = api_instance.security_smtp_by_name_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_smtp_by_name_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SmtpCredentialsPayload**](../../models/SmtpCredentialsPayload.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#security_smtp_by_name_put.ApiResponseFor200) | OK

#### security_smtp_by_name_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SmtpCredentials**](../../models/SmtpCredentials.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_smtp_get**
<a name="security_smtp_get"></a>
> [SmtpCredentials] security_smtp_get()

List SMTP Credentials

List all your existing SMTP Credentials. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
from ElasticEmail.model.smtp_credentials import SmtpCredentials
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only optional values
    query_params = {
        'subaccount': "subaccount_example",
    }
    try:
        # List SMTP Credentials
        api_response = api_instance.security_smtp_get(
            query_params=query_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_smtp_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
subaccount | SubaccountSchema | | optional


# SubaccountSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#security_smtp_get.ApiResponseFor200) | OK

#### security_smtp_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SmtpCredentials**]({{complexTypePrefix}}SmtpCredentials.md) | [**SmtpCredentials**]({{complexTypePrefix}}SmtpCredentials.md) | [**SmtpCredentials**]({{complexTypePrefix}}SmtpCredentials.md) |  | 

### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **security_smtp_post**
<a name="security_smtp_post"></a>
> NewSmtpCredentials security_smtp_post(smtp_credentials_payload)

Add SMTP Credential

Add new SMTP Credential. Required Access Level: Security

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import security_api
from ElasticEmail.model.new_smtp_credentials import NewSmtpCredentials
from ElasticEmail.model.smtp_credentials_payload import SmtpCredentialsPayload
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
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    body = SmtpCredentialsPayload(
        name="name_example",
        expires="1970-01-01T00:00:00.00Z",
        restrict_access_to_ip_range=[
            "restrict_access_to_ip_range_example"
        ],
        subaccount="subaccount_example",
    )
    try:
        # Add SMTP Credential
        api_response = api_instance.security_smtp_post(
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling SecurityApi->security_smtp_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SmtpCredentialsPayload**](../../models/SmtpCredentialsPayload.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#security_smtp_post.ApiResponseFor201) | Created

#### security_smtp_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NewSmtpCredentials**](../../models/NewSmtpCredentials.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

