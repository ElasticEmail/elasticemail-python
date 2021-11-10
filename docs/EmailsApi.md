# ElasticEmail.EmailsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emails_by_msgid_view_get**](EmailsApi.md#emails_by_msgid_view_get) | **GET** /emails/{msgid}/view | View Email
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
import time
import ElasticEmail
from ElasticEmail.api import emails_api
from ElasticEmail.model.email_data import EmailData
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
    api_instance = emails_api.EmailsApi(api_client)
    msgid = "msgid_example" # str | Message identifier

    # example passing only required values which don't have defaults set
    try:
        # View Email
        api_response = api_instance.emails_by_msgid_view_get(msgid)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
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

# **emails_mergefile_post**
> EmailSend emails_mergefile_post(merge_email_payload)

Send Bulk Emails CSV

Send bulk merge email. Required Access Level: SendHttp

### Example

* Api Key Authentication (apikey):

```python
import time
import ElasticEmail
from ElasticEmail.api import emails_api
from ElasticEmail.model.email_send import EmailSend
from ElasticEmail.model.merge_email_payload import MergeEmailPayload
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
    api_instance = emails_api.EmailsApi(api_client)
    merge_email_payload = MergeEmailPayload(
        merge_file=MessageAttachment(
            binary_content='YQ==',
            name="name_example",
            content_type="content_type_example",
        ),
        content=EmailContent(
            body=[
                BodyPart(
                    content_type=BodyContentType("HTML"),
                    content="content_example",
                    charset="charset_example",
                ),
            ],
            merge={
                "key": "key_example",
            },
            attachments=[
                MessageAttachment(
                    binary_content='YQ==',
                    name="name_example",
                    content_type="content_type_example",
                ),
            ],
            headers={
                "key": "key_example",
            },
            postback="postback_example",
            envelope_from="John Doe <email@domain.com>",
            _from="John Doe <email@domain.com>",
            reply_to="John Doe <email@domain.com>",
            subject="Hello!",
            template_name="Template01",
            attach_files=[
                "[ "preuploaded.jpg" ]",
            ],
            utm=Utm(
                source="source_example",
                medium="medium_example",
                campaign="campaign_example",
                content="content_example",
            ),
        ),
        options=Options(
            time_offset=1,
            pool_name="My Custom Pool",
            channel_name="Channel01",
            encoding=EncodingType("UserProvided"),
            track_opens=True,
            track_clicks=True,
        ),
    ) # MergeEmailPayload | Email data

    # example passing only required values which don't have defaults set
    try:
        # Send Bulk Emails CSV
        api_response = api_instance.emails_mergefile_post(merge_email_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
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
import time
import ElasticEmail
from ElasticEmail.api import emails_api
from ElasticEmail.model.email_send import EmailSend
from ElasticEmail.model.email_message_data import EmailMessageData
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
    api_instance = emails_api.EmailsApi(api_client)
    email_message_data = EmailMessageData(
        recipients=[
            EmailRecipient(
                email="mail@example.com",
                fields={
                    "key": "key_example",
                },
            ),
        ],
        content=EmailContent(
            body=[
                BodyPart(
                    content_type=BodyContentType("HTML"),
                    content="content_example",
                    charset="charset_example",
                ),
            ],
            merge={
                "key": "key_example",
            },
            attachments=[
                MessageAttachment(
                    binary_content='YQ==',
                    name="name_example",
                    content_type="content_type_example",
                ),
            ],
            headers={
                "key": "key_example",
            },
            postback="postback_example",
            envelope_from="John Doe <email@domain.com>",
            _from="John Doe <email@domain.com>",
            reply_to="John Doe <email@domain.com>",
            subject="Hello!",
            template_name="Template01",
            attach_files=[
                "[ "preuploaded.jpg" ]",
            ],
            utm=Utm(
                source="source_example",
                medium="medium_example",
                campaign="campaign_example",
                content="content_example",
            ),
        ),
        options=Options(
            time_offset=1,
            pool_name="My Custom Pool",
            channel_name="Channel01",
            encoding=EncodingType("UserProvided"),
            track_opens=True,
            track_clicks=True,
        ),
    ) # EmailMessageData | Email data

    # example passing only required values which don't have defaults set
    try:
        # Send Bulk Emails
        api_response = api_instance.emails_post(email_message_data)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
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
import time
import ElasticEmail
from ElasticEmail.api import emails_api
from ElasticEmail.model.email_send import EmailSend
from ElasticEmail.model.email_transactional_message_data import EmailTransactionalMessageData
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
    api_instance = emails_api.EmailsApi(api_client)
    email_transactional_message_data = EmailTransactionalMessageData(
        recipients=TransactionalRecipient(
            to=[
                "to_example",
            ],
            cc=[
                "cc_example",
            ],
            bcc=[
                "bcc_example",
            ],
        ),
        content=EmailContent(
            body=[
                BodyPart(
                    content_type=BodyContentType("HTML"),
                    content="content_example",
                    charset="charset_example",
                ),
            ],
            merge={
                "key": "key_example",
            },
            attachments=[
                MessageAttachment(
                    binary_content='YQ==',
                    name="name_example",
                    content_type="content_type_example",
                ),
            ],
            headers={
                "key": "key_example",
            },
            postback="postback_example",
            envelope_from="John Doe <email@domain.com>",
            _from="John Doe <email@domain.com>",
            reply_to="John Doe <email@domain.com>",
            subject="Hello!",
            template_name="Template01",
            attach_files=[
                "[ "preuploaded.jpg" ]",
            ],
            utm=Utm(
                source="source_example",
                medium="medium_example",
                campaign="campaign_example",
                content="content_example",
            ),
        ),
        options=Options(
            time_offset=1,
            pool_name="My Custom Pool",
            channel_name="Channel01",
            encoding=EncodingType("UserProvided"),
            track_opens=True,
            track_clicks=True,
        ),
    ) # EmailTransactionalMessageData | Email data

    # example passing only required values which don't have defaults set
    try:
        # Send Transactional Email
        api_response = api_instance.emails_transactional_post(email_transactional_message_data)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
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

