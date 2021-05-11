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
**date_added** | **datetime** | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] 
**result** | [**EmailValidationStatus**](EmailValidationStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


