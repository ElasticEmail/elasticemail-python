# ApiKeyPayload

Create a new ApiKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the ApiKey for ease of reference. | 
**access_level** | [**List[AccessLevel]**](AccessLevel.md) | Access level or permission to be assigned to this ApiKey. | 
**expires** | **datetime** | Date this ApiKey expires. | [optional] 
**restrict_access_to_ip_range** | **List[str]** | Which IPs can use this ApiKey | [optional] 
**subaccount** | **str** | Email of the subaccount for which this ApiKey should be created | [optional] 

## Example

```python
from ElasticEmail.models.api_key_payload import ApiKeyPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyPayload from a JSON string
api_key_payload_instance = ApiKeyPayload.from_json(json)
# print the JSON string representation of the object
print(ApiKeyPayload.to_json())

# convert the object into a dict
api_key_payload_dict = api_key_payload_instance.to_dict()
# create an instance of ApiKeyPayload from a dict
api_key_payload_from_dict = ApiKeyPayload.from_dict(api_key_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


