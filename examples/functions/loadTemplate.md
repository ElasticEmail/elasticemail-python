# Load Template

This example is aligned with the current SDK and can be run directly from `examples/functions/loadTemplate.py`.

```python
import ElasticEmail
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

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
        try:
            available = api_instance.templates_get(
                scope_type=[
                    ElasticEmail.TemplateScope("Personal"),
                    ElasticEmail.TemplateScope("Global"),
                ],
                limit=1,
                offset=0,
            )
            if available:
                fallback_name = available[0].name
                api_response = api_instance.templates_by_name_get(fallback_name)
                pprint(api_response)
                raise SystemExit(0)
        except ElasticEmail.ApiException:
            pass
        print(f"No template found to load ({e.status}). Skipping.")
```

Run with:

```bash
py -3 loadTemplate.py
```
