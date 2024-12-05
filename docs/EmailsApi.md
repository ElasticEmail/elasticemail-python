# ElasticEmail.EmailsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emails_by_msgid_view_get**](EmailsApi.md#emails_by_msgid_view_get) | **GET** /emails/{msgid}/view | View Email
[**emails_by_transactionid_status_get**](EmailsApi.md#emails_by_transactionid_status_get) | **GET** /emails/{transactionid}/status | Get Status
[**emails_mergefile_post**](EmailsApi.md#emails_mergefile_post) | **POST** /emails/mergefile | Send Bulk Emails CSV
[**emails_post**](EmailsApi.md#emails_post) | **POST** /emails | Send Bulk Emails
[**emails_transactional_post**](EmailsApi.md#emails_transactional_post) | **POST** /emails/transactional | Send Transactional Email


# **emails_by_msgid_view_get**
> EmailData emails_by_msgid_view_get(msgid)

View Email

Returns email details for viewing or rendering. Required Access Level: None

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.email_data import EmailData
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
    api_instance = ElasticEmail.EmailsApi(api_client)
    msgid = 'msgid_example' # str | Message identifier

    try:
        # View Email
        api_response = api_instance.emails_by_msgid_view_get(msgid)
        print("The response of EmailsApi->emails_by_msgid_view_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->emails_by_msgid_view_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msgid** | **str**| Message identifier | 

### Return type

[**EmailData**](EmailData.md)

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

# **emails_by_transactionid_status_get**
> EmailJobStatus emails_by_transactionid_status_get(transactionid, show_failed=show_failed, show_sent=show_sent, show_delivered=show_delivered, show_pending=show_pending, show_opened=show_opened, show_clicked=show_clicked, show_abuse=show_abuse, show_unsubscribed=show_unsubscribed, show_errors=show_errors, show_message_ids=show_message_ids)

Get Status

Get status details of an email transaction. Required Access Level: ViewReports

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.email_job_status import EmailJobStatus
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
    api_instance = ElasticEmail.EmailsApi(api_client)
    transactionid = 'transactionid_example' # str | Transaction identifier
    show_failed = False # bool | Include Bounced email addresses. (optional) (default to False)
    show_sent = False # bool | Include Sent email addresses. (optional) (default to False)
    show_delivered = False # bool | Include all delivered email addresses. (optional) (default to False)
    show_pending = False # bool | Include Ready to send email addresses. (optional) (default to False)
    show_opened = False # bool | Include Opened email addresses. (optional) (default to False)
    show_clicked = False # bool | Include Clicked email addresses. (optional) (default to False)
    show_abuse = False # bool | Include Reported as abuse email addresses. (optional) (default to False)
    show_unsubscribed = False # bool | Include Unsubscribed email addresses. (optional) (default to False)
    show_errors = False # bool | Include error messages for bounced emails. (optional) (default to False)
    show_message_ids = False # bool | Include all MessageIDs for this transaction (optional) (default to False)

    try:
        # Get Status
        api_response = api_instance.emails_by_transactionid_status_get(transactionid, show_failed=show_failed, show_sent=show_sent, show_delivered=show_delivered, show_pending=show_pending, show_opened=show_opened, show_clicked=show_clicked, show_abuse=show_abuse, show_unsubscribed=show_unsubscribed, show_errors=show_errors, show_message_ids=show_message_ids)
        print("The response of EmailsApi->emails_by_transactionid_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->emails_by_transactionid_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionid** | **str**| Transaction identifier | 
 **show_failed** | **bool**| Include Bounced email addresses. | [optional] [default to False]
 **show_sent** | **bool**| Include Sent email addresses. | [optional] [default to False]
 **show_delivered** | **bool**| Include all delivered email addresses. | [optional] [default to False]
 **show_pending** | **bool**| Include Ready to send email addresses. | [optional] [default to False]
 **show_opened** | **bool**| Include Opened email addresses. | [optional] [default to False]
 **show_clicked** | **bool**| Include Clicked email addresses. | [optional] [default to False]
 **show_abuse** | **bool**| Include Reported as abuse email addresses. | [optional] [default to False]
 **show_unsubscribed** | **bool**| Include Unsubscribed email addresses. | [optional] [default to False]
 **show_errors** | **bool**| Include error messages for bounced emails. | [optional] [default to False]
 **show_message_ids** | **bool**| Include all MessageIDs for this transaction | [optional] [default to False]

### Return type

[**EmailJobStatus**](EmailJobStatus.md)

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

# **emails_mergefile_post**
> EmailSend emails_mergefile_post(merge_email_payload)

Send Bulk Emails CSV

Send to a list of contacts submitted in a CSV data file. The first column in the CSV must be the email address and the CSV must contain a header row. Additional fields can be included with a named header row and can be merged with the template using {merge} tags in the content.                           Example CSV:                           email, firstname, lastname              test1@gmail.com, michael, smith              test2@gmail.com, janet, smith                           Merge file must not be empty. Required Access Level: SendHttp

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.email_send import EmailSend
from ElasticEmail.models.merge_email_payload import MergeEmailPayload
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
    api_instance = ElasticEmail.EmailsApi(api_client)
    merge_email_payload = ElasticEmail.MergeEmailPayload() # MergeEmailPayload | Email data

    try:
        # Send Bulk Emails CSV
        api_response = api_instance.emails_mergefile_post(merge_email_payload)
        print("The response of EmailsApi->emails_mergefile_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->emails_mergefile_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_email_payload** | [**MergeEmailPayload**](MergeEmailPayload.md)| Email data | 

### Return type

[**EmailSend**](EmailSend.md)

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

# **emails_post**
> EmailSend emails_post(email_message_data)

Send Bulk Emails

Send bulk merge email. Required Access Level: SendHttp

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.email_message_data import EmailMessageData
from ElasticEmail.models.email_send import EmailSend
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
    api_instance = ElasticEmail.EmailsApi(api_client)
    email_message_data = ElasticEmail.EmailMessageData() # EmailMessageData | Email data

    try:
        # Send Bulk Emails
        api_response = api_instance.emails_post(email_message_data)
        print("The response of EmailsApi->emails_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->emails_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_message_data** | [**EmailMessageData**](EmailMessageData.md)| Email data | 

### Return type

[**EmailSend**](EmailSend.md)

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

# **emails_transactional_post**
> EmailSend emails_transactional_post(email_transactional_message_data)

Send Transactional Email

Send transactional emails (recipients will be known to each other). Required Access Level: SendHttp

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.email_send import EmailSend
from ElasticEmail.models.email_transactional_message_data import EmailTransactionalMessageData
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
    api_instance = ElasticEmail.EmailsApi(api_client)
    email_transactional_message_data = ElasticEmail.EmailTransactionalMessageData() # EmailTransactionalMessageData | Email data

    try:
        # Send Transactional Email
        api_response = api_instance.emails_transactional_post(email_transactional_message_data)
        print("The response of EmailsApi->emails_transactional_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->emails_transactional_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_transactional_message_data** | [**EmailTransactionalMessageData**](EmailTransactionalMessageData.md)| Email data | 

### Return type

[**EmailSend**](EmailSend.md)

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

