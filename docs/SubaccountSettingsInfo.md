# SubaccountSettingsInfo

SubAccount settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**SubaccountEmailSettings**](SubaccountEmailSettings.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.subaccount_settings_info import SubaccountSettingsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountSettingsInfo from a JSON string
subaccount_settings_info_instance = SubaccountSettingsInfo.from_json(json)
# print the JSON string representation of the object
print(SubaccountSettingsInfo.to_json())

# convert the object into a dict
subaccount_settings_info_dict = subaccount_settings_info_instance.to_dict()
# create an instance of SubaccountSettingsInfo from a dict
subaccount_settings_info_from_dict = SubaccountSettingsInfo.from_dict(subaccount_settings_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


