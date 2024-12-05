# Utm

Utm marketing data to be attached to every link in this e-mail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | utmsource value | [optional] 
**medium** | **str** | utmmedium value | [optional] 
**campaign** | **str** | utmcampaign value | [optional] 
**content** | **str** | utmcontent value | [optional] 

## Example

```python
from ElasticEmail.models.utm import Utm

# TODO update the JSON string below
json = "{}"
# create an instance of Utm from a JSON string
utm_instance = Utm.from_json(json)
# print the JSON string representation of the object
print(Utm.to_json())

# convert the object into a dict
utm_dict = utm_instance.to_dict()
# create an instance of Utm from a dict
utm_from_dict = Utm.from_dict(utm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


