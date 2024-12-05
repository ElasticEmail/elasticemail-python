# EmailView

Email details formatted in json

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body (HTML, otherwise plain text) of email | [optional] 
**subject** | **str** | Default subject of email. | [optional] 
**var_from** | **str** | From email address | [optional] 

## Example

```python
from ElasticEmail.models.email_view import EmailView

# TODO update the JSON string below
json = "{}"
# create an instance of EmailView from a JSON string
email_view_instance = EmailView.from_json(json)
# print the JSON string representation of the object
print(EmailView.to_json())

# convert the object into a dict
email_view_dict = email_view_instance.to_dict()
# create an instance of EmailView from a dict
email_view_from_dict = EmailView.from_dict(email_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


