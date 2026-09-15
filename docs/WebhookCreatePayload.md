# WebhookCreatePayload

Create webhook payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Filename | 
**url** | **str** | URL of notification. | 
**notify_once_per_email** | **bool** |  | [optional] 
**notification_for_sent** | **bool** |  | [optional] 
**notification_for_opened** | **bool** |  | [optional] 
**notification_for_clicked** | **bool** |  | [optional] 
**notification_for_unsubscribed** | **bool** |  | [optional] 
**notification_for_abuse_report** | **bool** |  | [optional] 
**notification_for_error** | **bool** |  | [optional] 

## Example

```python
from ElasticEmail.models.webhook_create_payload import WebhookCreatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreatePayload from a JSON string
webhook_create_payload_instance = WebhookCreatePayload.from_json(json)
# print the JSON string representation of the object
print(WebhookCreatePayload.to_json())

# convert the object into a dict
webhook_create_payload_dict = webhook_create_payload_instance.to_dict()
# create an instance of WebhookCreatePayload from a dict
webhook_create_payload_from_dict = WebhookCreatePayload.from_dict(webhook_create_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


