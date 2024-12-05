# Template

Template info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_type** | [**TemplateType**](TemplateType.md) |  | [optional] 
**name** | **str** | Template name | [optional] 
**date_added** | **datetime** | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] 
**subject** | **str** | Default subject of email. | [optional] 
**body** | [**List[BodyPart]**](BodyPart.md) | Email content of this template | [optional] 
**template_scope** | [**TemplateScope**](TemplateScope.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


