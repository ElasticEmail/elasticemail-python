# NewSmtpCredentials

Newly generated SMTP Credentials with Token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Unique token to be used in the system | [optional] 
**access_level** | [**AccessLevel**](AccessLevel.md) |  | [optional] 
**name** | **str** | Name of the key. | [optional] 
**date_created** | **datetime** | Date this SmtpCredential was created. | [optional] 
**last_use** | **datetime, none_type** | Date this SmtpCredential was last used. | [optional] 
**expires** | **datetime, none_type** | Date this SmtpCredential expires. | [optional] 
**restrict_access_to_ip_range** | **[str]** | Which IPs can use this SmtpCredential | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


