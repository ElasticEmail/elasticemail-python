# EmailContent

Proper e-mail content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**List[BodyPart]**](BodyPart.md) | List of e-mail body parts, with user-provided MIME types (text/html, text/plain etc) | [optional] 
**merge** | **Dict[str, str]** | A key-value collection of custom merge fields, shared between recipients. Should be used in e-mail body like so: {firstname}, {lastname} etc. | [optional] 
**attachments** | [**List[MessageAttachment]**](MessageAttachment.md) | Attachments provided by sending binary data | [optional] 
**headers** | **Dict[str, str]** | A key-value collection of custom e-mail headers. | [optional] 
**postback** | **str** | Postback header. | [optional] 
**envelope_from** | **str** | E-mail with an optional name to be used as the envelope from address (e.g.: John Doe &lt;email@domain.com&gt;) | [optional] 
**var_from** | **str** | Your e-mail with an optional name (e.g.: John Doe &lt;email@domain.com&gt;) | 
**reply_to** | **str** | To what address should the recipients reply to (e.g. John Doe &lt;email@domain.com&gt;) | [optional] 
**subject** | **str** | Default subject of email. | [optional] 
**template_name** | **str** | Name of template. | [optional] 
**attach_files** | **List[str]** | Names of previously uploaded files that should be sent as downloadable attachments | [optional] 
**utm** | [**Utm**](Utm.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.email_content import EmailContent

# TODO update the JSON string below
json = "{}"
# create an instance of EmailContent from a JSON string
email_content_instance = EmailContent.from_json(json)
# print the JSON string representation of the object
print(EmailContent.to_json())

# convert the object into a dict
email_content_dict = email_content_instance.to_dict()
# create an instance of EmailContent from a dict
email_content_from_dict = EmailContent.from_dict(email_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


