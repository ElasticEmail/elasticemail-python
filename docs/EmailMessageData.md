# EmailMessageData

Email data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**List[EmailRecipient]**](EmailRecipient.md) | List of recipients | 
**content** | [**EmailContent**](EmailContent.md) |  | 
**options** | [**Options**](Options.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.email_message_data import EmailMessageData

# TODO update the JSON string below
json = "{}"
# create an instance of EmailMessageData from a JSON string
email_message_data_instance = EmailMessageData.from_json(json)
# print the JSON string representation of the object
print(EmailMessageData.to_json())

# convert the object into a dict
email_message_data_dict = email_message_data_instance.to_dict()
# create an instance of EmailMessageData from a dict
email_message_data_from_dict = EmailMessageData.from_dict(email_message_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


