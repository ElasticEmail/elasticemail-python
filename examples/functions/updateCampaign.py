import ElasticEmail
from ElasticEmail.apis.tags import campaigns_api
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
Update Campaign
Example api call that updates a campaign.
Send will be triggered immediately or postponed, depending on given options.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaigns_api.CampaignsApi(api_client)

    name = "hello campaign"

    campaign = Campaign(
        Content=[
            CampaignTemplate(
                From="test@email.test",
                ReplyTo="test@email.test",
                Subject="Hello",
                TemplateName="hello_template",
            ),
        ],
        Name="hello campaign update",
        Status=CampaignStatus("Draft"),
        Recipients=CampaignRecipient(
            ListNames=[
                "my list name",
            ],
        ),
    ) # Campaign | JSON representation of a campaign

    # example passing only required values which don't have defaults set
    try:
        # Add Campaign
        api_response = api_instance.campaigns_by_name_put(path_params = {'name': name}, body = campaign)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_put: %s\n" % e)
