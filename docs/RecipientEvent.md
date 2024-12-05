# RecipientEvent

Detailed information about message recipient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID number of transaction | [optional] 
**msg_id** | **str** | ID number of selected message. | [optional] 
**from_email** | **str** | Default From: email address. | [optional] 
**to** | **str** | Ending date for search in YYYY-MM-DDThh:mm:ss format. | [optional] 
**subject** | **str** | Default subject of email. | [optional] 
**event_type** | [**EventType**](EventType.md) |  | [optional] 
**event_date** | **datetime** | Creation date | [optional] 
**channel_name** | **str** | Name of selected channel. | [optional] 
**message_category** | [**MessageCategory**](MessageCategory.md) |  | [optional] 
**next_try_on** | **datetime** | Date of next try | [optional] 
**message** | **str** | Content of message, HTML encoded | [optional] 
**ip_address** | **str** | IP which this email was sent through | [optional] 
**pool_name** | **str** | Name of an IP pool this email was sent through | [optional] 

## Example

```python
from ElasticEmail.models.recipient_event import RecipientEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientEvent from a JSON string
recipient_event_instance = RecipientEvent.from_json(json)
# print the JSON string representation of the object
print(RecipientEvent.to_json())

# convert the object into a dict
recipient_event_dict = recipient_event_instance.to_dict()
# create an instance of RecipientEvent from a dict
recipient_event_from_dict = RecipientEvent.from_dict(recipient_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


