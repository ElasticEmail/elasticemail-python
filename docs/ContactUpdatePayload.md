# ContactUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**custom_fields** | **Dict[str, str]** | A key-value collection of custom contact fields which can be used in the system. | [optional] 

## Example

```python
from ElasticEmail.models.contact_update_payload import ContactUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdatePayload from a JSON string
contact_update_payload_instance = ContactUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(ContactUpdatePayload.to_json())

# convert the object into a dict
contact_update_payload_dict = contact_update_payload_instance.to_dict()
# create an instance of ContactUpdatePayload from a dict
contact_update_payload_from_dict = ContactUpdatePayload.from_dict(contact_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


