import os
import sys
import ElasticEmail

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Read the API key from the ELASTICEMAIL_API_KEY environment variable
api_key = os.environ.get('ELASTICEMAIL_API_KEY')
if not api_key:
    sys.exit('Set the ELASTICEMAIL_API_KEY environment variable to your Elastic Email API key.')
configuration.api_key['apikey'] = api_key

"""
Delete contact
Example api call that deletes one contact by its email address.
Required Access Level: ModifyContacts
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ContactsApi(api_client)

    email = "johnsmith@domain.com"  # str | Proper email address.

    try:
        # Delete Contact
        api_instance.contacts_by_email_delete(email)
        print("Contact deleted.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_by_email_delete: %s\n" % e)
