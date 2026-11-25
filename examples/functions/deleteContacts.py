import os
import sys
import ElasticEmail
from ElasticEmail.models.emails_payload import EmailsPayload

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Read the API key from the ELASTICEMAIL_API_KEY environment variable
api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key

"""
Delete contacts
Example api call that deletes contacts in bulk, by a list of email addresses.
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
