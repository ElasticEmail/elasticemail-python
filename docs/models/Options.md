# ElasticEmail.model.options.Options

E-mail configuration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | E-mail configuration | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**TimeOffset** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | By how long should an e-mail be delayed (in minutes). Maximum is 35 days. | [optional] value must be a 32 bit integer
**PoolName** | str,  | str,  | Name of your custom IP Pool to be used in the sending process | [optional] 
**ChannelName** | str,  | str,  | Name of selected channel. | [optional] 
**Encoding** | [**EncodingType**](EncodingType.md) | [**EncodingType**](EncodingType.md) |  | [optional] 
**TrackOpens** | bool,  | BoolClass,  | Should the opens be tracked? If no value has been provided, Account&#x27;s default setting will be used. | [optional] 
**TrackClicks** | bool,  | BoolClass,  | Should the clicks be tracked? If no value has been provided, Account&#x27;s default setting will be used. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

