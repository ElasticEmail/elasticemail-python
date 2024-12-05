# EmailsPayload

Provide either rule or a list of emails, not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | **str** | SQL-like rule. Sending &#39;All&#39; as a value loads all resources of the given type. Help for building a segment rule can be found here: https://help.elasticemail.com/en/articles/5162182-segment-rules | [optional] 
**emails** | **List[str]** | Comma delimited list of contact emails | [optional] 

## Example

```python
from ElasticEmail.models.emails_payload import EmailsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmailsPayload from a JSON string
emails_payload_instance = EmailsPayload.from_json(json)
# print the JSON string representation of the object
print(EmailsPayload.to_json())

# convert the object into a dict
emails_payload_dict = emails_payload_instance.to_dict()
# create an instance of EmailsPayload from a dict
emails_payload_from_dict = EmailsPayload.from_dict(emails_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


