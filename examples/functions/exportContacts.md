# Export Contacts

This guide will walk you through the process of exporting selected contacts to downloadable file using the Python library. 

*Required Access Level: Export*

## What's a contact?
When using Elastic Email, you send emails to contacts – recipients who receive your emails. Contacts can be grouped by created segments or lists.

## Preparation
Install Python 3.

Install ElasticEmail library.

Eg. run in terminal `pip install ElasticEmail` to install from PyPi repository.

Create a new Python file `snippet.py` and open it in editor of your preference eg. PyCharm (https://www.jetbrains.com/pycharm/download/)

## Let's dig into the code

Put the below code to your file.

Load libraries using below code:

```python
import ElasticEmail
from ElasticEmail.models.export_file_formats import ExportFileFormats
from ElasticEmail.models.compression_format import CompressionFormat
from pprint import pprint
```

Generate and use your API key (remember to check a required access level).

Defining the host is optional and defaults to https://api.elasticemail.com/v4

```python
configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
```

Pass configuration to an api client and make it instance available under `api_client` name:
```
with ElasticEmail.ApiClient(configuration) as api_client:
```

Create an instance of ContactsApi that will be used to create a file with exported contacts.

```python
    api_instance = ElasticEmail.ContactsApi(api_client)
```

Create options variables:
- fileFormat - specify format in which file should be created, options are: "Csv" "Xml" "Json".
- emails - select contacts to export by providing array of emails
- fileName - you can specify file name of your choice

Other options:
- rule - eg. `rule=Status%20=%20Engaged` – Query used for filtering
- compressionFormat - "None" or "Zip"

> Find out more by checking our API's documentation: https://elasticemail.com/developers/api-documentation/rest-api#operation/contactsExportPost

```python
            file_format=ExportFileFormats("Csv"),
            compression_format=CompressionFormat("None"),
            file_name="exported.csv",
```

Use try & except block to call `contacts_export_post` method from the API to export contacts: 

```python
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
```


## The whole code to copy and paste:

```python
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
```

## Run the code
```
python3 snippet.py
```
