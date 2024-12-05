# CampaignTemplate

Content of a Campaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poolname** | **str** | Name of your custom IP Pool to be used in the sending process | [optional] 
**var_from** | **str** | Your e-mail with an optional name (e.g.: John Doe &lt;email@domain.com&gt;) | 
**reply_to** | **str** | To what address should the recipients reply to (e.g. John Doe &lt;email@domain.com&gt;) | [optional] 
**subject** | **str** | Default subject of email. | [optional] 
**template_name** | **str** | Name of template. | [optional] 
**attach_files** | **List[str]** | Names of previously uploaded files that should be sent as downloadable attachments | [optional] 
**utm** | [**Utm**](Utm.md) |  | [optional] 

## Example

```python
from ElasticEmail.models.campaign_template import CampaignTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignTemplate from a JSON string
campaign_template_instance = CampaignTemplate.from_json(json)
# print the JSON string representation of the object
print(CampaignTemplate.to_json())

# convert the object into a dict
campaign_template_dict = campaign_template_instance.to_dict()
# create an instance of CampaignTemplate from a dict
campaign_template_from_dict = CampaignTemplate.from_dict(campaign_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


