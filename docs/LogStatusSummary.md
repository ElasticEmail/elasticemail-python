# LogStatusSummary

Summary of log status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **int** | Number of recipients | [optional] 
**email_total** | **int** | Number of emails | [optional] 
**sms_total** | **int** | Number of SMS | [optional] 
**delivered** | **int** | Number of delivered messages | [optional] 
**bounced** | **int** | Number of bounced messages | [optional] 
**in_progress** | **int** | Number of messages in progress | [optional] 
**opened** | **int** | Number of opened messages | [optional] 
**clicked** | **int** | Number of clicked messages | [optional] 
**unsubscribed** | **int** | Number of unsubscribed messages | [optional] 
**complaints** | **int** | Number of complaint messages | [optional] 
**inbound** | **int** | Number of inbound messages | [optional] 
**manual_cancel** | **int** | Number of manually cancelled messages | [optional] 
**not_delivered** | **int** | Number of messages flagged with &#39;Not Delivered&#39; | [optional] 

## Example

```python
from ElasticEmail.models.log_status_summary import LogStatusSummary

# TODO update the JSON string below
json = "{}"
# create an instance of LogStatusSummary from a JSON string
log_status_summary_instance = LogStatusSummary.from_json(json)
# print the JSON string representation of the object
print(LogStatusSummary.to_json())

# convert the object into a dict
log_status_summary_dict = log_status_summary_instance.to_dict()
# create an instance of LogStatusSummary from a dict
log_status_summary_from_dict = LogStatusSummary.from_dict(log_status_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


