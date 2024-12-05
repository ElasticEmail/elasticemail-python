# InboundPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filter of the inbound data | 
**name** | **str** | Name of this route | 
**filter_type** | [**InboundRouteFilterType**](InboundRouteFilterType.md) |  | 
**action_type** | [**InboundRouteActionType**](InboundRouteActionType.md) |  | 
**email_address** | **str** | Email to forward the inbound to | [optional] 
**http_address** | **str** | Address to notify about the inbound | [optional] 

## Example

```python
from ElasticEmail.models.inbound_payload import InboundPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InboundPayload from a JSON string
inbound_payload_instance = InboundPayload.from_json(json)
# print the JSON string representation of the object
print(InboundPayload.to_json())

# convert the object into a dict
inbound_payload_dict = inbound_payload_instance.to_dict()
# create an instance of InboundPayload from a dict
inbound_payload_from_dict = InboundPayload.from_dict(inbound_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


