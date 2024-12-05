# DomainData

Domain data, with information about domain records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_log** | **str** | Domain validation results - when domain has been running through validation process | [optional] 
**domain** | **str** | Name of selected domain. | [optional] 
**default_domain** | **bool** | True, if domain is used as default. Otherwise, false, | [optional] 
**spf** | **bool** | True, if SPF record is verified | [optional] 
**dkim** | **bool** | True, if DKIM record is verified | [optional] 
**mx** | **bool** | True, if MX record is verified | [optional] 
**dmarc** | **bool** |  | [optional] 
**is_rewrite_domain_valid** | **bool** | True, if tracking CNAME record is verified | [optional] 
**verify** | **bool** | True, if DKIM, SPF, or tracking are still to be verified | [optional] 
**type** | [**TrackingType**](TrackingType.md) |  | [optional] 
**tracking_status** | [**TrackingValidationStatus**](TrackingValidationStatus.md) |  | [optional] 
**certificate_status** | [**CertificateValidationStatus**](CertificateValidationStatus.md) |  | [optional] 
**certificate_validation_error** | **str** |  | [optional] 
**tracking_type_user_request** | [**TrackingType**](TrackingType.md) |  | [optional] 
**verp** | **bool** |  | [optional] 
**custom_bounces_domain** | **str** |  | [optional] 
**is_custom_bounces_domain_default** | **bool** |  | [optional] 
**is_marked_for_deletion** | **bool** |  | [optional] 
**ownership** | [**DomainOwner**](DomainOwner.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.domain_data import DomainData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainData from a JSON string
domain_data_instance = DomainData.from_json(json)
# print the JSON string representation of the object
print(DomainData.to_json())

# convert the object into a dict
domain_data_dict = domain_data_instance.to_dict()
# create an instance of DomainData from a dict
domain_data_from_dict = DomainData.from_dict(domain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


