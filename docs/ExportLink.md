# ExportLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | Direct URL to the exported file | [optional] 
**public_export_id** | **str** | ID of the exported file | [optional] 

## Example

```python
from ElasticEmail.models.export_link import ExportLink

# TODO update the JSON string below
json = "{}"
# create an instance of ExportLink from a JSON string
export_link_instance = ExportLink.from_json(json)
# print the JSON string representation of the object
print(ExportLink.to_json())

# convert the object into a dict
export_link_dict = export_link_instance.to_dict()
# create an instance of ExportLink from a dict
export_link_from_dict = ExportLink.from_dict(export_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


