# Campaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[CampaignTemplate]**](CampaignTemplate.md) | Campaign&#39;s email content. Provide multiple items to send an A/X Split Campaign | [optional] 
**name** | **str** | Campaign name | 
**status** | [**CampaignStatus**](CampaignStatus.md) |  | [optional] 
**recipients** | [**CampaignRecipient**](CampaignRecipient.md) |  | 
**options** | [**CampaignOptions**](CampaignOptions.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print(Campaign.to_json())

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_from_dict = Campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


