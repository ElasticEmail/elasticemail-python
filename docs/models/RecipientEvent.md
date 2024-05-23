# ElasticEmail.model.recipient_event.RecipientEvent

Detailed information about message recipient

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Detailed information about message recipient | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**TransactionID** | str,  | str,  | ID number of transaction | [optional] 
**MsgID** | str,  | str,  | ID number of selected message. | [optional] 
**FromEmail** | str,  | str,  | Default From: email address. | [optional] 
**To** | str,  | str,  | Ending date for search in YYYY-MM-DDThh:mm:ss format. | [optional] 
**Subject** | str,  | str,  | Default subject of email. | [optional] 
**EventType** | [**EventType**](EventType.md) | [**EventType**](EventType.md) |  | [optional] 
**EventDate** | str, datetime,  | str,  | Creation date | [optional] value must conform to RFC-3339 date-time
**ChannelName** | str,  | str,  | Name of selected channel. | [optional] 
**MessageCategory** | [**MessageCategory**](MessageCategory.md) | [**MessageCategory**](MessageCategory.md) |  | [optional] 
**NextTryOn** | None, str, datetime,  | NoneClass, str,  | Date of next try | [optional] value must conform to RFC-3339 date-time
**Message** | str,  | str,  | Content of message, HTML encoded | [optional] 
**IPAddress** | str,  | str,  | IP which this email was sent through | [optional] 
**PoolName** | str,  | str,  | Name of an IP pool this email was sent through | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

