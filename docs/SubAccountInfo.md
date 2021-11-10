# SubAccountInfo

Detailed information about SubAccount.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_account_id** | **str** | Public key for limited access to your Account such as contact/add so you can use it safely on public websites. | [optional] 
**email** | **str** | Proper email address. | [optional] 
**settings** | [**SubaccountSettingsInfo**](SubaccountSettingsInfo.md) |  | [optional] 
**last_activity** | **datetime** | Date of last activity on Account | [optional] 
**email_credits** | **int** | Amount of email credits | [optional] 
**total_emails_sent** | **int** | Amount of emails sent from this Account | [optional] 
**reputation** | **float** | Numeric reputation | [optional] 
**status** | [**AccountStatusEnum**](AccountStatusEnum.md) |  | [optional] 
**contacts_count** | **int** | How many contacts this SubAccount has stored | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


