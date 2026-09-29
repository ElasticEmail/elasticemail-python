import ElasticEmail

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
    api_instance = ElasticEmail.ContactsApi(api_client)

    try:
        with open('./files/contacts.csv', 'rb') as contacts_file:
            api_instance.contacts_import_post(
                list_name="example list",
                encoding_name="utf-8",
                file=contacts_file.read(),
            )
            print("Contacts uploaded.")
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_import_post: %s\n" % e)
