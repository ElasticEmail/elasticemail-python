# ElasticEmail.model.email_transactional_message_data.EmailTransactionalMessageData

Email data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Email data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Recipients** | [**TransactionalRecipient**](TransactionalRecipient.md) | [**TransactionalRecipient**](TransactionalRecipient.md) |  | 
**Content** | [**EmailContent**](EmailContent.md) | [**EmailContent**](EmailContent.md) |  | 
**Options** | [**Options**](Options.md) | [**Options**](Options.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

