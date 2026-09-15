# Add Template

This example is aligned with the current SDK and can be run directly from `examples/functions/addTemplate.py`.

```python
import ElasticEmail
from ElasticEmail.models.template_payload import TemplatePayload
from ElasticEmail.models.body_part import BodyPart
from ElasticEmail.models.body_content_type import BodyContentType
from ElasticEmail.models.template_scope import TemplateScope
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Add Template
Example api call that adds a new template.
TemplateScope: "Personal" or "Global"
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.TemplatesApi(api_client)

    template_payload = TemplatePayload(
        Name="My new template",
        Subject="Default subject",
        Body=[
            BodyPart(
                ContentType=BodyContentType("HTML"),
                Content="My template",
                Charset="utf-8",
            ),
        ],
        TemplateScope=TemplateScope("Personal"),
    )  # TemplatePayload |

    try:
        api_response = api_instance.templates_post(template_payload=template_payload)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling TemplatesApi->templates_post: %s\n" % e)
```

Run with:

```bash
py -3 addTemplate.py
```
