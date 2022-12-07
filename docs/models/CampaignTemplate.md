# ElasticEmail.model.campaign_template.CampaignTemplate

Content of a Campaign

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Content of a Campaign | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Poolname** | str,  | str,  | Name of your custom IP Pool to be used in the sending process | [optional] 
**From** | str,  | str,  | Your e-mail with an optional name (e.g.: John Doe &lt;email@domain.com&gt;) | [optional] 
**ReplyTo** | str,  | str,  | To what address should the recipients reply to (e.g. John Doe &lt;email@domain.com&gt;) | [optional] 
**Subject** | str,  | str,  | Default subject of email. | [optional] 
**TemplateName** | str,  | str,  | Name of template. | [optional] 
**[AttachFiles](#AttachFiles)** | list, tuple,  | tuple,  | Names of previously uploaded files that should be sent as downloadable attachments | [optional] 
**Utm** | [**Utm**](Utm.md) | [**Utm**](Utm.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# AttachFiles

Names of previously uploaded files that should be sent as downloadable attachments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Names of previously uploaded files that should be sent as downloadable attachments | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

