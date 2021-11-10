# EmailContent

Proper e-mail content

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**[BodyPart]**](BodyPart.md) | List of e-mail body parts, with user-provided MIME types (text/html, text/plain etc) | [optional] 
**merge** | **{str: (str,)}** | A key-value collection of custom merge fields, shared between recipients. Should be used in e-mail body like so: {firstname}, {lastname} etc. | [optional] 
**attachments** | [**[MessageAttachment]**](MessageAttachment.md) | Attachments provided by sending binary data | [optional] 
**headers** | **{str: (str,)}** | A key-value collection of custom e-mail headers. | [optional] 
**postback** | **str** | Postback header. | [optional] 
**envelope_from** | **str** | E-mail with an optional name to be used as the envelope from address (e.g.: John Doe &lt;email@domain.com&gt;) | [optional] 
**_from** | **str** | Your e-mail with an optional name (e.g.: John Doe &lt;email@domain.com&gt;) | [optional] 
**reply_to** | **str** | To what address should the recipients reply to (e.g. John Doe &lt;email@domain.com&gt;) | [optional] 
**subject** | **str** | Default subject of email. | [optional] 
**template_name** | **str** | Name of template. | [optional] 
**attach_files** | **[str]** | Names of previously uploaded files that should be sent as downloadable attachments | [optional] 
**utm** | [**Utm**](Utm.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


