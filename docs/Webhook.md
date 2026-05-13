# Webhook

Notification webhook setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | Public webhook ID | [optional] 
**name** | **str** | Filename | [optional] 
**date_created** | **datetime** | Creation date. | [optional] 
**date_updated** | **datetime** | Last change date | [optional] 
**url** | **str** | URL of notification. | [optional] 
**notify_once_per_email** | **bool** |  | [optional] 
**notification_for_sent** | **bool** |  | [optional] 
**notification_for_opened** | **bool** |  | [optional] 
**notification_for_clicked** | **bool** |  | [optional] 
**notification_for_unsubscribed** | **bool** |  | [optional] 
**notification_for_abuse_report** | **bool** |  | [optional] 
**notification_for_error** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 

## Example

```python
from ElasticEmail.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


