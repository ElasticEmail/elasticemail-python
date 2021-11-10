"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.    To start using this API, you will need your Access Token (available <a target=\"_blank\" href=\"https://elasticemail.com/account#/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    This is the documentation for REST API. If you’d like to read our legacy documentation regarding Web API v2 click <a target=\"_blank\" href=\"https://api.elasticemail.com/public/help\">here</a>.    Downloadable library clients can be found in our Github repository <a target=\"_blank\" href=\"https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme\">here</a>  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ElasticEmail.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from ElasticEmail.exceptions import ApiAttributeError



class ChannelLogStatusSummary(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'channel_name': (str,),  # noqa: E501
            'recipients': (int,),  # noqa: E501
            'email_total': (int,),  # noqa: E501
            'sms_total': (int,),  # noqa: E501
            'delivered': (int,),  # noqa: E501
            'bounced': (int,),  # noqa: E501
            'in_progress': (int,),  # noqa: E501
            'opened': (int,),  # noqa: E501
            'clicked': (int,),  # noqa: E501
            'unsubscribed': (int,),  # noqa: E501
            'complaints': (int,),  # noqa: E501
            'inbound': (int,),  # noqa: E501
            'manual_cancel': (int,),  # noqa: E501
            'not_delivered': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'channel_name': 'ChannelName',  # noqa: E501
        'recipients': 'Recipients',  # noqa: E501
        'email_total': 'EmailTotal',  # noqa: E501
        'sms_total': 'SmsTotal',  # noqa: E501
        'delivered': 'Delivered',  # noqa: E501
        'bounced': 'Bounced',  # noqa: E501
        'in_progress': 'InProgress',  # noqa: E501
        'opened': 'Opened',  # noqa: E501
        'clicked': 'Clicked',  # noqa: E501
        'unsubscribed': 'Unsubscribed',  # noqa: E501
        'complaints': 'Complaints',  # noqa: E501
        'inbound': 'Inbound',  # noqa: E501
        'manual_cancel': 'ManualCancel',  # noqa: E501
        'not_delivered': 'NotDelivered',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ChannelLogStatusSummary - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            channel_name (str): Channel name. [optional]  # noqa: E501
            recipients (int): Number of recipients. [optional]  # noqa: E501
            email_total (int): Number of emails. [optional]  # noqa: E501
            sms_total (int): Number of SMS. [optional]  # noqa: E501
            delivered (int): Number of delivered messages. [optional]  # noqa: E501
            bounced (int): Number of bounced messages. [optional]  # noqa: E501
            in_progress (int): Number of messages in progress. [optional]  # noqa: E501
            opened (int): Number of opened messages. [optional]  # noqa: E501
            clicked (int): Number of clicked messages. [optional]  # noqa: E501
            unsubscribed (int): Number of unsubscribed messages. [optional]  # noqa: E501
            complaints (int): Number of complaint messages. [optional]  # noqa: E501
            inbound (int): Number of inbound messages. [optional]  # noqa: E501
            manual_cancel (int): Number of manually cancelled messages. [optional]  # noqa: E501
            not_delivered (int): Number of messages flagged with 'Not Delivered'. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', False)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ChannelLogStatusSummary - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            channel_name (str): Channel name. [optional]  # noqa: E501
            recipients (int): Number of recipients. [optional]  # noqa: E501
            email_total (int): Number of emails. [optional]  # noqa: E501
            sms_total (int): Number of SMS. [optional]  # noqa: E501
            delivered (int): Number of delivered messages. [optional]  # noqa: E501
            bounced (int): Number of bounced messages. [optional]  # noqa: E501
            in_progress (int): Number of messages in progress. [optional]  # noqa: E501
            opened (int): Number of opened messages. [optional]  # noqa: E501
            clicked (int): Number of clicked messages. [optional]  # noqa: E501
            unsubscribed (int): Number of unsubscribed messages. [optional]  # noqa: E501
            complaints (int): Number of complaint messages. [optional]  # noqa: E501
            inbound (int): Number of inbound messages. [optional]  # noqa: E501
            manual_cancel (int): Number of manually cancelled messages. [optional]  # noqa: E501
            not_delivered (int): Number of messages flagged with 'Not Delivered'. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', False)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
