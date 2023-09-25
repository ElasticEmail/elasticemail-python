<a name="__pageTop"></a>
# ElasticEmail.apis.tags.emails_api.EmailsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emails_by_msgid_view_get**](#emails_by_msgid_view_get) | **get** /emails/{msgid}/view | View Email
[**emails_mergefile_post**](#emails_mergefile_post) | **post** /emails/mergefile | Send Bulk Emails CSV
[**emails_post**](#emails_post) | **post** /emails | Send Bulk Emails
[**emails_transactional_post**](#emails_transactional_post) | **post** /emails/transactional | Send Transactional Email

# **emails_by_msgid_view_get**
<a name="emails_by_msgid_view_get"></a>
> EmailData emails_by_msgid_view_get(msgid)

View Email

Returns email details for viewing or rendering. Required Access Level: None

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import emails_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'msgid': "msgid_example",
    }
    try:
        # View Email
        api_response = api_instance.emails_by_msgid_view_get(
            path_params=path_params,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_by_msgid_view_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
msgid | MsgidSchema | | 

# MsgidSchema

string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | string | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#emails_by_msgid_view_get.ApiResponseFor200) | OK

#### emails_by_msgid_view_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailData**](../../models/EmailData.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **emails_mergefile_post**
<a name="emails_mergefile_post"></a>
> EmailSend emails_mergefile_post(merge_email_payload)

Send Bulk Emails CSV

Send bulk merge email. Required Access Level: SendHttp

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import emails_api
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

    # example passing only required values which don't have defaults set
    body = MergeEmailPayload(
        merge_file=MessageAttachment(
            binary_content='YQ==',
            name="name_example",
            content_type="content_type_example",
            size=100,
        ),
        content=EmailContent(
            body=[
                BodyPart(
                    content_type=BodyContentType("HTML"),
                    content="content_example",
                    charset="charset_example",
                )
            ],
            merge=dict(
                "key": "key_example",
            ),
            attachments=[
                MessageAttachment()
            ],
            headers=dict(
                "key": "key_example",
            ),
            postback="postback_example",
            envelope_from="John Doe <email@domain.com>",
            _from="John Doe <email@domain.com>",
            reply_to="John Doe <email@domain.com>",
            subject="Hello!",
            template_name="Template01",
            attach_files=[
                "[ \"preuploaded.jpg\" ]"
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
    )
    try:
        # Send Bulk Emails CSV
        api_response = api_instance.emails_mergefile_post(
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_mergefile_post: %s\n" % e)
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
[**MergeEmailPayload**](../../models/MergeEmailPayload.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#emails_mergefile_post.ApiResponseFor200) | OK

#### emails_mergefile_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailSend**](../../models/EmailSend.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **emails_post**
<a name="emails_post"></a>
> EmailSend emails_post(email_message_data)

Send Bulk Emails

Send bulk merge email. Required Access Level: SendHttp

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import emails_api
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

    # example passing only required values which don't have defaults set
    body = EmailMessageData(
        recipients=[
            EmailRecipient(
                email="mail@example.com",
                fields=dict(
                    "key": "key_example",
                ),
            )
        ],
        content=EmailContent(
            body=[
                BodyPart(
                    content_type=BodyContentType("HTML"),
                    content="content_example",
                    charset="charset_example",
                )
            ],
            merge=dict(
                "key": "key_example",
            ),
            attachments=[
                MessageAttachment(
                    binary_content='YQ==',
                    name="name_example",
                    content_type="content_type_example",
                    size=100,
                )
            ],
            headers=dict(
                "key": "key_example",
            ),
            postback="postback_example",
            envelope_from="John Doe <email@domain.com>",
            _from="John Doe <email@domain.com>",
            reply_to="John Doe <email@domain.com>",
            subject="Hello!",
            template_name="Template01",
            attach_files=[
                "[ \"preuploaded.jpg\" ]"
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
    )
    try:
        # Send Bulk Emails
        api_response = api_instance.emails_post(
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_post: %s\n" % e)
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
[**EmailMessageData**](../../models/EmailMessageData.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#emails_post.ApiResponseFor200) | OK

#### emails_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailSend**](../../models/EmailSend.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **emails_transactional_post**
<a name="emails_transactional_post"></a>
> EmailSend emails_transactional_post(email_transactional_message_data)

Send Transactional Email

Send transactional emails (recipients will be known to each other). Required Access Level: SendHttp

### Example

* Api Key Authentication (apikey):
```python
import ElasticEmail
from ElasticEmail.apis.tags import emails_api
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

    # example passing only required values which don't have defaults set
    body = EmailTransactionalMessageData(
        recipients=TransactionalRecipient(
            to=[
                "to_example"
            ],
            cc=[
                "cc_example"
            ],
            bcc=[
                "bcc_example"
            ],
        ),
        content=EmailContent(
            body=[
                BodyPart(
                    content_type=BodyContentType("HTML"),
                    content="content_example",
                    charset="charset_example",
                )
            ],
            merge=dict(
                "key": "key_example",
            ),
            attachments=[
                MessageAttachment(
                    binary_content='YQ==',
                    name="name_example",
                    content_type="content_type_example",
                    size=100,
                )
            ],
            headers=dict(
                "key": "key_example",
            ),
            postback="postback_example",
            envelope_from="John Doe <email@domain.com>",
            _from="John Doe <email@domain.com>",
            reply_to="John Doe <email@domain.com>",
            subject="Hello!",
            template_name="Template01",
            attach_files=[
                "[ \"preuploaded.jpg\" ]"
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
    )
    try:
        # Send Transactional Email
        api_response = api_instance.emails_transactional_post(
            body=body,
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_transactional_post: %s\n" % e)
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
[**EmailTransactionalMessageData**](../../models/EmailTransactionalMessageData.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#emails_transactional_post.ApiResponseFor200) | OK

#### emails_transactional_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailSend**](../../models/EmailSend.md) |  | 


### Authorization

[apikey](../../../README.md#apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

