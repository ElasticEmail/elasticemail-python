# ElasticEmail.model.email_job_status.EmailJobStatus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | str,  | str,  | ID number of your attachment | [optional] 
**Status** | str,  | str,  | Name of status: submitted, complete, in_progress | [optional] 
**RecipientsCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[Failed](#Failed)** | list, tuple,  | tuple,  |  | [optional] 
**FailedCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails failed. | [optional] value must be a 32 bit integer
**[Sent](#Sent)** | list, tuple,  | tuple,  |  | [optional] 
**SentCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails sent. | [optional] value must be a 32 bit integer
**[Delivered](#Delivered)** | list, tuple,  | tuple,  | Number of delivered messages | [optional] 
**DeliveredCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[Pending](#Pending)** | list, tuple,  | tuple,  |  | [optional] 
**PendingCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[Opened](#Opened)** | list, tuple,  | tuple,  | Number of opened messages | [optional] 
**OpenedCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails opened. | [optional] value must be a 32 bit integer
**[Clicked](#Clicked)** | list, tuple,  | tuple,  | Number of clicked messages | [optional] 
**ClickedCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails clicked | [optional] value must be a 32 bit integer
**[Unsubscribed](#Unsubscribed)** | list, tuple,  | tuple,  | Number of unsubscribed messages | [optional] 
**UnsubscribedCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total emails unsubscribed | [optional] value must be a 32 bit integer
**[AbuseReports](#AbuseReports)** | list, tuple,  | tuple,  |  | [optional] 
**AbuseReportsCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[MessageIDs](#MessageIDs)** | list, tuple,  | tuple,  | List of all MessageIDs for this job. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Failed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EmailJobFailedStatus**](EmailJobFailedStatus.md) | [**EmailJobFailedStatus**](EmailJobFailedStatus.md) | [**EmailJobFailedStatus**](EmailJobFailedStatus.md) |  | 

# Sent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Delivered

Number of delivered messages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Number of delivered messages | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Pending

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Opened

Number of opened messages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Number of opened messages | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Clicked

Number of clicked messages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Number of clicked messages | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Unsubscribed

Number of unsubscribed messages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Number of unsubscribed messages | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AbuseReports

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# MessageIDs

List of all MessageIDs for this job.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of all MessageIDs for this job. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

