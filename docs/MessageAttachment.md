# MessageAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_content** | **bytearray** | File&#39;s content as byte array (or a Base64 string) | 
**name** | **str** | Display name of the file | 
**content_type** | **str** | MIME content type | [optional] 
**size** | **int** | Size of your attachment (in bytes). | [optional] 

## Example

```python
from ElasticEmail.models.message_attachment import MessageAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAttachment from a JSON string
message_attachment_instance = MessageAttachment.from_json(json)
# print the JSON string representation of the object
print(MessageAttachment.to_json())

# convert the object into a dict
message_attachment_dict = message_attachment_instance.to_dict()
# create an instance of MessageAttachment from a dict
message_attachment_from_dict = MessageAttachment.from_dict(message_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


