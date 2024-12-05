# EmailTransactionalMessageData

Email data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**TransactionalRecipient**](TransactionalRecipient.md) |  | 
**content** | [**EmailContent**](EmailContent.md) |  | 
**options** | [**Options**](Options.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.email_transactional_message_data import EmailTransactionalMessageData

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTransactionalMessageData from a JSON string
email_transactional_message_data_instance = EmailTransactionalMessageData.from_json(json)
# print the JSON string representation of the object
print(EmailTransactionalMessageData.to_json())

# convert the object into a dict
email_transactional_message_data_dict = email_transactional_message_data_instance.to_dict()
# create an instance of EmailTransactionalMessageData from a dict
email_transactional_message_data_from_dict = EmailTransactionalMessageData.from_dict(email_transactional_message_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


