# NewApiKey

Newly generated ApiKey with Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Unique token to be used in the system | [optional] 
**access_level** | [**List[AccessLevel]**](AccessLevel.md) | Access level or permission to be assigned to this ApiKey. | [optional] 
**name** | **str** | Name of the ApiKey. | [optional] 
**date_created** | **datetime** | Date this ApiKey was created. | [optional] 
**last_use** | **datetime** | Date this ApiKey was last used. | [optional] 
**expires** | **datetime** | Date this ApiKey expires. | [optional] 
**restrict_access_to_ip_range** | **List[str]** | Which IPs can use this ApiKey | [optional] 

## Example

```python
from ElasticEmail.models.new_api_key import NewApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of NewApiKey from a JSON string
new_api_key_instance = NewApiKey.from_json(json)
# print the JSON string representation of the object
print(NewApiKey.to_json())

# convert the object into a dict
new_api_key_dict = new_api_key_instance.to_dict()
# create an instance of NewApiKey from a dict
new_api_key_from_dict = NewApiKey.from_dict(new_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


