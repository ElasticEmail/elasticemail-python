# NewSmtpCredentials

Newly generated SMTP Credentials with Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Unique token to be used in the system | [optional] 
**access_level** | [**AccessLevel**](AccessLevel.md) |  | [optional] 
**name** | **str** | Name of the key. | [optional] 
**date_created** | **datetime** | Date this SmtpCredential was created. | [optional] 
**last_use** | **datetime** | Date this SmtpCredential was last used. | [optional] 
**expires** | **datetime** | Date this SmtpCredential expires. | [optional] 
**restrict_access_to_ip_range** | **List[str]** | Which IPs can use this SmtpCredential | [optional] 

## Example

```python
from ElasticEmail.models.new_smtp_credentials import NewSmtpCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of NewSmtpCredentials from a JSON string
new_smtp_credentials_instance = NewSmtpCredentials.from_json(json)
# print the JSON string representation of the object
print(NewSmtpCredentials.to_json())

# convert the object into a dict
new_smtp_credentials_dict = new_smtp_credentials_instance.to_dict()
# create an instance of NewSmtpCredentials from a dict
new_smtp_credentials_from_dict = NewSmtpCredentials.from_dict(new_smtp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


