# Add Campaign

This example is aligned with the current SDK and can be run directly from `examples/functions/addCampaign.py`.

```python
import ElasticEmail
from ElasticEmail.models.campaign import Campaign
from ElasticEmail.models.campaign_recipient import CampaignRecipient
from ElasticEmail.models.campaign_status import CampaignStatus
from ElasticEmail.models.campaign_template import CampaignTemplate
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Add Campaign
Example api call that creates a new campaign.
Send will be triggered immediately or postponed, depending on given options.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.CampaignsApi(api_client)

    campaign = Campaign(
        Content=[
            CampaignTemplate(
                From="example@email.test",
                ReplyTo="example@email.test",
                Subject="Hello",
                TemplateName="hello_template",
            ),
        ],
        Name="hello campaign",
        Status=CampaignStatus("Draft"),
        Recipients=CampaignRecipient(
            list_names=[
                "my list name",
            ],
        ),
    ) # Campaign | JSON representation of a campaign

    # example passing only required values which don't have defaults set
    try:
        # Add Campaign
        api_response = api_instance.campaigns_post(campaign=campaign)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_post: %s\n" % e)
```

Run with:

```bash
py -3 addCampaign.py
```
