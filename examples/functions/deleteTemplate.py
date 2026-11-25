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
Delete template
Example api call that deletes existing template.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.TemplatesApi(api_client)

    name = "My new template"  # str | Name of template.

    try:
        # Delete Template
        api_instance.templates_by_name_delete(name)
        print("Template deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_by_name_delete: %s\n" % e)
