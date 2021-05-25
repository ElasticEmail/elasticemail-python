"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    To start using this API, you will need your Access Token (available <a target=\"_blank\" href=\"https://elasticemail.com/account#/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    This is the documentation for REST API. If you’d like to read our legacy documentation regarding Web API v2 click <a target=\"_blank\" href=\"https://api.elasticemail.com/public/help\">here</a>.    Downloadable library clients can be found in our Github repository <a target=\"_blank\" href=\"https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme\">here</a>  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ElasticEmail.api_client import ApiClient, Endpoint as _Endpoint
from ElasticEmail.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ElasticEmail.model.email_data import EmailData
from ElasticEmail.model.email_message_data import EmailMessageData
from ElasticEmail.model.email_send import EmailSend
from ElasticEmail.model.email_transactional_message_data import EmailTransactionalMessageData
from ElasticEmail.model.merge_email_payload import MergeEmailPayload


class EmailsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __emails_by_msgid_view_get(
            self,
            msgid,
            **kwargs
        ):
            """View Email  # noqa: E501

            Returns email details for viewing or rendering. Required Access Level: None  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.emails_by_msgid_view_get(msgid, async_req=True)
            >>> result = thread.get()

            Args:
                msgid (str): Message identifier

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                EmailData
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['msgid'] = \
                msgid
            return self.call_with_http_info(**kwargs)

        self.emails_by_msgid_view_get = _Endpoint(
            settings={
                'response_type': (EmailData,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/emails/{msgid}/view',
                'operation_id': 'emails_by_msgid_view_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'msgid',
                ],
                'required': [
                    'msgid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'msgid':
                        (str,),
                },
                'attribute_map': {
                    'msgid': 'msgid',
                },
                'location_map': {
                    'msgid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__emails_by_msgid_view_get
        )

        def __emails_mergefile_post(
            self,
            merge_email_payload,
            **kwargs
        ):
            """Send Bulk Emails CSV  # noqa: E501

            Send bulk merge email. Required Access Level: SendHttp  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.emails_mergefile_post(merge_email_payload, async_req=True)
            >>> result = thread.get()

            Args:
                merge_email_payload (MergeEmailPayload): Email data

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                EmailSend
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['merge_email_payload'] = \
                merge_email_payload
            return self.call_with_http_info(**kwargs)

        self.emails_mergefile_post = _Endpoint(
            settings={
                'response_type': (EmailSend,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/emails/mergefile',
                'operation_id': 'emails_mergefile_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'merge_email_payload',
                ],
                'required': [
                    'merge_email_payload',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'merge_email_payload':
                        (MergeEmailPayload,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'merge_email_payload': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__emails_mergefile_post
        )

        def __emails_post(
            self,
            email_message_data,
            **kwargs
        ):
            """Send Bulk Emails  # noqa: E501

            Send bulk merge email. Required Access Level: SendHttp  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.emails_post(email_message_data, async_req=True)
            >>> result = thread.get()

            Args:
                email_message_data (EmailMessageData): Email data

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                EmailSend
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['email_message_data'] = \
                email_message_data
            return self.call_with_http_info(**kwargs)

        self.emails_post = _Endpoint(
            settings={
                'response_type': (EmailSend,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/emails',
                'operation_id': 'emails_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'email_message_data',
                ],
                'required': [
                    'email_message_data',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'email_message_data':
                        (EmailMessageData,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'email_message_data': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__emails_post
        )

        def __emails_transactional_post(
            self,
            email_transactional_message_data,
            **kwargs
        ):
            """Send Transactional Email  # noqa: E501

            Send transactional emails (recipients will be known to each other). Required Access Level: SendHttp  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.emails_transactional_post(email_transactional_message_data, async_req=True)
            >>> result = thread.get()

            Args:
                email_transactional_message_data (EmailTransactionalMessageData): Email data

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                EmailSend
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['email_transactional_message_data'] = \
                email_transactional_message_data
            return self.call_with_http_info(**kwargs)

        self.emails_transactional_post = _Endpoint(
            settings={
                'response_type': (EmailSend,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/emails/transactional',
                'operation_id': 'emails_transactional_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'email_transactional_message_data',
                ],
                'required': [
                    'email_transactional_message_data',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'email_transactional_message_data':
                        (EmailTransactionalMessageData,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'email_transactional_message_data': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__emails_transactional_post
        )
