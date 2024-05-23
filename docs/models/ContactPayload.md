# ElasticEmail.model.contact_payload.ContactPayload

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Email** | str,  | str,  | Proper email address. | 
**Status** | [**ContactStatus**](ContactStatus.md) | [**ContactStatus**](ContactStatus.md) |  | [optional] 
**FirstName** | str,  | str,  | First name. | [optional] 
**LastName** | str,  | str,  | Last name. | [optional] 
**[CustomFields](#CustomFields)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A key-value collection of custom contact fields which can be used in the system. Only already existing custom fields will be saved. | [optional] 
**Consent** | [**ConsentData**](ConsentData.md) | [**ConsentData**](ConsentData.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# CustomFields

A key-value collection of custom contact fields which can be used in the system. Only already existing custom fields will be saved.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A key-value collection of custom contact fields which can be used in the system. Only already existing custom fields will be saved. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

