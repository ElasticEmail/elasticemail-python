# SmtpCredentialsPayload

Create new SMTP Credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Credential for ease of reference. It must be a valid email address. | 
**expires** | **datetime** | Date this SmtpCredential expires. | [optional] 
**restrict_access_to_ip_range** | **List[str]** | Which IPs can use this SmtpCredential | [optional] 
**subaccount** | **str** | Email of the subaccount for which this SmtpCredential should be created | [optional] 

## Example

```python
from ElasticEmail.models.smtp_credentials_payload import SmtpCredentialsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SmtpCredentialsPayload from a JSON string
smtp_credentials_payload_instance = SmtpCredentialsPayload.from_json(json)
# print the JSON string representation of the object
print(SmtpCredentialsPayload.to_json())

# convert the object into a dict
smtp_credentials_payload_dict = smtp_credentials_payload_instance.to_dict()
# create an instance of SmtpCredentialsPayload from a dict
smtp_credentials_payload_from_dict = SmtpCredentialsPayload.from_dict(smtp_credentials_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


