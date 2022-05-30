import ElasticEmail
from ElasticEmail.api import campaigns_api
from ElasticEmail.model.campaign import Campaign
from ElasticEmail.model.campaign_recipient import CampaignRecipient
from ElasticEmail.model.campaign_status import CampaignStatus
from ElasticEmail.model.campaign_template import CampaignTemplate
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Add Campaign
Example api call that creates a new campaign.
Send will be triggered immediately or postponed, depending on given options.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaigns_api.CampaignsApi(api_client)

    campaign = Campaign(
        content=[
            CampaignTemplate(
                _from="karol.szczycinski@elasticemail.com",
                reply_to="karol.szczycinski@elasticemail.com",
                subject="Hello",
                template_name="hello_template",
            ),
        ],
        name="hello campaign",
        status=CampaignStatus("Draft"),
        recipients=CampaignRecipient(
            list_names=[
                "my list name",
            ],
        ),
    ) # Campaign | JSON representation of a campaign

    # example passing only required values which don't have defaults set
    try:
        # Add Campaign
        api_response = api_instance.campaigns_post(campaign)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_post: %s\n" % e)
