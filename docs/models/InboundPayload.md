# ElasticEmail.model.inbound_payload.InboundPayload

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**FilterType** | [**InboundRouteFilterType**](InboundRouteFilterType.md) | [**InboundRouteFilterType**](InboundRouteFilterType.md) |  | 
**ActionType** | [**InboundRouteActionType**](InboundRouteActionType.md) | [**InboundRouteActionType**](InboundRouteActionType.md) |  | 
**Filter** | str,  | str,  | Filter of the inbound data | 
**Name** | str,  | str,  | Name of this route | 
**EmailAddress** | str,  | str,  | Email to forward the inbound to | [optional] 
**HttpAddress** | str,  | str,  | Address to notify about the inbound | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

