# ElasticEmail.model.message_attachment.MessageAttachment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**BinaryContent** | str,  | str,  | File&#x27;s content as byte array (or a Base64 string) | 
**Name** | str,  | str,  | Display name of the file | 
**ContentType** | str,  | str,  | MIME content type | [optional] 
**Size** | decimal.Decimal, int,  | decimal.Decimal,  | Size of your attachment (in bytes). | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

