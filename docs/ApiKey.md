# ApiKey

ApiKey info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**List[AccessLevel]**](AccessLevel.md) | Access level or permission to be assigned to this ApiKey. | [optional] 
**name** | **str** | Name of the ApiKey. | [optional] 
**date_created** | **datetime** | Date this ApiKey was created. | [optional] 
**last_use** | **datetime** | Date this ApiKey was last used. | [optional] 
**expires** | **datetime** | Date this ApiKey expires. | [optional] 
**restrict_access_to_ip_range** | **List[str]** | Which IPs can use this ApiKey | [optional] 

## Example

```python
from ElasticEmail.models.api_key import ApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKey from a JSON string
api_key_instance = ApiKey.from_json(json)
# print the JSON string representation of the object
print(ApiKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of ApiKey from a dict
api_key_from_dict = ApiKey.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


