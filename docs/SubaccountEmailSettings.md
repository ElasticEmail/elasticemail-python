# SubaccountEmailSettings

Settings related to sending emails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_refill_credits** | **int** | Amount of credits added to Account automatically | [optional] 
**requires_email_credits** | **bool** | True, if Account needs credits to send emails. Otherwise, false | [optional] 
**email_size_limit** | **int** | Maximum size of email including attachments in MB&#39;s | [optional] 
**daily_send_limit** | **int** | Amount of emails Account can send daily | [optional] 
**max_contacts** | **int** | Maximum number of contacts the Account can have. 0 means that parent account&#39;s limit is used. | [optional] 
**enable_private_ip_purchase** | **bool** | Can the SubAccount purchase Private IP for themselves | [optional] 
**pool_name** | **str** | Name of your custom IP Pool to be used in the sending process | [optional] 
**valid_sender_domain_only** | **bool** |  | [optional] 

## Example

```python
from ElasticEmail.models.subaccount_email_settings import SubaccountEmailSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountEmailSettings from a JSON string
subaccount_email_settings_instance = SubaccountEmailSettings.from_json(json)
# print the JSON string representation of the object
print(SubaccountEmailSettings.to_json())

# convert the object into a dict
subaccount_email_settings_dict = subaccount_email_settings_instance.to_dict()
# create an instance of SubaccountEmailSettings from a dict
subaccount_email_settings_from_dict = SubaccountEmailSettings.from_dict(subaccount_email_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


