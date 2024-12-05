# DomainUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_status** | [**CertificateValidationStatus**](CertificateValidationStatus.md) |  | [optional] 
**verp** | **bool** |  | [optional] 
**custom_bounces_domain** | **str** |  | [optional] 
**is_custom_bounces_domain_default** | **bool** |  | [optional] 

## Example

```python
from ElasticEmail.models.domain_update_payload import DomainUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of DomainUpdatePayload from a JSON string
domain_update_payload_instance = DomainUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(DomainUpdatePayload.to_json())

# convert the object into a dict
domain_update_payload_dict = domain_update_payload_instance.to_dict()
# create an instance of DomainUpdatePayload from a dict
domain_update_payload_from_dict = DomainUpdatePayload.from_dict(domain_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


