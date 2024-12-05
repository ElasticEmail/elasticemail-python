# CampaignOptions

Different send options for a Campaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_optimization** | [**DeliveryOptimizationType**](DeliveryOptimizationType.md) |  | [optional] 
**track_opens** | **bool** | Should the opens be tracked? If no value has been provided, Account&#39;s default setting will be used. | [optional] 
**track_clicks** | **bool** | Should the clicks be tracked? If no value has been provided, Account&#39;s default setting will be used. | [optional] 
**schedule_for** | **datetime** | Date when this Campaign is scheduled to be sent on | [optional] 
**trigger_frequency** | **float** | How often (in minutes) to send the campaign | [optional] 
**trigger_count** | **int** | How many times send the campaign | [optional] 
**split_options** | [**SplitOptions**](SplitOptions.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.campaign_options import CampaignOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignOptions from a JSON string
campaign_options_instance = CampaignOptions.from_json(json)
# print the JSON string representation of the object
print(CampaignOptions.to_json())

# convert the object into a dict
campaign_options_dict = campaign_options_instance.to_dict()
# create an instance of CampaignOptions from a dict
campaign_options_from_dict = CampaignOptions.from_dict(campaign_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


