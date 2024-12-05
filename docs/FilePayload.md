# FilePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_content** | **bytearray** | Content of the file sent as binary data | 
**name** | **str** | Filename | [optional] 
**content_type** | **str** | Type of file&#39;s content (e.g. image/jpeg) | [optional] 

## Example

```python
from ElasticEmail.models.file_payload import FilePayload

# TODO update the JSON string below
json = "{}"
# create an instance of FilePayload from a JSON string
file_payload_instance = FilePayload.from_json(json)
# print the JSON string representation of the object
print(FilePayload.to_json())

# convert the object into a dict
file_payload_dict = file_payload_instance.to_dict()
# create an instance of FilePayload from a dict
file_payload_from_dict = FilePayload.from_dict(file_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


