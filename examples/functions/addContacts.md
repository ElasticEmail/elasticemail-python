# Add Contacts

This example is aligned with the current SDK and can be run directly from `examples/functions/addContacts.py`.

```python
import ElasticEmail
from ElasticEmail.models.contact_status import ContactStatus
from ElasticEmail.models.contact_payload import ContactPayload
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = '6E313A3326A5C0A3D0C5F32916BE6EE3E858AA4C068829DEF4B6D21E0A12971AD60B3F92330DFDD1F193916BDE8444AF'

"""
Add contacts
Example api call that adds new contacts.
Pass array with contact details to add up to 1000 contacts.
Specify a list name in options or add to all contacts.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ContactsApi(api_client)
    contact_payload = [
        ContactPayload(
            Email="johnsmith@domain.com",
            Status=ContactStatus("Active"),
            FirstName="John",
            LastName="Smith",
        ),
    ]  # [ContactPayload]

    list_names = [
        "New list",
    ]  # [str] | Names of lists to which the uploaded contacts should be added to (optional)

    try:
        # Add Contact
        api_response = api_instance.contacts_post(contact_payload=contact_payload, listnames=list_names)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_post: %s\n" % e)
```

Run with:

```bash
py -3 addContacts.py
```
