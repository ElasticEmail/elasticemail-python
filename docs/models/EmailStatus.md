# ElasticEmail.model.email_status.EmailStatus

Status information of the specified email

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Status information of the specified email | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**From** | str,  | str,  | Email address this email was sent from. | [optional] 
**To** | str,  | str,  | Email address this email was sent to. | [optional] 
**Date** | str, datetime,  | str,  | Date the email was submitted. | [optional] value must conform to RFC-3339 date-time
**Status** | [**LogJobStatus**](LogJobStatus.md) | [**LogJobStatus**](LogJobStatus.md) |  | [optional] 
**StatusName** | str,  | str,  | Name of email&#x27;s status | [optional] 
**StatusChangeDate** | str, datetime,  | str,  | Date of last status change. | [optional] value must conform to RFC-3339 date-time
**DateSent** | str, datetime,  | str,  | Date when the email was sent | [optional] value must conform to RFC-3339 date-time
**DateOpened** | None, str, datetime,  | NoneClass, str,  | Date when the email changed the status to &#x27;opened&#x27; | [optional] value must conform to RFC-3339 date-time
**DateClicked** | None, str, datetime,  | NoneClass, str,  | Date when the email changed the status to &#x27;clicked&#x27; | [optional] value must conform to RFC-3339 date-time
**ErrorMessage** | str,  | str,  | Detailed error or bounced message. | [optional] 
**TransactionID** | str,  | str,  | ID number of transaction | [optional] 
**EnvelopeFrom** | str,  | str,  | Envelope from address | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

