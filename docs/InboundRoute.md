# InboundRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_id** | **str** |  | [optional] 
**name** | **str** | Name of this route | [optional] 
**filter_type** | [**InboundRouteFilterType**](InboundRouteFilterType.md) |  | [optional] 
**filter** | **str** | Filter of the inbound data | [optional] 
**action_type** | [**InboundRouteActionType**](InboundRouteActionType.md) |  | [optional] 
**action_parameter** | **str** | URL address or Email to notify about the inbound | [optional] 
**sort_order** | **int** | Place of this route in your routes queue&#39;s order | [optional] 

## Example

```python
from ElasticEmail.models.inbound_route import InboundRoute

# TODO update the JSON string below
json = "{}"
# create an instance of InboundRoute from a JSON string
inbound_route_instance = InboundRoute.from_json(json)
# print the JSON string representation of the object
print(InboundRoute.to_json())

# convert the object into a dict
inbound_route_dict = inbound_route_instance.to_dict()
# create an instance of InboundRoute from a dict
inbound_route_from_dict = InboundRoute.from_dict(inbound_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


