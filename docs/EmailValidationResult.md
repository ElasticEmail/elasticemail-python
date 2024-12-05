# EmailValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Local part of an email | [optional] 
**domain** | **str** | Name of selected domain. | [optional] 
**email** | **str** | Full email address that was verified | [optional] 
**suggested_spelling** | **str** | Suggested spelling if a possible mistake was found | [optional] 
**disposable** | **bool** | Does the email have a temporary domain | [optional] 
**role** | **bool** | Is an email a role email (e.g. info@, noreply@ etc.) | [optional] 
**reason** | **str** | All detected issues | [optional] 
**date_added** | **datetime** | Added date | [optional] 
**result** | [**EmailValidationStatus**](EmailValidationStatus.md) |  | [optional] 
**predicted_score** | **float** | Predicted score | [optional] 
**predicted_status** | [**EmailPredictedValidationStatus**](EmailPredictedValidationStatus.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.email_validation_result import EmailValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of EmailValidationResult from a JSON string
email_validation_result_instance = EmailValidationResult.from_json(json)
# print the JSON string representation of the object
print(EmailValidationResult.to_json())

# convert the object into a dict
email_validation_result_dict = email_validation_result_instance.to_dict()
# create an instance of EmailValidationResult from a dict
email_validation_result_from_dict = EmailValidationResult.from_dict(email_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


