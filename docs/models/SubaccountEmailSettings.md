# ElasticEmail.model.subaccount_email_settings.SubaccountEmailSettings

Settings related to sending emails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Settings related to sending emails | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**MonthlyRefillCredits** | decimal.Decimal, int,  | decimal.Decimal,  | Amount of credits added to Account automatically | [optional] value must be a 32 bit integer
**RequiresEmailCredits** | bool,  | BoolClass,  | True, if Account needs credits to send emails. Otherwise, false | [optional] 
**EmailSizeLimit** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum size of email including attachments in MB&#x27;s | [optional] value must be a 32 bit integer
**DailySendLimit** | decimal.Decimal, int,  | decimal.Decimal,  | Amount of emails Account can send daily | [optional] value must be a 32 bit integer
**MaxContacts** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of contacts the Account can have. 0 means that parent account&#x27;s limit is used. | [optional] value must be a 32 bit integer
**EnablePrivateIPPurchase** | bool,  | BoolClass,  | Can the SubAccount purchase Private IP for themselves | [optional] 
**PoolName** | str,  | str,  | Name of your custom IP Pool to be used in the sending process | [optional] 
**ValidSenderDomainOnly** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

