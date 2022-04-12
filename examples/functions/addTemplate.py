import ElasticEmail
from ElasticEmail.api import templates_api
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.template_payload import TemplatePayload
from ElasticEmail.model.template_scope import TemplateScope
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Add Template
Example api call that adds a new template.
TemplateScope: "Personal" or "Global"
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)

    template_payload = TemplatePayload(
        name="My new template",
        subject="Default subject",
        body=[
            BodyPart(
                content_type=BodyContentType("HTML"),
                content="My template",
                charset="utf-8",
            ),
        ],
        template_scope=TemplateScope("Personal"),
    )  # TemplatePayload |

    try:
        api_response = api_instance.templates_post(template_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_post: %s\n" % e)
