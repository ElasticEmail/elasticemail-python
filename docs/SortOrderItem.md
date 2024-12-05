# SortOrderItem

Change the ordering of this inbound route for when matching the inbound

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_inbound_id** | **str** | ID of the route to change the order of | 
**sort_order** | **int** | 1 - route will be used first | 

## Example

```python
from ElasticEmail.models.sort_order_item import SortOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of SortOrderItem from a JSON string
sort_order_item_instance = SortOrderItem.from_json(json)
# print the JSON string representation of the object
print(SortOrderItem.to_json())

# convert the object into a dict
sort_order_item_dict = sort_order_item_instance.to_dict()
# create an instance of SortOrderItem from a dict
sort_order_item_from_dict = SortOrderItem.from_dict(sort_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


