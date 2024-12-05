# ContactsList

List of Lists, with detailed data about its contents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_name** | **str** | Name of your list. | [optional] 
**public_list_id** | **str** | ID code of list. Please note that this is different from the listid field. | [optional] 
**date_added** | **datetime** | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] 
**allow_unsubscribe** | **bool** | True: Allow unsubscribing from this list. Otherwise, false | [optional] 

## Example

```python
from ElasticEmail.models.contacts_list import ContactsList

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsList from a JSON string
contacts_list_instance = ContactsList.from_json(json)
# print the JSON string representation of the object
print(ContactsList.to_json())

# convert the object into a dict
contacts_list_dict = contacts_list_instance.to_dict()
# create an instance of ContactsList from a dict
contacts_list_from_dict = ContactsList.from_dict(contacts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


