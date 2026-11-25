import os
import sys
import ElasticEmail
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Read the API key from the ELASTICEMAIL_API_KEY environment variable
api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key

"""
Load template
Example api call that loads an existing template.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.TemplatesApi(api_client)

    name = "hello_template"  # str | Name of template.

    try:
        # Load Template
        api_response = api_instance.templates_by_name_get(name)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_by_name_get: %s\n" % e)
