# Suppression

Suppression - Email returning Hard Bounces

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Proper email address. | [optional] 
**friendly_error_message** | **str** | RFC error message | [optional] 
**error_code** | **int** | SMTP Error code | [optional] 
**date_updated** | **datetime** | Last change date | [optional] 

## Example

```python
from ElasticEmail.models.suppression import Suppression

# TODO update the JSON string below
json = "{}"
# create an instance of Suppression from a JSON string
suppression_instance = Suppression.from_json(json)
# print the JSON string representation of the object
print(Suppression.to_json())

# convert the object into a dict
suppression_dict = suppression_instance.to_dict()
# create an instance of Suppression from a dict
suppression_from_dict = Suppression.from_dict(suppression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


