# ElasticEmail.model.inbound_route.InboundRoute

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**PublicId** | str,  | str,  |  | [optional] 
**Name** | str,  | str,  | Name of this route | [optional] 
**FilterType** | [**InboundRouteFilterType**](InboundRouteFilterType.md) | [**InboundRouteFilterType**](InboundRouteFilterType.md) |  | [optional] 
**Filter** | str,  | str,  | Filter of the inbound data | [optional] 
**ActionType** | [**InboundRouteActionType**](InboundRouteActionType.md) | [**InboundRouteActionType**](InboundRouteActionType.md) |  | [optional] 
**ActionParameter** | str,  | str,  | URL address or Email to notify about the inbound | [optional] 
**SortOrder** | decimal.Decimal, int,  | decimal.Decimal,  | Place of this route in your routes queue&#x27;s order | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

