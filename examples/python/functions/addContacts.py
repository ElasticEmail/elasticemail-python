import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.contact_status import ContactStatus
from ElasticEmail.model.contact_payload import ContactPayload
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Add contacts
Example api call that adds new contacts.
Pass array with contact details to add up to 1000 contacts.
Specify a list name in options or add to all contacts.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contacts_api.ContactsApi(api_client)
    contact_payload = [
        ContactPayload(
            email="johnsmith@domain.com",
            status=ContactStatus("Active"),
            first_name="John",
            last_name="Smith",
        ),
    ]  # [ContactPayload]

    list_names = [
        "New list",
    ]  # [str] | Names of lists to which the uploaded contacts should be added to (optional)

    try:
        # Add Contact
        api_response = api_instance.contacts_post(contact_payload, listnames=list_names)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_post: %s\n" % e)
