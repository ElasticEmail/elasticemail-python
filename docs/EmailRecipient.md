# EmailRecipient

List of recipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Proper email address. | 
**fields** | **Dict[str, str]** | A key-value collection of merge fields which can be used in e-mail body. | [optional] 

## Example

```python
from ElasticEmail.models.email_recipient import EmailRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of EmailRecipient from a JSON string
email_recipient_instance = EmailRecipient.from_json(json)
# print the JSON string representation of the object
print(EmailRecipient.to_json())

# convert the object into a dict
email_recipient_dict = email_recipient_instance.to_dict()
# create an instance of EmailRecipient from a dict
email_recipient_from_dict = EmailRecipient.from_dict(email_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


