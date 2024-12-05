# FileUploadResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails_count** | **int** | How many unique emails were detected the file | [optional] 
**duplicated_emails_count** | **int** | How many email duplicates were detected | [optional] 

## Example

```python
from ElasticEmail.models.file_upload_result import FileUploadResult

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadResult from a JSON string
file_upload_result_instance = FileUploadResult.from_json(json)
# print the JSON string representation of the object
print(FileUploadResult.to_json())

# convert the object into a dict
file_upload_result_dict = file_upload_result_instance.to_dict()
# create an instance of FileUploadResult from a dict
file_upload_result_from_dict = FileUploadResult.from_dict(file_upload_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


