# FileInfo

File information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Name of your file including extension. | [optional] 
**size** | **int** | Size of your attachment (in bytes). | [optional] 
**date_added** | **datetime** | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] 
**expiration_date** | **datetime** | Date when the file will be deleted from your Account. | [optional] 
**content_type** | **str** | Content type of the file. | [optional] 

## Example

```python
from ElasticEmail.models.file_info import FileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileInfo from a JSON string
file_info_instance = FileInfo.from_json(json)
# print the JSON string representation of the object
print(FileInfo.to_json())

# convert the object into a dict
file_info_dict = file_info_instance.to_dict()
# create an instance of FileInfo from a dict
file_info_from_dict = FileInfo.from_dict(file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


