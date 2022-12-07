# ElasticEmail.model.template.Template

Template info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Template info | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**TemplateType** | [**TemplateType**](TemplateType.md) | [**TemplateType**](TemplateType.md) |  | [optional] 
**Name** | str,  | str,  | Template name | [optional] 
**DateAdded** | str, datetime,  | str,  | Date of creation in YYYY-MM-DDThh:ii:ss format | [optional] value must conform to RFC-3339 date-time
**Subject** | str,  | str,  | Default subject of email. | [optional] 
**[Body](#Body)** | list, tuple,  | tuple,  | Email content of this template | [optional] 
**TemplateScope** | [**TemplateScope**](TemplateScope.md) | [**TemplateScope**](TemplateScope.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Body

Email content of this template

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Email content of this template | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BodyPart**](BodyPart.md) | [**BodyPart**](BodyPart.md) | [**BodyPart**](BodyPart.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

