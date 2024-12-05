# EmailJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID number of your attachment | [optional] 
**status** | **str** | Name of status: submitted, complete, in_progress | [optional] 
**recipients_count** | **int** |  | [optional] 
**failed** | [**List[EmailJobFailedStatus]**](EmailJobFailedStatus.md) |  | [optional] 
**failed_count** | **int** | Total emails failed. | [optional] 
**sent** | **List[str]** |  | [optional] 
**sent_count** | **int** | Total emails sent. | [optional] 
**delivered** | **List[str]** | Number of delivered messages | [optional] 
**delivered_count** | **int** |  | [optional] 
**pending** | **List[str]** |  | [optional] 
**pending_count** | **int** |  | [optional] 
**opened** | **List[str]** | Number of opened messages | [optional] 
**opened_count** | **int** | Total emails opened. | [optional] 
**clicked** | **List[str]** | Number of clicked messages | [optional] 
**clicked_count** | **int** | Total emails clicked | [optional] 
**unsubscribed** | **List[str]** | Number of unsubscribed messages | [optional] 
**unsubscribed_count** | **int** | Total emails unsubscribed | [optional] 
**abuse_reports** | **List[str]** |  | [optional] 
**abuse_reports_count** | **int** |  | [optional] 
**message_ids** | **List[str]** | List of all MessageIDs for this job. | [optional] 

## Example

```python
from ElasticEmail.models.email_job_status import EmailJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EmailJobStatus from a JSON string
email_job_status_instance = EmailJobStatus.from_json(json)
# print the JSON string representation of the object
print(EmailJobStatus.to_json())

# convert the object into a dict
email_job_status_dict = email_job_status_instance.to_dict()
# create an instance of EmailJobStatus from a dict
email_job_status_from_dict = EmailJobStatus.from_dict(email_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


