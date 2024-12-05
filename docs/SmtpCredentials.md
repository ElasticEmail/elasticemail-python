# SmtpCredentials

SMTP Credentials info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**AccessLevel**](AccessLevel.md) |  | [optional] 
**name** | **str** | Name of the key. | [optional] 
**date_created** | **datetime** | Date this SmtpCredential was created. | [optional] 
**last_use** | **datetime** | Date this SmtpCredential was last used. | [optional] 
**expires** | **datetime** | Date this SmtpCredential expires. | [optional] 
**restrict_access_to_ip_range** | **List[str]** | Which IPs can use this SmtpCredential | [optional] 

## Example

```python
from ElasticEmail.models.smtp_credentials import SmtpCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SmtpCredentials from a JSON string
smtp_credentials_instance = SmtpCredentials.from_json(json)
# print the JSON string representation of the object
print(SmtpCredentials.to_json())

# convert the object into a dict
smtp_credentials_dict = smtp_credentials_instance.to_dict()
# create an instance of SmtpCredentials from a dict
smtp_credentials_from_dict = SmtpCredentials.from_dict(smtp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


