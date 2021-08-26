# ApiKeyPayload

Create a new ApiKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the ApiKey for ease of reference. | 
**access_level** | [**[AccessLevel]**](AccessLevel.md) | Access level or permission to be assigned to this ApiKey. | 
**expires** | **datetime, none_type** | Date this ApiKey expires. | [optional] 
**restrict_access_to_ip_range** | **[str]** | Which IPs can use this ApiKey | [optional] 
**subaccount** | **str** | Email of the subaccount for which this ApiKey should be created | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


