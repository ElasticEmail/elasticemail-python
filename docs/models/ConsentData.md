# ElasticEmail.model.consent_data.ConsentData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ConsentIP** | str,  | str,  | IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. | [optional] 
**ConsentDate** | None, str, datetime,  | NoneClass, str,  | Date of consent to send this contact(s) your email. If not provided current date is used for consent. | [optional] value must conform to RFC-3339 date-time
**ConsentTracking** | [**ConsentTracking**](ConsentTracking.md) | [**ConsentTracking**](ConsentTracking.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

