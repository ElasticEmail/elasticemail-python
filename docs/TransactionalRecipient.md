# TransactionalRecipient

List of transactional recipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **List[str]** | List of recipients (visible to others) | 
**cc** | **List[str]** | List of Carbon Copy recipients (visible to others) | [optional] 
**bcc** | **List[str]** | List of Blind Carbon Copy recipients (hidden from other recipients) | [optional] 

## Example

```python
from ElasticEmail.models.transactional_recipient import TransactionalRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionalRecipient from a JSON string
transactional_recipient_instance = TransactionalRecipient.from_json(json)
# print the JSON string representation of the object
print(TransactionalRecipient.to_json())

# convert the object into a dict
transactional_recipient_dict = transactional_recipient_instance.to_dict()
# create an instance of TransactionalRecipient from a dict
transactional_recipient_from_dict = TransactionalRecipient.from_dict(transactional_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


