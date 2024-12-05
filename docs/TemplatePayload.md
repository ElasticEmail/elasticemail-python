# TemplatePayload

New template object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Template name | 
**subject** | **str** | Default subject of email. | [optional] 
**body** | [**List[BodyPart]**](BodyPart.md) | Email content of this template | [optional] 
**template_scope** | [**TemplateScope**](TemplateScope.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.template_payload import TemplatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePayload from a JSON string
template_payload_instance = TemplatePayload.from_json(json)
# print the JSON string representation of the object
print(TemplatePayload.to_json())

# convert the object into a dict
template_payload_dict = template_payload_instance.to_dict()
# create an instance of TemplatePayload from a dict
template_payload_from_dict = TemplatePayload.from_dict(template_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


