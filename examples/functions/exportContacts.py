import ElasticEmail
from ElasticEmail.models.export_file_formats import ExportFileFormats
from ElasticEmail.models.compression_format import CompressionFormat
from pprint import pprint

# Defining the host is optional and defaults to https://api.elasticemail.com/v4
configuration = ElasticEmail.Configuration()

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

"""
Export contacts
Example api call that exports selected contacts to downloadable file.
Options:
fileFormat: "Csv" "Xml" "Json" – Format of the exported file
emails: [mail@contact.com,mail1@contact.com,mail2@contact.com] – Array of contact emails
compressionFormat: "None" "Zip"
fileName=filename.txt – Name of your file including extension.
rule: rule="Status%20=%20Engaged" – Query used for filtering.
"""
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ElasticEmail.ContactsApi(api_client)

    try:
        # Export Contacts
        api_response = api_instance.contacts_export_post(
            file_format=ExportFileFormats("Csv"),
            compression_format=CompressionFormat("None"),
            file_name="exported.csv",
        )
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_export_post: %s\n" % e)
