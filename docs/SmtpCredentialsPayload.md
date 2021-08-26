# SmtpCredentialsPayload

Create new SMTP Credentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Credential for ease of reference. It must be a valid email address. | 
**expires** | **datetime, none_type** | Date this SmtpCredential expires. | [optional] 
**restrict_access_to_ip_range** | **[str]** | Which IPs can use this SmtpCredential | [optional] 
**subaccount** | **str** | Email of the subaccount for which this SmtpCredential should be created | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


