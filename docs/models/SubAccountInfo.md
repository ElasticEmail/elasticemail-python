# ElasticEmail.model.sub_account_info.SubAccountInfo

Detailed information about SubAccount.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Detailed information about SubAccount. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**PublicAccountID** | str,  | str,  | Public key for limited access to your Account such as contact/add so you can use it safely on public websites. | [optional] 
**Email** | str,  | str,  | Proper email address. | [optional] 
**Settings** | [**SubaccountSettingsInfo**](SubaccountSettingsInfo.md) | [**SubaccountSettingsInfo**](SubaccountSettingsInfo.md) |  | [optional] 
**LastActivity** | str, datetime,  | str,  | Date of last activity on Account | [optional] value must conform to RFC-3339 date-time
**EmailCredits** | decimal.Decimal, int,  | decimal.Decimal,  | Amount of email credits | [optional] value must be a 32 bit integer
**TotalEmailsSent** | decimal.Decimal, int,  | decimal.Decimal,  | Amount of emails sent from this Account | [optional] value must be a 64 bit integer
**Reputation** | decimal.Decimal, int, float,  | decimal.Decimal,  | Numeric reputation | [optional] value must be a 64 bit float
**Status** | [**AccountStatusEnum**](AccountStatusEnum.md) | [**AccountStatusEnum**](AccountStatusEnum.md) |  | [optional] 
**ContactsCount** | decimal.Decimal, int,  | decimal.Decimal,  | How many contacts this SubAccount has stored | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

