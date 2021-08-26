# ElasticEmail.TemplatesApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_by_name_delete**](TemplatesApi.md#templates_by_name_delete) | **DELETE** /templates/{name} | Delete Template
[**templates_by_name_get**](TemplatesApi.md#templates_by_name_get) | **GET** /templates/{name} | Load Template
[**templates_by_name_put**](TemplatesApi.md#templates_by_name_put) | **PUT** /templates/{name} | Update Template
[**templates_get**](TemplatesApi.md#templates_get) | **GET** /templates | Load Templates
[**templates_post**](TemplatesApi.md#templates_post) | **POST** /templates | Add Template


# **templates_by_name_delete**
> templates_by_name_delete(name)

Delete Template

Delete template with the specified name. Required Access Level: ModifyTemplates

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import templates_api
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
    api_instance = templates_api.TemplatesApi(api_client)
    name = "Template01" # str | Name of template.

    # example passing only required values which don't have defaults set
    try:
        # Delete Template
        api_instance.templates_by_name_delete(name)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_by_name_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template. |

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

# **templates_by_name_get**
> dict templates_by_name_get(name)

Load Template

Load detailed information of the specified template. Required Access Level: ViewTemplates

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import templates_api
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
    api_instance = templates_api.TemplatesApi(api_client)
    name = "Template01" # str | Name of template.

    # example passing only required values which don't have defaults set
    try:
        # Load Template
        api_response = api_instance.templates_by_name_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_by_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template. |

### Return type

**dict**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Serialized template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_by_name_put**
> Template templates_by_name_put(name, template_payload)

Update Template

Update existing template, overwriting existing data. Required Access Level: ModifyTemplates

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import templates_api
from ElasticEmail.model.template import Template
from ElasticEmail.model.template_payload import TemplatePayload
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
    api_instance = templates_api.TemplatesApi(api_client)
    name = "Template01" # str | Name of template.
    template_payload = TemplatePayload(
        name="name_example",
        subject="Hello!",
        body=[
            BodyPart(
                content_type=,
                content="content_example",
                charset="charset_example",
            ),
        ],
        template_scope=,
    ) # TemplatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update Template
        api_response = api_instance.templates_by_name_put(name, template_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_by_name_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template. |
 **template_payload** | [**TemplatePayload**](TemplatePayload.md)|  |

### Return type

[**Template**](Template.md)

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

# **templates_get**
> [Template] templates_get(scope_type)

Load Templates

Returns a list of templates for the specified type. Required Access Level: ViewTemplates

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import templates_api
from ElasticEmail.model.template import Template
from ElasticEmail.model.template_type import TemplateType
from ElasticEmail.model.template_scope import TemplateScope
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
    api_instance = templates_api.TemplatesApi(api_client)
    scope_type = [
        TemplateScope("Personal"),
    ] # [TemplateScope] | Return templates with specified scope only
    template_types = [
        TemplateType("RawHTML"),
    ] # [TemplateType] | Return templates with specified type only (optional)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Load Templates
        api_response = api_instance.templates_get(scope_type)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Load Templates
        api_response = api_instance.templates_get(scope_type, template_types=template_types, limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_type** | [**[TemplateScope]**](TemplateScope.md)| Return templates with specified scope only |
 **template_types** | [**[TemplateType]**](TemplateType.md)| Return templates with specified type only | [optional]
 **limit** | **int**| Maximum number of returned items. | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[Template]**](Template.md)

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

# **templates_post**
> dict templates_post(template_payload)

Add Template

Add a new Template. Required Access Level: ModifyTemplates

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import templates_api
from ElasticEmail.model.template_payload import TemplatePayload
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
    api_instance = templates_api.TemplatesApi(api_client)
    template_payload = TemplatePayload(
        name="name_example",
        subject="Hello!",
        body=[
            BodyPart(
                content_type=,
                content="content_example",
                charset="charset_example",
            ),
        ],
        template_scope=,
    ) # TemplatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Add Template
        api_response = api_instance.templates_post(template_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_payload** | [**TemplatePayload**](TemplatePayload.md)|  |

### Return type

**dict**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

