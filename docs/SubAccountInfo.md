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

## Example

```python
from ElasticEmail.models.sub_account_info import SubAccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountInfo from a JSON string
sub_account_info_instance = SubAccountInfo.from_json(json)
# print the JSON string representation of the object
print(SubAccountInfo.to_json())

# convert the object into a dict
sub_account_info_dict = sub_account_info_instance.to_dict()
# create an instance of SubAccountInfo from a dict
sub_account_info_from_dict = SubAccountInfo.from_dict(sub_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


