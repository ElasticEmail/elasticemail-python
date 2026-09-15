# Delete Contacts

This example is aligned with the current SDK and can be run directly from `examples/functions/deleteContacts.py`.

```python
import ElasticEmail
from ElasticEmail.models.emails_payload import EmailsPayload

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Delete contact
Example api call that deletes given contact(s).
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ContactsApi(api_client)

    emails_payload = EmailsPayload(
        Emails=["johnsmith@domain.com"],
    )  # EmailsPayload | Provide either rule or a list of emails, not both.

    try:
        # Delete Contacts Bulk
        api_instance.contacts_delete_post(emails_payload)
        print("Contacts deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_delete_post: %s\n" % e)
```

Run with:

```bash
py -3 deleteContacts.py
```
