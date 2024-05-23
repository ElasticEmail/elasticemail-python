# ElasticEmail.model.subaccount_email_credits_payload.SubaccountEmailCreditsPayload

A change to SubAccount email credits pool, with an additional note.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A change to SubAccount email credits pool, with an additional note. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Credits** | decimal.Decimal, int,  | decimal.Decimal,  | Positive or negative value; this will be added or subtracted from Subaccount&#x27;s current email Credits pool. | value must be a 32 bit integer
**Notes** | str,  | str,  | Note to append to this credits change, for history. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

