# DKIMRecord

Content of the DKIM record to be added to DNS for the domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**record_value** | **str** |  | [optional] 
**domain** | **str** | Name of selected domain. | [optional] 

## Example

```python
from ElasticEmail.models.dkim_record import DKIMRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DKIMRecord from a JSON string
dkim_record_instance = DKIMRecord.from_json(json)
# print the JSON string representation of the object
print(DKIMRecord.to_json())

# convert the object into a dict
dkim_record_dict = dkim_record_instance.to_dict()
# create an instance of DKIMRecord from a dict
dkim_record_from_dict = DKIMRecord.from_dict(dkim_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


