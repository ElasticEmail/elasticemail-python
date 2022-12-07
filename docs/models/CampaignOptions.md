# ElasticEmail.model.campaign_options.CampaignOptions

Different send options for a Campaign

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Different send options for a Campaign | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**DeliveryOptimization** | [**DeliveryOptimizationType**](DeliveryOptimizationType.md) | [**DeliveryOptimizationType**](DeliveryOptimizationType.md) |  | [optional] 
**TrackOpens** | None, bool,  | NoneClass, BoolClass,  | Should the opens be tracked? If no value has been provided, Account&#x27;s default setting will be used. | [optional] 
**TrackClicks** | None, bool,  | NoneClass, BoolClass,  | Should the clicks be tracked? If no value has been provided, Account&#x27;s default setting will be used. | [optional] 
**ScheduleFor** | None, str, datetime,  | NoneClass, str,  | Date when this Campaign is scheduled to be sent on | [optional] value must conform to RFC-3339 date-time
**SplitOptions** | [**SplitOptions**](SplitOptions.md) | [**SplitOptions**](SplitOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

