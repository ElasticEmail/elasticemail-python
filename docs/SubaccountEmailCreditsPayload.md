# SubaccountEmailCreditsPayload

A change to SubAccount email credits pool, with an additional note.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits** | **int** | Positive or negative value; this will be added or subtracted from Subaccount&#39;s current email Credits pool. | 
**notes** | **str** | Note to append to this credits change, for history. | [optional] 

## Example

```python
from ElasticEmail.models.subaccount_email_credits_payload import SubaccountEmailCreditsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountEmailCreditsPayload from a JSON string
subaccount_email_credits_payload_instance = SubaccountEmailCreditsPayload.from_json(json)
# print the JSON string representation of the object
print(SubaccountEmailCreditsPayload.to_json())

# convert the object into a dict
subaccount_email_credits_payload_dict = subaccount_email_credits_payload_instance.to_dict()
# create an instance of SubaccountEmailCreditsPayload from a dict
subaccount_email_credits_payload_from_dict = SubaccountEmailCreditsPayload.from_dict(subaccount_email_credits_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


