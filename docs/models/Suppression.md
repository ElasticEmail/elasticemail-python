# ElasticEmail.model.suppression.Suppression

Suppression - Email returning Hard Bounces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Suppression - Email returning Hard Bounces | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Email** | str,  | str,  | Proper email address. | [optional] 
**FriendlyErrorMessage** | str,  | str,  | RFC error message | [optional] 
**ErrorCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | SMTP Error code | [optional] value must be a 32 bit integer
**DateUpdated** | None, str, datetime,  | NoneClass, str,  | Last change date | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

