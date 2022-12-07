# ElasticEmail.model.log_status_summary.LogStatusSummary

Summary of log status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Summary of log status | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Recipients** | decimal.Decimal, int,  | decimal.Decimal,  | Number of recipients | [optional] value must be a 64 bit integer
**EmailTotal** | decimal.Decimal, int,  | decimal.Decimal,  | Number of emails | [optional] value must be a 64 bit integer
**SmsTotal** | decimal.Decimal, int,  | decimal.Decimal,  | Number of SMS | [optional] value must be a 64 bit integer
**Delivered** | decimal.Decimal, int,  | decimal.Decimal,  | Number of delivered messages | [optional] value must be a 64 bit integer
**Bounced** | decimal.Decimal, int,  | decimal.Decimal,  | Number of bounced messages | [optional] value must be a 64 bit integer
**InProgress** | decimal.Decimal, int,  | decimal.Decimal,  | Number of messages in progress | [optional] value must be a 64 bit integer
**Opened** | decimal.Decimal, int,  | decimal.Decimal,  | Number of opened messages | [optional] value must be a 64 bit integer
**Clicked** | decimal.Decimal, int,  | decimal.Decimal,  | Number of clicked messages | [optional] value must be a 64 bit integer
**Unsubscribed** | decimal.Decimal, int,  | decimal.Decimal,  | Number of unsubscribed messages | [optional] value must be a 64 bit integer
**Complaints** | decimal.Decimal, int,  | decimal.Decimal,  | Number of complaint messages | [optional] value must be a 64 bit integer
**Inbound** | decimal.Decimal, int,  | decimal.Decimal,  | Number of inbound messages | [optional] value must be a 64 bit integer
**ManualCancel** | decimal.Decimal, int,  | decimal.Decimal,  | Number of manually cancelled messages | [optional] value must be a 64 bit integer
**NotDelivered** | decimal.Decimal, int,  | decimal.Decimal,  | Number of messages flagged with &#x27;Not Delivered&#x27; | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

