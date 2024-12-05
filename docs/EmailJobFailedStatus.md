# EmailJobFailedStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**error_code** | **int** | RFC Error code | [optional] 
**category** | **str** |  | [optional] 

## Example

```python
from ElasticEmail.models.email_job_failed_status import EmailJobFailedStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EmailJobFailedStatus from a JSON string
email_job_failed_status_instance = EmailJobFailedStatus.from_json(json)
# print the JSON string representation of the object
print(EmailJobFailedStatus.to_json())

# convert the object into a dict
email_job_failed_status_dict = email_job_failed_status_instance.to_dict()
# create an instance of EmailJobFailedStatus from a dict
email_job_failed_status_from_dict = EmailJobFailedStatus.from_dict(email_job_failed_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


