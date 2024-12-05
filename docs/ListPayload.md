# ListPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_name** | **str** | Name of your list. | 
**allow_unsubscribe** | **bool** | True: Allow unsubscribing from this list. Otherwise, false | [optional] 
**emails** | **List[str]** | Comma delimited list of existing contact emails that should be added to this list. Leave empty for all contacts | [optional] 

## Example

```python
from ElasticEmail.models.list_payload import ListPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ListPayload from a JSON string
list_payload_instance = ListPayload.from_json(json)
# print the JSON string representation of the object
print(ListPayload.to_json())

# convert the object into a dict
list_payload_dict = list_payload_instance.to_dict()
# create an instance of ListPayload from a dict
list_payload_from_dict = ListPayload.from_dict(list_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


