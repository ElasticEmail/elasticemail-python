# CampaignTemplate

Content of a Campaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poolname** | **str** | Name of your custom IP Pool to be used in the sending process | [optional] 
**_from** | **str** | Your e-mail with an optional name (e.g.: John Doe &lt;email@domain.com&gt;) | [optional] 
**reply_to** | **str** | To what address should the recipients reply to (e.g. John Doe &lt;email@domain.com&gt;) | [optional] 
**subject** | **str** | Default subject of email. | [optional] 
**template_name** | **str** | Name of template. | [optional] 
**attach_files** | **[str]** | Names of previously uploaded files that should be sent as downloadable attachments | [optional] 
**utm** | **dict** | Utm marketing data to be attached to every link in this e-mail. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


