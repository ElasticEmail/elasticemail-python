# SplitOptions

Optional A/X split campaign options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optimize_for** | [**SplitOptimizationType**](SplitOptimizationType.md) |  | [optional] 
**optimize_period_minutes** | **int** | For how long should the results be measured until determining the winner template (content) | [optional] 

## Example

```python
from ElasticEmail.models.split_options import SplitOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SplitOptions from a JSON string
split_options_instance = SplitOptions.from_json(json)
# print the JSON string representation of the object
print(SplitOptions.to_json())

# convert the object into a dict
split_options_dict = split_options_instance.to_dict()
# create an instance of SplitOptions from a dict
split_options_from_dict = SplitOptions.from_dict(split_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


