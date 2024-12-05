# EmailStatus

Status information of the specified email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Email address this email was sent from. | [optional] 
**to** | **str** | Email address this email was sent to. | [optional] 
**var_date** | **datetime** | Date the email was submitted. | [optional] 
**status** | [**LogJobStatus**](LogJobStatus.md) |  | [optional] 
**status_name** | **str** | Name of email&#39;s status | [optional] 
**status_change_date** | **datetime** | Date of last status change. | [optional] 
**date_sent** | **datetime** | Date when the email was sent | [optional] 
**date_opened** | **datetime** | Date when the email changed the status to &#39;opened&#39; | [optional] 
**date_clicked** | **datetime** | Date when the email changed the status to &#39;clicked&#39; | [optional] 
**error_message** | **str** | Detailed error or bounced message. | [optional] 
**transaction_id** | **str** | ID number of transaction | [optional] 
**envelope_from** | **str** | Envelope from address | [optional] 
**error_category** | [**MessageCategoryEnum**](MessageCategoryEnum.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.email_status import EmailStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EmailStatus from a JSON string
email_status_instance = EmailStatus.from_json(json)
# print the JSON string representation of the object
print(EmailStatus.to_json())

# convert the object into a dict
email_status_dict = email_status_instance.to_dict()
# create an instance of EmailStatus from a dict
email_status_from_dict = EmailStatus.from_dict(email_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


