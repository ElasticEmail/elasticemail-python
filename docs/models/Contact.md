# ElasticEmail.model.contact.Contact

Contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Email** | str,  | str,  | Proper email address. | [optional] 
**Status** | [**ContactStatus**](ContactStatus.md) | [**ContactStatus**](ContactStatus.md) |  | [optional] 
**FirstName** | str,  | str,  | First name. | [optional] 
**LastName** | str,  | str,  | Last name. | [optional] 
**[CustomFields](#CustomFields)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A key-value collection of custom contact fields which can be used in the system. | [optional] 
**Consent** | [**ConsentData**](ConsentData.md) | [**ConsentData**](ConsentData.md) |  | [optional] 
**Source** | [**ContactSource**](ContactSource.md) | [**ContactSource**](ContactSource.md) |  | [optional] 
**DateAdded** | str, datetime,  | str,  | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] value must conform to RFC-3339 date-time
**DateUpdated** | None, str, datetime,  | NoneClass, str,  | Last change date | [optional] value must conform to RFC-3339 date-time
**StatusChangeDate** | None, str, datetime,  | NoneClass, str,  | Date of last status change. | [optional] value must conform to RFC-3339 date-time
**Activity** | [**ContactActivity**](ContactActivity.md) | [**ContactActivity**](ContactActivity.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# CustomFields

A key-value collection of custom contact fields which can be used in the system.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A key-value collection of custom contact fields which can be used in the system. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

