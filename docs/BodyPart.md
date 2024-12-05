# BodyPart

Email body part with user-provided MIME type (text/html, text/plain, etc)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | [**BodyContentType**](BodyContentType.md) |  | 
**content** | **str** | Actual content of the body part | [optional] 
**charset** | **str** | Text value of charset encoding for example: iso-8859-1, windows-1251, utf-8, us-ascii, windows-1250 and more... | [optional] 

## Example

```python
from ElasticEmail.models.body_part import BodyPart

# TODO update the JSON string below
json = "{}"
# create an instance of BodyPart from a JSON string
body_part_instance = BodyPart.from_json(json)
# print the JSON string representation of the object
print(BodyPart.to_json())

# convert the object into a dict
body_part_dict = body_part_instance.to_dict()
# create an instance of BodyPart from a dict
body_part_from_dict = BodyPart.from_dict(body_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


