# ElasticEmail.model.subaccount_payload.SubaccountPayload

New SubAccount payload

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | New SubAccount payload | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Email** | str,  | str,  | Proper email address. | 
**Password** | str,  | str,  | Current password. | 
**SendActivation** | bool,  | BoolClass,  | True, if you want to send activation email to this Account to confirm the creation of a new SubAccount. Otherwise, false (SubAccount will immediately be Active). | [optional] 
**Settings** | [**SubaccountSettingsInfoPayload**](SubaccountSettingsInfoPayload.md) | [**SubaccountSettingsInfoPayload**](SubaccountSettingsInfoPayload.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

