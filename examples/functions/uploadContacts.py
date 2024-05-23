import ElasticEmail
from ElasticEmail.apis.tags import contacts_api

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Upload contacts
Example api call that adds new contacts by uploading csv file.
Required columns in CSV file: Email. 
Suggested columns in CSV file: AllowUnsubscribe, Status, ConsentDate, ConsentIP, ConsentTracking.

Example CSV file content:

Email
john@domain.com
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contacts_api.ContactsApi(api_client)

    query_params = {
        'listName': "example list",  # str | Name of an existing list to add these contacts to (optional)
        'encodingName': "utf-8",  # str | In what encoding the file is uploaded (optional)
    }

    body = dict(
        file = open('./files/contacts.csv', 'rb'),
    )

    try:
        api_instance.contacts_import_post(query_params=query_params, body=body)
        print("Contacts uploaded.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_import_post: %s\n" % e)
