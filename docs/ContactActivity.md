# ContactActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_sent** | **int** | Total emails sent. | [optional] 
**total_opened** | **int** | Total emails opened. | [optional] 
**total_clicked** | **int** | Total emails clicked | [optional] 
**total_failed** | **int** | Total emails failed. | [optional] 
**last_sent** | **datetime** | Last date when an email was sent to this contact | [optional] 
**last_opened** | **datetime** | Date this contact last opened an email | [optional] 
**last_clicked** | **datetime** | Date this contact last clicked an email | [optional] 
**last_failed** | **datetime** | Last date when an email sent to this contact bounced | [optional] 
**last_ip** | **str** | IP from which this contact opened or clicked their email last time | [optional] 
**error_code** | **int** | Last RFC Error code if any occurred | [optional] 
**friendly_error_message** | **str** | Last RFC error message if any occurred | [optional] 

## Example

```python
from ElasticEmail.models.contact_activity import ContactActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ContactActivity from a JSON string
contact_activity_instance = ContactActivity.from_json(json)
# print the JSON string representation of the object
print(ContactActivity.to_json())

# convert the object into a dict
contact_activity_dict = contact_activity_instance.to_dict()
# create an instance of ContactActivity from a dict
contact_activity_from_dict = ContactActivity.from_dict(contact_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


