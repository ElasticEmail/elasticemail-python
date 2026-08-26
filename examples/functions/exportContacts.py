import ElasticEmail
from ElasticEmail.apis.tags import contacts_api
from ElasticEmail.model.export_file_formats import ExportFileFormats
from ElasticEmail.model.compression_format import CompressionFormat
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
    api_instance = contacts_api.ContactsApi(api_client)

    query_params = {
        'fileFormat': ExportFileFormats("Csv"), # ExportFileFormats | Format of the exported file (optional)
        'compressionFormat': CompressionFormat("None"),  # CompressionFormat | FileResponse compression format. None or Zip. (optional)
        'fileName': "exported.csv", # str | Name of your file including extension. (optional)
    }

    try:
        # Export Contacts
        api_response = api_instance.contacts_export_post(query_params = query_params)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_export_post: %s\n" % e)
