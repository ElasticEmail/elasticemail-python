# ElasticEmail.model.verification_file_result.VerificationFileResult

Simple verification file result info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Simple verification file result info | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**VerificationID** | str,  | str,  | Identifier of this verification result | [optional] 
**Filename** | str,  | str,  | Origin file name | [optional] 
**VerificationStatus** | [**VerificationStatus**](VerificationStatus.md) | [**VerificationStatus**](VerificationStatus.md) |  | [optional] 
**FileUploadResult** | [**FileUploadResult**](FileUploadResult.md) | [**FileUploadResult**](FileUploadResult.md) |  | [optional] 
**DateAdded** | str, datetime,  | str,  | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] value must conform to RFC-3339 date-time
**Source** | str,  | str,  | Origin file extension | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

