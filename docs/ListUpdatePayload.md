# ListUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_list_name** | **str** | Name of your list if you want to change it. | [optional] 
**allow_unsubscribe** | **bool** | True: Allow unsubscribing from this list. Otherwise, false | [optional] 

## Example

```python
from ElasticEmail.models.list_update_payload import ListUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ListUpdatePayload from a JSON string
list_update_payload_instance = ListUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(ListUpdatePayload.to_json())

# convert the object into a dict
list_update_payload_dict = list_update_payload_instance.to_dict()
# create an instance of ListUpdatePayload from a dict
list_update_payload_from_dict = ListUpdatePayload.from_dict(list_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


