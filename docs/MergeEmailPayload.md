# MergeEmailPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_file** | [**MessageAttachment**](MessageAttachment.md) |  | 
**content** | [**EmailContent**](EmailContent.md) |  | 
**options** | [**Options**](Options.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.merge_email_payload import MergeEmailPayload

# TODO update the JSON string below
json = "{}"
# create an instance of MergeEmailPayload from a JSON string
merge_email_payload_instance = MergeEmailPayload.from_json(json)
# print the JSON string representation of the object
print(MergeEmailPayload.to_json())

# convert the object into a dict
merge_email_payload_dict = merge_email_payload_instance.to_dict()
# create an instance of MergeEmailPayload from a dict
merge_email_payload_from_dict = MergeEmailPayload.from_dict(merge_email_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


