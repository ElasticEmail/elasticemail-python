# ElasticEmail.model.contacts_list.ContactsList

List of Lists, with detailed data about its contents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of Lists, with detailed data about its contents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ListName** | str,  | str,  | Name of your list. | [optional] 
**PublicListID** | None, str,  | NoneClass, str,  | ID code of list. Please note that this is different from the listid field. | [optional] 
**DateAdded** | str, datetime,  | str,  | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] value must conform to RFC-3339 date-time
**AllowUnsubscribe** | bool,  | BoolClass,  | True: Allow unsubscribing from this list. Otherwise, false | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

