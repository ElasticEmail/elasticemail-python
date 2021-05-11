# ElasticEmail.ContactsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacts_by_email_delete**](ContactsApi.md#contacts_by_email_delete) | **DELETE** /contacts/{email} | Delete Contact
[**contacts_by_email_get**](ContactsApi.md#contacts_by_email_get) | **GET** /contacts/{email} | Load Contact
[**contacts_by_email_history_get**](ContactsApi.md#contacts_by_email_history_get) | **GET** /contacts/{email}/history | Load History
[**contacts_by_email_put**](ContactsApi.md#contacts_by_email_put) | **PUT** /contacts/{email} | Update Contact
[**contacts_delete_post**](ContactsApi.md#contacts_delete_post) | **POST** /contacts/delete | Delete Contacts Bulk
[**contacts_export_by_id_status_get**](ContactsApi.md#contacts_export_by_id_status_get) | **GET** /contacts/export/{id}/status | Check Export Status
[**contacts_export_post**](ContactsApi.md#contacts_export_post) | **POST** /contacts/export | Export Contacts
[**contacts_get**](ContactsApi.md#contacts_get) | **GET** /contacts | Load Contacts
[**contacts_import_post**](ContactsApi.md#contacts_import_post) | **POST** /contacts/import | Upload Contacts
[**contacts_post**](ContactsApi.md#contacts_post) | **POST** /contacts | Add Contact


# **contacts_by_email_delete**
> contacts_by_email_delete(email)

Delete Contact

Deletes the provided contact. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
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
    api_instance = contacts_api.ContactsApi(api_client)
    email = "mail@example.com" # str | Proper email address.

    # example passing only required values which don't have defaults set
    try:
        # Delete Contact
        api_instance.contacts_by_email_delete(email)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_by_email_delete: %s\n" % e)
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

# **contacts_by_email_get**
> Contact contacts_by_email_get(email)

Load Contact

Load detailed contact information for specified email. Required Access Level: ViewContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.contact import Contact
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
    api_instance = contacts_api.ContactsApi(api_client)
    email = "mail@example.com" # str | Proper email address.

    # example passing only required values which don't have defaults set
    try:
        # Load Contact
        api_response = api_instance.contacts_by_email_get(email)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_by_email_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Proper email address. |

### Return type

[**Contact**](Contact.md)

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

# **contacts_by_email_history_get**
> [ContactHistory] contacts_by_email_history_get(email)

Load History

Returns detailed history of specified Contact. Required Access Level: ViewContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.contact_history import ContactHistory
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
    api_instance = contacts_api.ContactsApi(api_client)
    email = "mail@example.com" # str | Proper email address.
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Load History
        api_response = api_instance.contacts_by_email_history_get(email)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_by_email_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Load History
        api_response = api_instance.contacts_by_email_history_get(email, limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_by_email_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Proper email address. |
 **limit** | **int**| Maximum number of returned items. | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[ContactHistory]**](ContactHistory.md)

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

# **contacts_by_email_put**
> Contact contacts_by_email_put(email, contact_update_payload)

Update Contact

Update selected contact. Omitted contact's fields will not be changed. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.contact_update_payload import ContactUpdatePayload
from ElasticEmail.model.contact import Contact
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
    api_instance = contacts_api.ContactsApi(api_client)
    email = "mail@example.com" # str | Proper email address.
    contact_update_payload = ContactUpdatePayload(
        first_name="Fred",
        last_name="Flintstone",
        custom_fields={
            "key": "key_example",
        },
    ) # ContactUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update Contact
        api_response = api_instance.contacts_by_email_put(email, contact_update_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_by_email_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Proper email address. |
 **contact_update_payload** | [**ContactUpdatePayload**](ContactUpdatePayload.md)|  |

### Return type

[**Contact**](Contact.md)

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

# **contacts_delete_post**
> contacts_delete_post(emails_payload)

Delete Contacts Bulk

Deletes provided contacts in bulk. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.emails_payload import EmailsPayload
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
    api_instance = contacts_api.ContactsApi(api_client)
    emails_payload = EmailsPayload(
        rule="rule_example",
        emails=[
            "emails_example",
        ],
    ) # EmailsPayload | Provide either rule or a list of emails, not both.

    # example passing only required values which don't have defaults set
    try:
        # Delete Contacts Bulk
        api_instance.contacts_delete_post(emails_payload)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emails_payload** | [**EmailsPayload**](EmailsPayload.md)| Provide either rule or a list of emails, not both. |

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

# **contacts_export_by_id_status_get**
> ExportStatus contacts_export_by_id_status_get(id)

Check Export Status

Check the current status of the export. Required Access Level: Export

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.export_status import ExportStatus
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
    api_instance = contacts_api.ContactsApi(api_client)
    id = "E33EBA7A-C20D-4D3D-8F2F-5EEF42F58E6F" # str | ID of the exported file

    # example passing only required values which don't have defaults set
    try:
        # Check Export Status
        api_response = api_instance.contacts_export_by_id_status_get(id)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_export_by_id_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the exported file |

### Return type

[**ExportStatus**](ExportStatus.md)

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

# **contacts_export_post**
> ExportLink contacts_export_post()

Export Contacts

Request an Export of specified Contacts. Required Access Level: Export

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.export_link import ExportLink
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
    api_instance = contacts_api.ContactsApi(api_client)
    file_format =  # object | Format of the exported file (optional)
    rule = "Status%20=%20Engaged" # str | Query used for filtering. (optional)
    emails = [
        "emails_example",
    ] # [str] | Comma delimited list of contact emails (optional)
    compression_format =  # object | FileResponse compression format. None or Zip. (optional)
    file_name = "filename.txt" # str | Name of your file including extension. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Contacts
        api_response = api_instance.contacts_export_post(file_format=file_format, rule=rule, emails=emails, compression_format=compression_format, file_name=file_name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_format** | **object**| Format of the exported file | [optional]
 **rule** | **str**| Query used for filtering. | [optional]
 **emails** | **[str]**| Comma delimited list of contact emails | [optional]
 **compression_format** | **object**| FileResponse compression format. None or Zip. | [optional]
 **file_name** | **str**| Name of your file including extension. | [optional]

### Return type

[**ExportLink**](ExportLink.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_get**
> [Contact] contacts_get()

Load Contacts

Returns a list of contacts. Required Access Level: ViewContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.contact import Contact
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
    api_instance = contacts_api.ContactsApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Load Contacts
        api_response = api_instance.contacts_get(limit=limit, offset=offset)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional]
 **offset** | **int**| How many items should be returned ahead. | [optional]

### Return type

[**[Contact]**](Contact.md)

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

# **contacts_import_post**
> contacts_import_post()

Upload Contacts

Upload contacts from a file. Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
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
    api_instance = contacts_api.ContactsApi(api_client)
    list_name = "listName_example" # str | Name of an existing list to add these contacts to (optional)
    encoding_name = "encodingName_example" # str | In what encoding the file is uploaded (optional)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload Contacts
        api_instance.contacts_import_post(list_name=list_name, encoding_name=encoding_name, file=file)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_name** | **str**| Name of an existing list to add these contacts to | [optional]
 **encoding_name** | **str**| In what encoding the file is uploaded | [optional]
 **file** | **file_type**|  | [optional]

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

# **contacts_post**
> [Contact] contacts_post(contact_payload)

Add Contact

Add new Contacts to your Lists. Up to 1000 can be added (for more please refer to the import request). Required Access Level: ModifyContacts

### Example

* Api Key Authentication (apikey):
```python
import time
import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.contact import Contact
from ElasticEmail.model.contact_payload import ContactPayload
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
    api_instance = contacts_api.ContactsApi(api_client)
    contact_payload = [
        ContactPayload(
            email="mail@example.com",
            status=,
            first_name="Fred",
            last_name="Flintstone",
            custom_fields={
                "key": "key_example",
            },
            consent=ConsentData(
                consent_ip="192.168.0.1",
                consent_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                consent_tracking=,
            ),
        ),
    ] # [ContactPayload] | 
    listnames = [
        "listnames_example",
    ] # [str] | Names of lists to which the uploaded contacts should be added to (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Contact
        api_response = api_instance.contacts_post(contact_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Contact
        api_response = api_instance.contacts_post(contact_payload, listnames=listnames)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_payload** | [**[ContactPayload]**](ContactPayload.md)|  |
 **listnames** | **[str]**| Names of lists to which the uploaded contacts should be added to | [optional]

### Return type

[**[Contact]**](Contact.md)

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

