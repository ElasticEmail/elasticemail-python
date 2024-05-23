# ElasticEmail.model.email_content.EmailContent

Proper e-mail content

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Proper e-mail content | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**From** | str,  | str,  | Your e-mail with an optional name (e.g.: John Doe &lt;email@domain.com&gt;) | 
**[Body](#Body)** | list, tuple,  | tuple,  | List of e-mail body parts, with user-provided MIME types (text/html, text/plain etc) | [optional] 
**[Merge](#Merge)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A key-value collection of custom merge fields, shared between recipients. Should be used in e-mail body like so: {firstname}, {lastname} etc. | [optional] 
**[Attachments](#Attachments)** | list, tuple,  | tuple,  | Attachments provided by sending binary data | [optional] 
**[Headers](#Headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A key-value collection of custom e-mail headers. | [optional] 
**Postback** | str,  | str,  | Postback header. | [optional] 
**EnvelopeFrom** | str,  | str,  | E-mail with an optional name to be used as the envelope from address (e.g.: John Doe &lt;email@domain.com&gt;) | [optional] 
**ReplyTo** | str,  | str,  | To what address should the recipients reply to (e.g. John Doe &lt;email@domain.com&gt;) | [optional] 
**Subject** | str,  | str,  | Default subject of email. | [optional] 
**TemplateName** | str,  | str,  | Name of template. | [optional] 
**[AttachFiles](#AttachFiles)** | list, tuple,  | tuple,  | Names of previously uploaded files that should be sent as downloadable attachments | [optional] 
**Utm** | [**Utm**](Utm.md) | [**Utm**](Utm.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Body

List of e-mail body parts, with user-provided MIME types (text/html, text/plain etc)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of e-mail body parts, with user-provided MIME types (text/html, text/plain etc) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BodyPart**](BodyPart.md) | [**BodyPart**](BodyPart.md) | [**BodyPart**](BodyPart.md) |  | 

# Merge

A key-value collection of custom merge fields, shared between recipients. Should be used in e-mail body like so: {firstname}, {lastname} etc.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A key-value collection of custom merge fields, shared between recipients. Should be used in e-mail body like so: {firstname}, {lastname} etc. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# Attachments

Attachments provided by sending binary data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Attachments provided by sending binary data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MessageAttachment**](MessageAttachment.md) | [**MessageAttachment**](MessageAttachment.md) | [**MessageAttachment**](MessageAttachment.md) |  | 

# Headers

A key-value collection of custom e-mail headers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A key-value collection of custom e-mail headers. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

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

