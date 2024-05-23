# ElasticEmail.model.campaign.Campaign

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Recipients** | [**CampaignRecipient**](CampaignRecipient.md) | [**CampaignRecipient**](CampaignRecipient.md) |  | 
**Name** | str,  | str,  | Campaign name | 
**[Content](#Content)** | list, tuple,  | tuple,  | Campaign&#x27;s email content. Provide multiple items to send an A/X Split Campaign | [optional] 
**Status** | [**CampaignStatus**](CampaignStatus.md) | [**CampaignStatus**](CampaignStatus.md) |  | [optional] 
**Options** | [**CampaignOptions**](CampaignOptions.md) | [**CampaignOptions**](CampaignOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Content

Campaign's email content. Provide multiple items to send an A/X Split Campaign

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Campaign&#x27;s email content. Provide multiple items to send an A/X Split Campaign | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CampaignTemplate**](CampaignTemplate.md) | [**CampaignTemplate**](CampaignTemplate.md) | [**CampaignTemplate**](CampaignTemplate.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

