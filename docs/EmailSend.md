# EmailSend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID number of transaction | [optional] 
**message_id** | **str** | Unique identifier for this email. | [optional] 

## Example

```python
from ElasticEmail.models.email_send import EmailSend

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSend from a JSON string
email_send_instance = EmailSend.from_json(json)
# print the JSON string representation of the object
print(EmailSend.to_json())

# convert the object into a dict
email_send_dict = email_send_instance.to_dict()
# create an instance of EmailSend from a dict
email_send_from_dict = EmailSend.from_dict(email_send_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


