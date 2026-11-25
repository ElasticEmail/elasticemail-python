import os
import sys
import ElasticEmail

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Read the API key from the ELASTICEMAIL_API_KEY environment variable
api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key

"""
Delete Campaign
Example api call that deletes an existing campaign.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.CampaignsApi(api_client)

    name = "hello campaign"

    try:
        # Delete Campaign
        api_instance.campaigns_by_name_delete(name)
        print("Campaign deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_delete: %s\n" % e)
