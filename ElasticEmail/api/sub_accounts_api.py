"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    To start using this API, you will need your Access Token (available <a href=\"https://elasticemail.com/account#/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    This is the documentation for REST API. If you’d like to read our legacy documentation regarding Web API v2 click <a href=\"https://api.elasticemail.com/public/help\">here</a>.  # noqa: E501

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
from ElasticEmail.model.sub_account_info import SubAccountInfo
from ElasticEmail.model.subaccount_email_credits_payload import SubaccountEmailCreditsPayload
from ElasticEmail.model.subaccount_email_settings import SubaccountEmailSettings
from ElasticEmail.model.subaccount_payload import SubaccountPayload


class SubAccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __subaccounts_by_email_credits_patch(
            self,
            email,
            subaccount_email_credits_payload,
            **kwargs
        ):
            """Add, Subtract Email Credits  # noqa: E501

            Update email credits of a subaccount by the given amount. Required Access Level: ModifySubAccounts  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.subaccounts_by_email_credits_patch(email, subaccount_email_credits_payload, async_req=True)
            >>> result = thread.get()

            Args:
                email (str): Email address of Sub-Account
                subaccount_email_credits_payload (SubaccountEmailCreditsPayload): Amount of email credits to add or subtract from the current SubAccount email credits pool (positive or negative value)

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
                None
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
            kwargs['email'] = \
                email
            kwargs['subaccount_email_credits_payload'] = \
                subaccount_email_credits_payload
            return self.call_with_http_info(**kwargs)

        self.subaccounts_by_email_credits_patch = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/subaccounts/{email}/credits',
                'operation_id': 'subaccounts_by_email_credits_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'email',
                    'subaccount_email_credits_payload',
                ],
                'required': [
                    'email',
                    'subaccount_email_credits_payload',
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
                    'email':
                        (str,),
                    'subaccount_email_credits_payload':
                        (SubaccountEmailCreditsPayload,),
                },
                'attribute_map': {
                    'email': 'email',
                },
                'location_map': {
                    'email': 'path',
                    'subaccount_email_credits_payload': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__subaccounts_by_email_credits_patch
        )

        def __subaccounts_by_email_delete(
            self,
            email,
            **kwargs
        ):
            """Delete SubAccount  # noqa: E501

            Deletes specified SubAccount. An email will be sent to confirm this change. Required Access Level: ModifySubAccounts  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.subaccounts_by_email_delete(email, async_req=True)
            >>> result = thread.get()

            Args:
                email (str): Email address of Sub-Account

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
                None
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
            kwargs['email'] = \
                email
            return self.call_with_http_info(**kwargs)

        self.subaccounts_by_email_delete = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/subaccounts/{email}',
                'operation_id': 'subaccounts_by_email_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'email',
                ],
                'required': [
                    'email',
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
                    'email':
                        (str,),
                },
                'attribute_map': {
                    'email': 'email',
                },
                'location_map': {
                    'email': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__subaccounts_by_email_delete
        )

        def __subaccounts_by_email_get(
            self,
            email,
            **kwargs
        ):
            """Load SubAccount  # noqa: E501

            Returns details for the specified SubAccount. Required Access Level: ViewSubAccounts  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.subaccounts_by_email_get(email, async_req=True)
            >>> result = thread.get()

            Args:
                email (str): Email address of Sub-Account

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
                SubAccountInfo
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
            kwargs['email'] = \
                email
            return self.call_with_http_info(**kwargs)

        self.subaccounts_by_email_get = _Endpoint(
            settings={
                'response_type': (SubAccountInfo,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/subaccounts/{email}',
                'operation_id': 'subaccounts_by_email_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'email',
                ],
                'required': [
                    'email',
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
                    'email':
                        (str,),
                },
                'attribute_map': {
                    'email': 'email',
                },
                'location_map': {
                    'email': 'path',
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
            callable=__subaccounts_by_email_get
        )

        def __subaccounts_by_email_settings_email_put(
            self,
            email,
            subaccount_email_settings,
            **kwargs
        ):
            """Update SubAccount Email Settings  # noqa: E501

            Update SubAccount email settings. Required Access Level: ModifySubAccounts  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.subaccounts_by_email_settings_email_put(email, subaccount_email_settings, async_req=True)
            >>> result = thread.get()

            Args:
                email (str):
                subaccount_email_settings (SubaccountEmailSettings): Updated Email Settings

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
                SubaccountEmailSettings
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
            kwargs['email'] = \
                email
            kwargs['subaccount_email_settings'] = \
                subaccount_email_settings
            return self.call_with_http_info(**kwargs)

        self.subaccounts_by_email_settings_email_put = _Endpoint(
            settings={
                'response_type': (SubaccountEmailSettings,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/subaccounts/{email}/settings/email',
                'operation_id': 'subaccounts_by_email_settings_email_put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'email',
                    'subaccount_email_settings',
                ],
                'required': [
                    'email',
                    'subaccount_email_settings',
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
                    'email':
                        (str,),
                    'subaccount_email_settings':
                        (SubaccountEmailSettings,),
                },
                'attribute_map': {
                    'email': 'email',
                },
                'location_map': {
                    'email': 'path',
                    'subaccount_email_settings': 'body',
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
            callable=__subaccounts_by_email_settings_email_put
        )

        def __subaccounts_get(
            self,
            **kwargs
        ):
            """Load SubAccounts  # noqa: E501

            Returns a list of all your SubAccounts. Required Access Level: ViewSubAccounts  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.subaccounts_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                limit (int): Maximum number of returned items.. [optional]
                offset (int): How many items should be returned ahead.. [optional]
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
                [SubAccountInfo]
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
            return self.call_with_http_info(**kwargs)

        self.subaccounts_get = _Endpoint(
            settings={
                'response_type': ([SubAccountInfo],),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/subaccounts',
                'operation_id': 'subaccounts_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'offset',
                ],
                'required': [],
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
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'limit': 'query',
                    'offset': 'query',
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
            callable=__subaccounts_get
        )

        def __subaccounts_post(
            self,
            subaccount_payload,
            **kwargs
        ):
            """Add SubAccount  # noqa: E501

            Add a new SubAccount to your Account. To receive an access token for this SubAccount, make a POST security/apikeys request using the 'subaccount' parameter. Required Access Level: ModifySubAccounts  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.subaccounts_post(subaccount_payload, async_req=True)
            >>> result = thread.get()

            Args:
                subaccount_payload (SubaccountPayload):

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
                SubAccountInfo
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
            kwargs['subaccount_payload'] = \
                subaccount_payload
            return self.call_with_http_info(**kwargs)

        self.subaccounts_post = _Endpoint(
            settings={
                'response_type': (SubAccountInfo,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/subaccounts',
                'operation_id': 'subaccounts_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'subaccount_payload',
                ],
                'required': [
                    'subaccount_payload',
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
                    'subaccount_payload':
                        (SubaccountPayload,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'subaccount_payload': 'body',
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
            callable=__subaccounts_post
        )
