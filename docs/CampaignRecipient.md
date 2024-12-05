# CampaignRecipient

A set of lists and segments names to read recipients from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_names** | **List[str]** | Names of lists from your Account to read recipients from | [optional] 
**segment_names** | **List[str]** | Names of segments from your Account to read recipients from | [optional] 

## Example

```python
from ElasticEmail.models.campaign_recipient import CampaignRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRecipient from a JSON string
campaign_recipient_instance = CampaignRecipient.from_json(json)
# print the JSON string representation of the object
print(CampaignRecipient.to_json())

# convert the object into a dict
campaign_recipient_dict = campaign_recipient_instance.to_dict()
# create an instance of CampaignRecipient from a dict
campaign_recipient_from_dict = CampaignRecipient.from_dict(campaign_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


