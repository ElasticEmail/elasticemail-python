# ElasticEmail.model.list_payload.ListPayload

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ListName** | str,  | str,  | Name of your list. | 
**AllowUnsubscribe** | bool,  | BoolClass,  | True: Allow unsubscribing from this list. Otherwise, false | [optional] 
**[Emails](#Emails)** | list, tuple,  | tuple,  | Comma delimited list of existing contact emails that should be added to this list. Leave empty for all contacts | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Emails

Comma delimited list of existing contact emails that should be added to this list. Leave empty for all contacts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Comma delimited list of existing contact emails that should be added to this list. Leave empty for all contacts | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

