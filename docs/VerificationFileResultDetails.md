# VerificationFileResultDetails

Detailed verification file result info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_result** | [**List[EmailValidationResult]**](EmailValidationResult.md) | Verification result&#39;s details | [optional] 
**verification_id** | **str** | Identifier of this verification result | [optional] 
**filename** | **str** | Origin file name | [optional] 
**verification_status** | [**VerificationStatus**](VerificationStatus.md) |  | [optional] 
**file_upload_result** | [**FileUploadResult**](FileUploadResult.md) |  | [optional] 
**date_added** | **datetime** | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] 
**source** | **str** | Origin file extension | [optional] 

## Example

```python
from ElasticEmail.models.verification_file_result_details import VerificationFileResultDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationFileResultDetails from a JSON string
verification_file_result_details_instance = VerificationFileResultDetails.from_json(json)
# print the JSON string representation of the object
print(VerificationFileResultDetails.to_json())

# convert the object into a dict
verification_file_result_details_dict = verification_file_result_details_instance.to_dict()
# create an instance of VerificationFileResultDetails from a dict
verification_file_result_details_from_dict = VerificationFileResultDetails.from_dict(verification_file_result_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


