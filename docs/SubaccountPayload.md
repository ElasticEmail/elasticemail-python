# SubaccountPayload

New SubAccount payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Proper email address. | 
**password** | **str** | Current password. | 
**send_activation** | **bool** | True, if you want to send activation email to this Account to confirm the creation of a new SubAccount. Otherwise, false (SubAccount will immediately be Active). | [optional] 
**settings** | [**SubaccountSettingsInfoPayload**](SubaccountSettingsInfoPayload.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.subaccount_payload import SubaccountPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountPayload from a JSON string
subaccount_payload_instance = SubaccountPayload.from_json(json)
# print the JSON string representation of the object
print(SubaccountPayload.to_json())

# convert the object into a dict
subaccount_payload_dict = subaccount_payload_instance.to_dict()
# create an instance of SubaccountPayload from a dict
subaccount_payload_from_dict = SubaccountPayload.from_dict(subaccount_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


