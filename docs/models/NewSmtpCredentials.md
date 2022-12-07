# ElasticEmail.model.new_smtp_credentials.NewSmtpCredentials

Newly generated SMTP Credentials with Token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Newly generated SMTP Credentials with Token | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Token** | str,  | str,  | Unique token to be used in the system | [optional] 
**AccessLevel** | [**AccessLevel**](AccessLevel.md) | [**AccessLevel**](AccessLevel.md) |  | [optional] 
**Name** | str,  | str,  | Name of the key. | [optional] 
**DateCreated** | str, datetime,  | str,  | Date this SmtpCredential was created. | [optional] value must conform to RFC-3339 date-time
**LastUse** | None, str, datetime,  | NoneClass, str,  | Date this SmtpCredential was last used. | [optional] value must conform to RFC-3339 date-time
**Expires** | None, str, datetime,  | NoneClass, str,  | Date this SmtpCredential expires. | [optional] value must conform to RFC-3339 date-time
**[RestrictAccessToIPRange](#RestrictAccessToIPRange)** | list, tuple,  | tuple,  | Which IPs can use this SmtpCredential | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# RestrictAccessToIPRange

Which IPs can use this SmtpCredential

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Which IPs can use this SmtpCredential | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

