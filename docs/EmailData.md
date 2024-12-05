# EmailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | [**EmailView**](EmailView.md) |  | [optional] 
**attachments** | [**List[FileInfo]**](FileInfo.md) | Attachments sent with the email | [optional] 
**status** | [**EmailStatus**](EmailStatus.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.email_data import EmailData

# TODO update the JSON string below
json = "{}"
# create an instance of EmailData from a JSON string
email_data_instance = EmailData.from_json(json)
# print the JSON string representation of the object
print(EmailData.to_json())

# convert the object into a dict
email_data_dict = email_data_instance.to_dict()
# create an instance of EmailData from a dict
email_data_from_dict = EmailData.from_dict(email_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


