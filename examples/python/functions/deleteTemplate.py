import ElasticEmail
from ElasticEmail.api import templates_api

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Delete template
Example api call that deletes existing template.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)

    name = "My new template"  # str | Name of template.

    try:
        # Delete Template
        api_instance.templates_by_name_delete(name)
        print("Template deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_by_name_delete: %s\n" % e)