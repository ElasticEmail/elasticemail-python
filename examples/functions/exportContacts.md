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
from ElasticEmail.apis.tags import contacts_api
from ElasticEmail.model.export_file_formats import ExportFileFormats
from ElasticEmail.model.compression_format import CompressionFormat
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
    api_instance = contacts_api.ContactsApi(api_client)
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
    query_params = {
        'fileFormat': ExportFileFormats("Csv"), # ExportFileFormats | Format of the exported file (optional)
        'compressionFormat': CompressionFormat("None"),  # CompressionFormat | FileResponse compression format. None or Zip. (optional)
        'fileName': "exported.csv", # str | Name of your file including extension. (optional)
    }
```

Use try & except block to call `contacts_export_post` method from the API to export contacts: 

```python
    try:
        api_response = api_instance.contacts_export_post(query_params = query_params)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_export_post: %s\n" % e)

```


## The whole code to copy and paste:

```python
import ElasticEmail
from ElasticEmail.apis.tags import contacts_api
from ElasticEmail.model.export_file_formats import ExportFileFormats
from ElasticEmail.model.compression_format import CompressionFormat
from pprint import pprint

configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = contacts_api.ContactsApi(api_client)

    query_params = {
        'fileFormat': ExportFileFormats("Csv"), # ExportFileFormats | Format of the exported file (optional)
        'compressionFormat': CompressionFormat("None"),  # CompressionFormat | FileResponse compression format. None or Zip. (optional)
        'fileName': "exported.csv", # str | Name of your file including extension. (optional)
    }

    try:
        api_response = api_instance.contacts_export_post(query_params = query_params)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling ContactsApi->contacts_export_post: %s\n" % e)
```

## Run the code
```
python3 snippet.py
```
