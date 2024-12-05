# ElasticEmail.CampaignsApi

All URIs are relative to *https://api.elasticemail.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**campaigns_by_name_delete**](CampaignsApi.md#campaigns_by_name_delete) | **DELETE** /campaigns/{name} | Delete Campaign
[**campaigns_by_name_get**](CampaignsApi.md#campaigns_by_name_get) | **GET** /campaigns/{name} | Load Campaign
[**campaigns_by_name_pause_put**](CampaignsApi.md#campaigns_by_name_pause_put) | **PUT** /campaigns/{name}/pause | Pause Campaign
[**campaigns_by_name_put**](CampaignsApi.md#campaigns_by_name_put) | **PUT** /campaigns/{name} | Update Campaign
[**campaigns_get**](CampaignsApi.md#campaigns_get) | **GET** /campaigns | Load Campaigns
[**campaigns_post**](CampaignsApi.md#campaigns_post) | **POST** /campaigns | Add Campaign


# **campaigns_by_name_delete**
> campaigns_by_name_delete(name)

Delete Campaign

Delete the specific campaign.  This does not cancel in progress email, see Cancel In Progress. Required Access Level: ModifyCampaigns

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
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
    api_instance = ElasticEmail.CampaignsApi(api_client)
    name = 'name_example' # str | Name of Campaign to delete

    try:
        # Delete Campaign
        api_instance.campaigns_by_name_delete(name)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of Campaign to delete | 

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

# **campaigns_by_name_get**
> Campaign campaigns_by_name_get(name)

Load Campaign

Returns the specified campaign details. Required Access Level: ViewCampaigns

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.campaign import Campaign
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
    api_instance = ElasticEmail.CampaignsApi(api_client)
    name = 'name_example' # str | Name of Campaign to get

    try:
        # Load Campaign
        api_response = api_instance.campaigns_by_name_get(name)
        print("The response of CampaignsApi->campaigns_by_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of Campaign to get | 

### Return type

[**Campaign**](Campaign.md)

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

# **campaigns_by_name_pause_put**
> campaigns_by_name_pause_put(name)

Pause Campaign

Pauses the specific campaign, cancelling emails that are waiting to be sent. Required Access Level: ModifyCampaigns

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
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
    api_instance = ElasticEmail.CampaignsApi(api_client)
    name = 'name_example' # str | Name of Campaign to pause

    try:
        # Pause Campaign
        api_instance.campaigns_by_name_pause_put(name)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_pause_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of Campaign to pause | 

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

# **campaigns_by_name_put**
> Campaign campaigns_by_name_put(name, campaign)

Update Campaign

Updates a previously added campaign.  Only Active and Paused campaigns can be updated. Required Access Level: ModifyCampaigns

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.campaign import Campaign
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
    api_instance = ElasticEmail.CampaignsApi(api_client)
    name = 'name_example' # str | Name of Campaign to update
    campaign = ElasticEmail.Campaign() # Campaign | JSON representation of a campaign

    try:
        # Update Campaign
        api_response = api_instance.campaigns_by_name_put(name, campaign)
        print("The response of CampaignsApi->campaigns_by_name_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of Campaign to update | 
 **campaign** | [**Campaign**](Campaign.md)| JSON representation of a campaign | 

### Return type

[**Campaign**](Campaign.md)

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

# **campaigns_get**
> List[Campaign] campaigns_get(search=search, offset=offset, limit=limit)

Load Campaigns

Returns a list all of your campaigns. Limited to 1000 results. Required Access Level: ViewCampaigns

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.campaign import Campaign
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
    api_instance = ElasticEmail.CampaignsApi(api_client)
    search = 'search_example' # str | Text fragment used for searching in Campaign name (using the 'contains' rule) (optional)
    offset = 20 # int | How many items should be returned ahead. (optional)
    limit = 100 # int | Maximum number of returned items. (optional)

    try:
        # Load Campaigns
        api_response = api_instance.campaigns_get(search=search, offset=offset, limit=limit)
        print("The response of CampaignsApi->campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Text fragment used for searching in Campaign name (using the &#39;contains&#39; rule) | [optional] 
 **offset** | **int**| How many items should be returned ahead. | [optional] 
 **limit** | **int**| Maximum number of returned items. | [optional] 

### Return type

[**List[Campaign]**](Campaign.md)

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

# **campaigns_post**
> Campaign campaigns_post(campaign)

Add Campaign

Add a campaign for processing. Required Access Level: ModifyCampaigns

### Example

* Api Key Authentication (apikey):

```python
import ElasticEmail
from ElasticEmail.models.campaign import Campaign
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
    api_instance = ElasticEmail.CampaignsApi(api_client)
    campaign = ElasticEmail.Campaign() # Campaign | JSON representation of a campaign

    try:
        # Add Campaign
        api_response = api_instance.campaigns_post(campaign)
        print("The response of CampaignsApi->campaigns_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | [**Campaign**](Campaign.md)| JSON representation of a campaign | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

