# ElasticEmail.model.contact_activity.ContactActivity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**TotalSent** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails sent. | [optional] value must be a 32 bit integer
**TotalOpened** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails opened. | [optional] value must be a 32 bit integer
**TotalClicked** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails clicked | [optional] value must be a 32 bit integer
**TotalFailed** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails failed. | [optional] value must be a 32 bit integer
**LastSent** | None, str, datetime,  | NoneClass, str,  | Last date when an email was sent to this contact | [optional] value must conform to RFC-3339 date-time
**LastOpened** | None, str, datetime,  | NoneClass, str,  | Date this contact last opened an email | [optional] value must conform to RFC-3339 date-time
**LastClicked** | None, str, datetime,  | NoneClass, str,  | Date this contact last clicked an email | [optional] value must conform to RFC-3339 date-time
**LastFailed** | None, str, datetime,  | NoneClass, str,  | Last date when an email sent to this contact bounced | [optional] value must conform to RFC-3339 date-time
**LastIP** | str,  | str,  | IP from which this contact opened or clicked their email last time | [optional] 
**ErrorCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Last RFC Error code if any occurred | [optional] value must be a 32 bit integer
**FriendlyErrorMessage** | str,  | str,  | Last RFC error message if any occurred | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

