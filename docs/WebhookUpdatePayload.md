# WebhookUpdatePayload

Update webhook payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Filename | [optional] 
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
from ElasticEmail.models.webhook_update_payload import WebhookUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookUpdatePayload from a JSON string
webhook_update_payload_instance = WebhookUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(WebhookUpdatePayload.to_json())

# convert the object into a dict
webhook_update_payload_dict = webhook_update_payload_instance.to_dict()
# create an instance of WebhookUpdatePayload from a dict
webhook_update_payload_from_dict = WebhookUpdatePayload.from_dict(webhook_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


