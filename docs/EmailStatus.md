# EmailStatus

Status information of the specified email
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | Email address this email was sent from. | [optional] 
**to** | **str** | Email address this email was sent to. | [optional] 
**date** | **datetime** | Date the email was submitted. | [optional] 
**status** | **object** | Value of email&#39;s status | [optional] 
**status_name** | **str** | Name of email&#39;s status | [optional] 
**status_change_date** | **datetime** | Date of last status change. | [optional] 
**date_sent** | **datetime** | Date when the email was sent | [optional] 
**date_opened** | **datetime, none_type** | Date when the email changed the status to &#39;opened&#39; | [optional] 
**date_clicked** | **datetime, none_type** | Date when the email changed the status to &#39;clicked&#39; | [optional] 
**error_message** | **str** | Detailed error or bounced message. | [optional] 
**transaction_id** | **str** | ID number of transaction | [optional] 
**envelope_from** | **str** | Envelope from address | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


