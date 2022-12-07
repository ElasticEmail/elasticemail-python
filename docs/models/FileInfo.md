# ElasticEmail.model.file_info.FileInfo

File information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | File information | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**FileName** | str,  | str,  | Name of your file including extension. | [optional] 
**Size** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Size of your attachment (in bytes). | [optional] value must be a 32 bit integer
**DateAdded** | str, datetime,  | str,  | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] value must conform to RFC-3339 date-time
**ExpirationDate** | None, str, datetime,  | NoneClass, str,  | Date when the file will be deleted from your Account. | [optional] value must conform to RFC-3339 date-time
**ContentType** | str,  | str,  | Content type of the file. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

