# ElasticEmail.model.email_validation_result.EmailValidationResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Account** | str,  | str,  | Local part of an email | [optional] 
**Domain** | str,  | str,  | Name of selected domain. | [optional] 
**Email** | str,  | str,  | Full email address that was verified | [optional] 
**SuggestedSpelling** | str,  | str,  | Suggested spelling if a possible mistake was found | [optional] 
**Disposable** | bool,  | BoolClass,  | Does the email have a temporary domain | [optional] 
**Role** | bool,  | BoolClass,  | Is an email a role email (e.g. info@, noreply@ etc.) | [optional] 
**Reason** | str,  | str,  | All detected issues | [optional] 
**DateAdded** | str, datetime,  | str,  | Added date | [optional] value must conform to RFC-3339 date-time
**Result** | [**EmailValidationStatus**](EmailValidationStatus.md) | [**EmailValidationStatus**](EmailValidationStatus.md) |  | [optional] 
**PredictedScore** | decimal.Decimal, int, float,  | decimal.Decimal,  | Predicted score | [optional] 
**PredictedStatus** | [**EmailPredictedValidationStatus**](EmailPredictedValidationStatus.md) | [**EmailPredictedValidationStatus**](EmailPredictedValidationStatus.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

