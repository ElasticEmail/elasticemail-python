import ElasticEmail
from ElasticEmail.api import contacts_api
from ElasticEmail.model.emails_payload import EmailsPayload

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Delete contact
Example api call that deletes given contact(s).
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contacts_api.ContactsApi(api_client)

    emails_payload = EmailsPayload(
        emails=["johnsmith@domain.com"],
    )  # EmailsPayload | Provide either rule or a list of emails, not both.

    try:
        # Delete Contacts Bulk
        api_instance.contacts_delete_post(emails_payload)
        print("Contacts deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_delete_post: %s\n" % e)
