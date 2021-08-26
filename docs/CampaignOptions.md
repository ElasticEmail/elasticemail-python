# CampaignOptions

Different send options for a Campaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_optimization** | **dict** | How to order email delivery - by recipients&#39; engagement score or by the time they open the most of the emails that were sent to them | [optional] 
**track_opens** | **bool, none_type** | Should the opens be tracked? If no value has been provided, Account&#39;s default setting will be used. | [optional] 
**track_clicks** | **bool, none_type** | Should the clicks be tracked? If no value has been provided, Account&#39;s default setting will be used. | [optional] 
**schedule_for** | **datetime, none_type** | Date when this Campaign is scheduled to be sent on | [optional] 
**split_options** | **dict** | Optional options for A/X split campaigns. Will be ignored if only one template content was provided | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


