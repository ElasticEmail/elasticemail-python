# ConsentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_ip** | **str** | IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. | [optional] 
**consent_date** | **datetime** | Date of consent to send this contact(s) your email. If not provided current date is used for consent. | [optional] 
**consent_tracking** | [**ConsentTracking**](ConsentTracking.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.consent_data import ConsentData

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentData from a JSON string
consent_data_instance = ConsentData.from_json(json)
# print the JSON string representation of the object
print(ConsentData.to_json())

# convert the object into a dict
consent_data_dict = consent_data_instance.to_dict()
# create an instance of ConsentData from a dict
consent_data_from_dict = ConsentData.from_dict(consent_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


