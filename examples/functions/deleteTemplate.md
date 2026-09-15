# Delete Template

This example is aligned with the current SDK and can be run directly from `examples/functions/deleteTemplate.py`.

```python
import ElasticEmail

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

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
```

Run with:

```bash
py -3 deleteTemplate.py
```
