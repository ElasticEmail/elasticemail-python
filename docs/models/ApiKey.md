# ElasticEmail.model.api_key.ApiKey

ApiKey info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ApiKey info | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[AccessLevel](#AccessLevel)** | list, tuple,  | tuple,  | Access level or permission to be assigned to this ApiKey. | [optional] 
**Name** | str,  | str,  | Name of the ApiKey. | [optional] 
**DateCreated** | str, datetime,  | str,  | Date this ApiKey was created. | [optional] value must conform to RFC-3339 date-time
**LastUse** | None, str, datetime,  | NoneClass, str,  | Date this ApiKey was last used. | [optional] value must conform to RFC-3339 date-time
**Expires** | None, str, datetime,  | NoneClass, str,  | Date this ApiKey expires. | [optional] value must conform to RFC-3339 date-time
**[RestrictAccessToIPRange](#RestrictAccessToIPRange)** | list, tuple,  | tuple,  | Which IPs can use this ApiKey | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# AccessLevel

Access level or permission to be assigned to this ApiKey.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Access level or permission to be assigned to this ApiKey. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccessLevel**](AccessLevel.md) | [**AccessLevel**](AccessLevel.md) | [**AccessLevel**](AccessLevel.md) |  | 

# RestrictAccessToIPRange

Which IPs can use this ApiKey

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Which IPs can use this ApiKey | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

