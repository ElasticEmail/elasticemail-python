# ElasticEmail.model.split_options.SplitOptions

Optional A/X split campaign options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Optional A/X split campaign options | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**OptimizeFor** | [**SplitOptimizationType**](SplitOptimizationType.md) | [**SplitOptimizationType**](SplitOptimizationType.md) |  | [optional] 
**OptimizePeriodMinutes** | decimal.Decimal, int,  | decimal.Decimal,  | For how long should the results be measured until determining the winner template (content) | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

