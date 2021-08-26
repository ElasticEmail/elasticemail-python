# ContactPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Proper email address. | 
**status** | **dict** | Status of the given resource | [optional] 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**custom_fields** | **{str: (str,)}** | A key-value collection of custom contact fields which can be used in the system. Only already existing custom fields will be saved. | [optional] 
**consent** | [**ConsentData**](ConsentData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


