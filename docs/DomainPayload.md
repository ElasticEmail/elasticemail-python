# DomainPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Name of selected domain. | [optional] 
**set_as_default** | **bool** |  | [optional] 

## Example

```python
from ElasticEmail.models.domain_payload import DomainPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPayload from a JSON string
domain_payload_instance = DomainPayload.from_json(json)
# print the JSON string representation of the object
print(DomainPayload.to_json())

# convert the object into a dict
domain_payload_dict = domain_payload_instance.to_dict()
# create an instance of DomainPayload from a dict
domain_payload_from_dict = DomainPayload.from_dict(domain_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


