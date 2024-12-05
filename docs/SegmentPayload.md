# SegmentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Segment name | 
**rule** | **str** | SQL-like rule to determine which Contacts belong to this Segment. Help for building a segment rule can be found here: https://help.elasticemail.com/en/articles/5162182-segment-rules | 

## Example

```python
from ElasticEmail.models.segment_payload import SegmentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentPayload from a JSON string
segment_payload_instance = SegmentPayload.from_json(json)
# print the JSON string representation of the object
print(SegmentPayload.to_json())

# convert the object into a dict
segment_payload_dict = segment_payload_instance.to_dict()
# create an instance of SegmentPayload from a dict
segment_payload_from_dict = SegmentPayload.from_dict(segment_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


