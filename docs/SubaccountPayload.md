# SubaccountPayload

New SubAccount payload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Proper email address. | 
**password** | **str** | Current password. | 
**send_activation** | **bool** | True, if you want to send activation email to this Account to confirm the creation of a new SubAccount. Otherwise, false (SubAccount will immediately be Active). | [optional] 
**settings** | [**SubaccountSettingsInfoPayload**](SubaccountSettingsInfoPayload.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


