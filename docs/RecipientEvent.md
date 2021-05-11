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
**event_type** | **object** | Type of an Event | [optional] 
**event_date** | **datetime** | Creation date | [optional] 
**channel_name** | **str** | Name of selected channel. | [optional] 
**message_category** | **object** | Message category | [optional] 
**next_try_on** | **datetime, none_type** | Date of next try | [optional] 
**message** | **str** | Content of message, HTML encoded | [optional] 
**ip_address** | **str** | IP which this email was sent through | [optional] 
**pool_name** | **str** | Name of an IP pool this email was sent through | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


