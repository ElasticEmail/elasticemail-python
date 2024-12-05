# SubaccountSettingsInfoPayload

SubAccount settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**SubaccountEmailSettingsPayload**](SubaccountEmailSettingsPayload.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.subaccount_settings_info_payload import SubaccountSettingsInfoPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountSettingsInfoPayload from a JSON string
subaccount_settings_info_payload_instance = SubaccountSettingsInfoPayload.from_json(json)
# print the JSON string representation of the object
print(SubaccountSettingsInfoPayload.to_json())

# convert the object into a dict
subaccount_settings_info_payload_dict = subaccount_settings_info_payload_instance.to_dict()
# create an instance of SubaccountSettingsInfoPayload from a dict
subaccount_settings_info_payload_from_dict = SubaccountSettingsInfoPayload.from_dict(subaccount_settings_info_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


