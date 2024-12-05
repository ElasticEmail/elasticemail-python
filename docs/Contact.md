# Contact

Contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Proper email address. | [optional] 
**status** | [**ContactStatus**](ContactStatus.md) |  | [optional] 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**custom_fields** | **Dict[str, str]** | A key-value collection of custom contact fields which can be used in the system. | [optional] 
**consent** | [**ConsentData**](ConsentData.md) |  | [optional] 
**source** | [**ContactSource**](ContactSource.md) |  | [optional] 
**date_added** | **datetime** | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] 
**date_updated** | **datetime** | Last change date | [optional] 
**status_change_date** | **datetime** | Date of last status change. | [optional] 
**activity** | [**ContactActivity**](ContactActivity.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print(Contact.to_json())

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


