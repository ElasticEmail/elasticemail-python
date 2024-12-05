# ElasticEmail.StatisticsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_campaigns_by_name_get**](StatisticsApi.md#statistics_campaigns_by_name_get) | **GET** /statistics/campaigns/{name} | Load Campaign Stats
[**statistics_campaigns_get**](StatisticsApi.md#statistics_campaigns_get) | **GET** /statistics/campaigns | Load Campaigns Stats
[**statistics_channels_by_name_get**](StatisticsApi.md#statistics_channels_by_name_get) | **GET** /statistics/channels/{name} | Load Channel Stats
[**statistics_channels_get**](StatisticsApi.md#statistics_channels_get) | **GET** /statistics/channels | Load Channels Stats
[**statistics_get**](StatisticsApi.md#statistics_get) | **GET** /statistics | Load Statistics


# **statistics_campaigns_by_name_get**
> ChannelLogStatusSummary statistics_campaigns_by_name_get(name)

Load Campaign Stats

Retrieve stats of an existing campaign. Required Access Level: ViewChannels

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.channel_log_status_summary import ChannelLogStatusSummary
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
    api_instance = ElasticEmail.StatisticsApi(api_client)
    name = 'name_example' # str | The name of the campaign to get.

    try:
        # Load Campaign Stats
        api_response = api_instance.statistics_campaigns_by_name_get(name)
        print("The response of StatisticsApi->statistics_campaigns_by_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->statistics_campaigns_by_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the campaign to get. | 

### Return type

[**ChannelLogStatusSummary**](ChannelLogStatusSummary.md)

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

# **statistics_campaigns_get**
> List[ChannelLogStatusSummary] statistics_campaigns_get(limit=limit, offset=offset)

Load Campaigns Stats

Returns a list of your Campaigns' stats. Required Access Level: ViewChannels

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.channel_log_status_summary import ChannelLogStatusSummary
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
    api_instance = ElasticEmail.StatisticsApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Load Campaigns Stats
        api_response = api_instance.statistics_campaigns_get(limit=limit, offset=offset)
        print("The response of StatisticsApi->statistics_campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->statistics_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[ChannelLogStatusSummary]**](ChannelLogStatusSummary.md)

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

# **statistics_channels_by_name_get**
> ChannelLogStatusSummary statistics_channels_by_name_get(name)

Load Channel Stats

Retrieve an existing channel stats. Required Access Level: ViewChannels

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.channel_log_status_summary import ChannelLogStatusSummary
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
    api_instance = ElasticEmail.StatisticsApi(api_client)
    name = 'name_example' # str | The name of the channel to get.

    try:
        # Load Channel Stats
        api_response = api_instance.statistics_channels_by_name_get(name)
        print("The response of StatisticsApi->statistics_channels_by_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->statistics_channels_by_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the channel to get. | 

### Return type

[**ChannelLogStatusSummary**](ChannelLogStatusSummary.md)

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

# **statistics_channels_get**
> List[ChannelLogStatusSummary] statistics_channels_get(limit=limit, offset=offset)

Load Channels Stats

Returns a list of your Channels' stats. Required Access Level: ViewChannels

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.channel_log_status_summary import ChannelLogStatusSummary
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
    api_instance = ElasticEmail.StatisticsApi(api_client)
    limit = 100 # int | Maximum number of returned items. (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)

    try:
        # Load Channels Stats
        api_response = api_instance.statistics_channels_get(limit=limit, offset=offset)
        print("The response of StatisticsApi->statistics_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->statistics_channels_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of returned items. | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 

### Return type

[**List[ChannelLogStatusSummary]**](ChannelLogStatusSummary.md)

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

# **statistics_get**
> LogStatusSummary statistics_get(var_from, to=to)

Load Statistics

Returns basic statistics. Required Access Level: ViewReports

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.log_status_summary import LogStatusSummary
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
    api_instance = ElasticEmail.StatisticsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Starting date for search in YYYY-MM-DDThh:mm:ss format.
    to = '2013-10-20T19:20:30+01:00' # datetime | Ending date for search in YYYY-MM-DDThh:mm:ss format. (optional)

    try:
        # Load Statistics
        api_response = api_instance.statistics_get(var_from, to=to)
        print("The response of StatisticsApi->statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->statistics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Starting date for search in YYYY-MM-DDThh:mm:ss format. | 
 **to** | **datetime**| Ending date for search in YYYY-MM-DDThh:mm:ss format. | [optional] 

### Return type

[**LogStatusSummary**](LogStatusSummary.md)

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

