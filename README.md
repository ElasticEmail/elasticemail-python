# ElasticEmail
This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.

Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.

The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.

To start using this API, you will need your Access Token (available [here](https://app.elasticemail.com/marketing/settings/new/manage-api)). Remember to keep it safe. Required access levels are listed in the given request’s description.

Downloadable library clients can be found in our Github repository [here](https://github.com/ElasticEmail/elasticemail-python)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 4.0.0
- Package version: 4.1.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/elasticemail/elasticemail-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/elasticemail/elasticemail-python.git`)

Then import the package:
```python
import ElasticEmail
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ElasticEmail
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ElasticEmail
from pprint import pprint
from ElasticEmail.apis.tags import campaigns_api
from ElasticEmail.model.campaign import Campaign
# Defining the host is optional and defaults to https://api.elasticemail.com/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = campaigns_api.CampaignsApi(api_client)
    name = "name_example" # str | Name of Campaign to delete

    try:
        # Delete Campaign
        api_instance.campaigns_by_name_delete(name)
    except ElasticEmail.ApiException as e:
        print("Exception when calling CampaignsApi->campaigns_by_name_delete: %s\n" % e)
```


## Examples

Function ||
------------ | ------------- 
[addCampaign](examples/functions/addCampaign.py) | [readme](examples/functions/addCampaign.md)
[addContacts](examples/functions/addContacts.py) | [readme](examples/functions/addContacts.md)
[addList](examples/functions/addList.py) | [readme](examples/functions/addList.md)
[addTemplate](examples/functions/addTemplate.py) | [readme](examples/functions/addTemplate.md)
[deleteCampaign](examples/functions/deleteCampaign.py) | [readme](examples/functions/deleteCampaign.md)
[deleteContacts](examples/functions/deleteContacts.py) | [readme](examples/functions/deleteContacts.md)
[deleteList](examples/functions/deleteList.py) | [readme](examples/functions/deleteList.md)
[deleteTemplate](examples/functions/deleteTemplate.py) | [readme](examples/functions/deleteTemplate.md)
[exportContacts](examples/functions/exportContacts.py) | [readme](examples/functions/exportContacts.md)
[loadCampaign](examples/functions/loadCampaign.py) | [readme](examples/functions/loadCampaign.md)
[loadCampaignsStats](examples/functions/loadCampaignsStats.py) | [readme](examples/functions/loadCampaignsStats.md)
[loadChannelsStats](examples/functions/loadChannelsStats.py) | [readme](examples/functions/loadChannelsStats.md)
[loadList](examples/functions/loadList.py) | [readme](examples/functions/loadList.md)
[loadStatistics](examples/functions/loadStatistics.py) | [readme](examples/functions/loadStatistics.md)
[loadTemplate](examples/functions/loadTemplate.py) | [readme](examples/functions/loadTemplate.md)
[sendBulkEmails](examples/functions/sendBulkEmails.py) | [readme](examples/functions/sendBulkEmails.md)
[sendTransactionalEmails](examples/functions/sendTransactionalEmails.py) | [readme](examples/functions/sendTransactionalEmails.md)
[updateCampaign](examples/functions/updateCampaign.py) | [readme](examples/functions/updateCampaign.md)
[uploadContacts](examples/functions/uploadContacts.py) | [readme](examples/functions/uploadContacts.md)

## Documentation for API Endpoints

All URIs are relative to *https://api.elasticemail.com/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CampaignsApi* | [**campaigns_by_name_delete**](docs/apis/tags/CampaignsApi.md#campaigns_by_name_delete) | **delete** /campaigns/{name} | Delete Campaign
*CampaignsApi* | [**campaigns_by_name_get**](docs/apis/tags/CampaignsApi.md#campaigns_by_name_get) | **get** /campaigns/{name} | Load Campaign
*CampaignsApi* | [**campaigns_by_name_put**](docs/apis/tags/CampaignsApi.md#campaigns_by_name_put) | **put** /campaigns/{name} | Update Campaign
*CampaignsApi* | [**campaigns_get**](docs/apis/tags/CampaignsApi.md#campaigns_get) | **get** /campaigns | Load Campaigns
*CampaignsApi* | [**campaigns_post**](docs/apis/tags/CampaignsApi.md#campaigns_post) | **post** /campaigns | Add Campaign
*ContactsApi* | [**contacts_by_email_delete**](docs/apis/tags/ContactsApi.md#contacts_by_email_delete) | **delete** /contacts/{email} | Delete Contact
*ContactsApi* | [**contacts_by_email_get**](docs/apis/tags/ContactsApi.md#contacts_by_email_get) | **get** /contacts/{email} | Load Contact
*ContactsApi* | [**contacts_by_email_put**](docs/apis/tags/ContactsApi.md#contacts_by_email_put) | **put** /contacts/{email} | Update Contact
*ContactsApi* | [**contacts_delete_post**](docs/apis/tags/ContactsApi.md#contacts_delete_post) | **post** /contacts/delete | Delete Contacts Bulk
*ContactsApi* | [**contacts_export_by_id_status_get**](docs/apis/tags/ContactsApi.md#contacts_export_by_id_status_get) | **get** /contacts/export/{id}/status | Check Export Status
*ContactsApi* | [**contacts_export_post**](docs/apis/tags/ContactsApi.md#contacts_export_post) | **post** /contacts/export | Export Contacts
*ContactsApi* | [**contacts_get**](docs/apis/tags/ContactsApi.md#contacts_get) | **get** /contacts | Load Contacts
*ContactsApi* | [**contacts_import_post**](docs/apis/tags/ContactsApi.md#contacts_import_post) | **post** /contacts/import | Upload Contacts
*ContactsApi* | [**contacts_post**](docs/apis/tags/ContactsApi.md#contacts_post) | **post** /contacts | Add Contact
*EmailsApi* | [**emails_by_msgid_view_get**](docs/apis/tags/EmailsApi.md#emails_by_msgid_view_get) | **get** /emails/{msgid}/view | View Email
*EmailsApi* | [**emails_by_transactionid_status_get**](docs/apis/tags/EmailsApi.md#emails_by_transactionid_status_get) | **get** /emails/{transactionid}/status | Get Status
*EmailsApi* | [**emails_mergefile_post**](docs/apis/tags/EmailsApi.md#emails_mergefile_post) | **post** /emails/mergefile | Send Bulk Emails CSV
*EmailsApi* | [**emails_post**](docs/apis/tags/EmailsApi.md#emails_post) | **post** /emails | Send Bulk Emails
*EmailsApi* | [**emails_transactional_post**](docs/apis/tags/EmailsApi.md#emails_transactional_post) | **post** /emails/transactional | Send Transactional Email
*EventsApi* | [**events_by_transactionid_get**](docs/apis/tags/EventsApi.md#events_by_transactionid_get) | **get** /events/{transactionid} | Load Email Events
*EventsApi* | [**events_channels_by_name_export_post**](docs/apis/tags/EventsApi.md#events_channels_by_name_export_post) | **post** /events/channels/{name}/export | Export Channel Events
*EventsApi* | [**events_channels_by_name_get**](docs/apis/tags/EventsApi.md#events_channels_by_name_get) | **get** /events/channels/{name} | Load Channel Events
*EventsApi* | [**events_channels_export_by_id_status_get**](docs/apis/tags/EventsApi.md#events_channels_export_by_id_status_get) | **get** /events/channels/export/{id}/status | Check Channel Export Status
*EventsApi* | [**events_export_by_id_status_get**](docs/apis/tags/EventsApi.md#events_export_by_id_status_get) | **get** /events/export/{id}/status | Check Export Status
*EventsApi* | [**events_export_post**](docs/apis/tags/EventsApi.md#events_export_post) | **post** /events/export | Export Events
*EventsApi* | [**events_get**](docs/apis/tags/EventsApi.md#events_get) | **get** /events | Load Events
*FilesApi* | [**files_by_name_delete**](docs/apis/tags/FilesApi.md#files_by_name_delete) | **delete** /files/{name} | Delete File
*FilesApi* | [**files_by_name_get**](docs/apis/tags/FilesApi.md#files_by_name_get) | **get** /files/{name} | Download File
*FilesApi* | [**files_by_name_info_get**](docs/apis/tags/FilesApi.md#files_by_name_info_get) | **get** /files/{name}/info | Load File Details
*FilesApi* | [**files_get**](docs/apis/tags/FilesApi.md#files_get) | **get** /files | List Files
*FilesApi* | [**files_post**](docs/apis/tags/FilesApi.md#files_post) | **post** /files | Upload File
*InboundRouteApi* | [**inboundroute_by_id_delete**](docs/apis/tags/InboundRouteApi.md#inboundroute_by_id_delete) | **delete** /inboundroute/{id} | Delete Route
*InboundRouteApi* | [**inboundroute_by_id_get**](docs/apis/tags/InboundRouteApi.md#inboundroute_by_id_get) | **get** /inboundroute/{id} | Get Route
*InboundRouteApi* | [**inboundroute_by_id_put**](docs/apis/tags/InboundRouteApi.md#inboundroute_by_id_put) | **put** /inboundroute/{id} | Update Route
*InboundRouteApi* | [**inboundroute_get**](docs/apis/tags/InboundRouteApi.md#inboundroute_get) | **get** /inboundroute | Get Routes
*InboundRouteApi* | [**inboundroute_order_put**](docs/apis/tags/InboundRouteApi.md#inboundroute_order_put) | **put** /inboundroute/order | Update Sorting
*InboundRouteApi* | [**inboundroute_post**](docs/apis/tags/InboundRouteApi.md#inboundroute_post) | **post** /inboundroute | Create Route
*ListsApi* | [**lists_by_listname_contacts_get**](docs/apis/tags/ListsApi.md#lists_by_listname_contacts_get) | **get** /lists/{listname}/contacts | Load Contacts in List
*ListsApi* | [**lists_by_name_contacts_post**](docs/apis/tags/ListsApi.md#lists_by_name_contacts_post) | **post** /lists/{name}/contacts | Add Contacts to List
*ListsApi* | [**lists_by_name_contacts_remove_post**](docs/apis/tags/ListsApi.md#lists_by_name_contacts_remove_post) | **post** /lists/{name}/contacts/remove | Remove Contacts from List
*ListsApi* | [**lists_by_name_delete**](docs/apis/tags/ListsApi.md#lists_by_name_delete) | **delete** /lists/{name} | Delete List
*ListsApi* | [**lists_by_name_get**](docs/apis/tags/ListsApi.md#lists_by_name_get) | **get** /lists/{name} | Load List
*ListsApi* | [**lists_by_name_put**](docs/apis/tags/ListsApi.md#lists_by_name_put) | **put** /lists/{name} | Update List
*ListsApi* | [**lists_get**](docs/apis/tags/ListsApi.md#lists_get) | **get** /lists | Load Lists
*ListsApi* | [**lists_post**](docs/apis/tags/ListsApi.md#lists_post) | **post** /lists | Add List
*SecurityApi* | [**security_apikeys_by_name_delete**](docs/apis/tags/SecurityApi.md#security_apikeys_by_name_delete) | **delete** /security/apikeys/{name} | Delete ApiKey
*SecurityApi* | [**security_apikeys_by_name_get**](docs/apis/tags/SecurityApi.md#security_apikeys_by_name_get) | **get** /security/apikeys/{name} | Load ApiKey
*SecurityApi* | [**security_apikeys_by_name_put**](docs/apis/tags/SecurityApi.md#security_apikeys_by_name_put) | **put** /security/apikeys/{name} | Update ApiKey
*SecurityApi* | [**security_apikeys_get**](docs/apis/tags/SecurityApi.md#security_apikeys_get) | **get** /security/apikeys | List ApiKeys
*SecurityApi* | [**security_apikeys_post**](docs/apis/tags/SecurityApi.md#security_apikeys_post) | **post** /security/apikeys | Add ApiKey
*SecurityApi* | [**security_smtp_by_name_delete**](docs/apis/tags/SecurityApi.md#security_smtp_by_name_delete) | **delete** /security/smtp/{name} | Delete SMTP Credential
*SecurityApi* | [**security_smtp_by_name_get**](docs/apis/tags/SecurityApi.md#security_smtp_by_name_get) | **get** /security/smtp/{name} | Load SMTP Credential
*SecurityApi* | [**security_smtp_by_name_put**](docs/apis/tags/SecurityApi.md#security_smtp_by_name_put) | **put** /security/smtp/{name} | Update SMTP Credential
*SecurityApi* | [**security_smtp_get**](docs/apis/tags/SecurityApi.md#security_smtp_get) | **get** /security/smtp | List SMTP Credentials
*SecurityApi* | [**security_smtp_post**](docs/apis/tags/SecurityApi.md#security_smtp_post) | **post** /security/smtp | Add SMTP Credential
*SegmentsApi* | [**segments_by_name_delete**](docs/apis/tags/SegmentsApi.md#segments_by_name_delete) | **delete** /segments/{name} | Delete Segment
*SegmentsApi* | [**segments_by_name_get**](docs/apis/tags/SegmentsApi.md#segments_by_name_get) | **get** /segments/{name} | Load Segment
*SegmentsApi* | [**segments_by_name_put**](docs/apis/tags/SegmentsApi.md#segments_by_name_put) | **put** /segments/{name} | Update Segment
*SegmentsApi* | [**segments_get**](docs/apis/tags/SegmentsApi.md#segments_get) | **get** /segments | Load Segments
*SegmentsApi* | [**segments_post**](docs/apis/tags/SegmentsApi.md#segments_post) | **post** /segments | Add Segment
*StatisticsApi* | [**statistics_campaigns_by_name_get**](docs/apis/tags/StatisticsApi.md#statistics_campaigns_by_name_get) | **get** /statistics/campaigns/{name} | Load Campaign Stats
*StatisticsApi* | [**statistics_campaigns_get**](docs/apis/tags/StatisticsApi.md#statistics_campaigns_get) | **get** /statistics/campaigns | Load Campaigns Stats
*StatisticsApi* | [**statistics_channels_by_name_get**](docs/apis/tags/StatisticsApi.md#statistics_channels_by_name_get) | **get** /statistics/channels/{name} | Load Channel Stats
*StatisticsApi* | [**statistics_channels_get**](docs/apis/tags/StatisticsApi.md#statistics_channels_get) | **get** /statistics/channels | Load Channels Stats
*StatisticsApi* | [**statistics_get**](docs/apis/tags/StatisticsApi.md#statistics_get) | **get** /statistics | Load Statistics
*SubAccountsApi* | [**subaccounts_by_email_credits_patch**](docs/apis/tags/SubAccountsApi.md#subaccounts_by_email_credits_patch) | **patch** /subaccounts/{email}/credits | Add, Subtract Email Credits
*SubAccountsApi* | [**subaccounts_by_email_delete**](docs/apis/tags/SubAccountsApi.md#subaccounts_by_email_delete) | **delete** /subaccounts/{email} | Delete SubAccount
*SubAccountsApi* | [**subaccounts_by_email_get**](docs/apis/tags/SubAccountsApi.md#subaccounts_by_email_get) | **get** /subaccounts/{email} | Load SubAccount
*SubAccountsApi* | [**subaccounts_by_email_settings_email_put**](docs/apis/tags/SubAccountsApi.md#subaccounts_by_email_settings_email_put) | **put** /subaccounts/{email}/settings/email | Update SubAccount Email Settings
*SubAccountsApi* | [**subaccounts_get**](docs/apis/tags/SubAccountsApi.md#subaccounts_get) | **get** /subaccounts | Load SubAccounts
*SubAccountsApi* | [**subaccounts_post**](docs/apis/tags/SubAccountsApi.md#subaccounts_post) | **post** /subaccounts | Add SubAccount
*SuppressionsApi* | [**suppressions_bounces_get**](docs/apis/tags/SuppressionsApi.md#suppressions_bounces_get) | **get** /suppressions/bounces | Get Bounce List
*SuppressionsApi* | [**suppressions_bounces_import_post**](docs/apis/tags/SuppressionsApi.md#suppressions_bounces_import_post) | **post** /suppressions/bounces/import | Add Bounces Async
*SuppressionsApi* | [**suppressions_bounces_post**](docs/apis/tags/SuppressionsApi.md#suppressions_bounces_post) | **post** /suppressions/bounces | Add Bounces
*SuppressionsApi* | [**suppressions_by_email_delete**](docs/apis/tags/SuppressionsApi.md#suppressions_by_email_delete) | **delete** /suppressions/{email} | Delete Suppression
*SuppressionsApi* | [**suppressions_by_email_get**](docs/apis/tags/SuppressionsApi.md#suppressions_by_email_get) | **get** /suppressions/{email} | Get Suppression
*SuppressionsApi* | [**suppressions_complaints_get**](docs/apis/tags/SuppressionsApi.md#suppressions_complaints_get) | **get** /suppressions/complaints | Get Complaints List
*SuppressionsApi* | [**suppressions_complaints_import_post**](docs/apis/tags/SuppressionsApi.md#suppressions_complaints_import_post) | **post** /suppressions/complaints/import | Add Complaints Async
*SuppressionsApi* | [**suppressions_complaints_post**](docs/apis/tags/SuppressionsApi.md#suppressions_complaints_post) | **post** /suppressions/complaints | Add Complaints
*SuppressionsApi* | [**suppressions_get**](docs/apis/tags/SuppressionsApi.md#suppressions_get) | **get** /suppressions | Get Suppressions
*SuppressionsApi* | [**suppressions_unsubscribes_get**](docs/apis/tags/SuppressionsApi.md#suppressions_unsubscribes_get) | **get** /suppressions/unsubscribes | Get Unsubscribes List
*SuppressionsApi* | [**suppressions_unsubscribes_import_post**](docs/apis/tags/SuppressionsApi.md#suppressions_unsubscribes_import_post) | **post** /suppressions/unsubscribes/import | Add Unsubscribes Async
*SuppressionsApi* | [**suppressions_unsubscribes_post**](docs/apis/tags/SuppressionsApi.md#suppressions_unsubscribes_post) | **post** /suppressions/unsubscribes | Add Unsubscribes
*TemplatesApi* | [**templates_by_name_delete**](docs/apis/tags/TemplatesApi.md#templates_by_name_delete) | **delete** /templates/{name} | Delete Template
*TemplatesApi* | [**templates_by_name_get**](docs/apis/tags/TemplatesApi.md#templates_by_name_get) | **get** /templates/{name} | Load Template
*TemplatesApi* | [**templates_by_name_put**](docs/apis/tags/TemplatesApi.md#templates_by_name_put) | **put** /templates/{name} | Update Template
*TemplatesApi* | [**templates_get**](docs/apis/tags/TemplatesApi.md#templates_get) | **get** /templates | Load Templates
*TemplatesApi* | [**templates_post**](docs/apis/tags/TemplatesApi.md#templates_post) | **post** /templates | Add Template
*VerificationsApi* | [**verifications_by_email_delete**](docs/apis/tags/VerificationsApi.md#verifications_by_email_delete) | **delete** /verifications/{email} | Delete Email Verification Result
*VerificationsApi* | [**verifications_by_email_get**](docs/apis/tags/VerificationsApi.md#verifications_by_email_get) | **get** /verifications/{email} | Get Email Verification Result
*VerificationsApi* | [**verifications_by_email_post**](docs/apis/tags/VerificationsApi.md#verifications_by_email_post) | **post** /verifications/{email} | Verify Email
*VerificationsApi* | [**verifications_files_by_id_delete**](docs/apis/tags/VerificationsApi.md#verifications_files_by_id_delete) | **delete** /verifications/files/{id} | Delete File Verification Result
*VerificationsApi* | [**verifications_files_by_id_result_download_get**](docs/apis/tags/VerificationsApi.md#verifications_files_by_id_result_download_get) | **get** /verifications/files/{id}/result/download | Download File Verification Result
*VerificationsApi* | [**verifications_files_by_id_result_get**](docs/apis/tags/VerificationsApi.md#verifications_files_by_id_result_get) | **get** /verifications/files/{id}/result | Get Detailed File Verification Result
*VerificationsApi* | [**verifications_files_by_id_verification_post**](docs/apis/tags/VerificationsApi.md#verifications_files_by_id_verification_post) | **post** /verifications/files/{id}/verification | Start verification
*VerificationsApi* | [**verifications_files_post**](docs/apis/tags/VerificationsApi.md#verifications_files_post) | **post** /verifications/files | Upload File with Emails
*VerificationsApi* | [**verifications_files_result_get**](docs/apis/tags/VerificationsApi.md#verifications_files_result_get) | **get** /verifications/files/result | Get Files Verification Results
*VerificationsApi* | [**verifications_get**](docs/apis/tags/VerificationsApi.md#verifications_get) | **get** /verifications | Get Emails Verification Results

## Documentation For Models

 - [AccessLevel](docs/models/AccessLevel.md)
 - [AccountStatusEnum](docs/models/AccountStatusEnum.md)
 - [ApiKey](docs/models/ApiKey.md)
 - [ApiKeyPayload](docs/models/ApiKeyPayload.md)
 - [BodyContentType](docs/models/BodyContentType.md)
 - [BodyPart](docs/models/BodyPart.md)
 - [Campaign](docs/models/Campaign.md)
 - [CampaignOptions](docs/models/CampaignOptions.md)
 - [CampaignRecipient](docs/models/CampaignRecipient.md)
 - [CampaignStatus](docs/models/CampaignStatus.md)
 - [CampaignTemplate](docs/models/CampaignTemplate.md)
 - [ChannelLogStatusSummary](docs/models/ChannelLogStatusSummary.md)
 - [CompressionFormat](docs/models/CompressionFormat.md)
 - [ConsentData](docs/models/ConsentData.md)
 - [ConsentTracking](docs/models/ConsentTracking.md)
 - [Contact](docs/models/Contact.md)
 - [ContactActivity](docs/models/ContactActivity.md)
 - [ContactPayload](docs/models/ContactPayload.md)
 - [ContactSource](docs/models/ContactSource.md)
 - [ContactStatus](docs/models/ContactStatus.md)
 - [ContactUpdatePayload](docs/models/ContactUpdatePayload.md)
 - [ContactsList](docs/models/ContactsList.md)
 - [DeliveryOptimizationType](docs/models/DeliveryOptimizationType.md)
 - [EmailContent](docs/models/EmailContent.md)
 - [EmailData](docs/models/EmailData.md)
 - [EmailJobFailedStatus](docs/models/EmailJobFailedStatus.md)
 - [EmailJobStatus](docs/models/EmailJobStatus.md)
 - [EmailMessageData](docs/models/EmailMessageData.md)
 - [EmailPredictedValidationStatus](docs/models/EmailPredictedValidationStatus.md)
 - [EmailRecipient](docs/models/EmailRecipient.md)
 - [EmailSend](docs/models/EmailSend.md)
 - [EmailStatus](docs/models/EmailStatus.md)
 - [EmailTransactionalMessageData](docs/models/EmailTransactionalMessageData.md)
 - [EmailValidationResult](docs/models/EmailValidationResult.md)
 - [EmailValidationStatus](docs/models/EmailValidationStatus.md)
 - [EmailView](docs/models/EmailView.md)
 - [EmailsPayload](docs/models/EmailsPayload.md)
 - [EncodingType](docs/models/EncodingType.md)
 - [EventType](docs/models/EventType.md)
 - [EventsOrderBy](docs/models/EventsOrderBy.md)
 - [ExportFileFormats](docs/models/ExportFileFormats.md)
 - [ExportLink](docs/models/ExportLink.md)
 - [ExportStatus](docs/models/ExportStatus.md)
 - [FileInfo](docs/models/FileInfo.md)
 - [FilePayload](docs/models/FilePayload.md)
 - [FileUploadResult](docs/models/FileUploadResult.md)
 - [InboundPayload](docs/models/InboundPayload.md)
 - [InboundRoute](docs/models/InboundRoute.md)
 - [InboundRouteActionType](docs/models/InboundRouteActionType.md)
 - [InboundRouteFilterType](docs/models/InboundRouteFilterType.md)
 - [ListPayload](docs/models/ListPayload.md)
 - [ListUpdatePayload](docs/models/ListUpdatePayload.md)
 - [LogJobStatus](docs/models/LogJobStatus.md)
 - [LogStatusSummary](docs/models/LogStatusSummary.md)
 - [MergeEmailPayload](docs/models/MergeEmailPayload.md)
 - [MessageAttachment](docs/models/MessageAttachment.md)
 - [MessageCategory](docs/models/MessageCategory.md)
 - [NewApiKey](docs/models/NewApiKey.md)
 - [NewSmtpCredentials](docs/models/NewSmtpCredentials.md)
 - [Options](docs/models/Options.md)
 - [RecipientEvent](docs/models/RecipientEvent.md)
 - [Segment](docs/models/Segment.md)
 - [SegmentPayload](docs/models/SegmentPayload.md)
 - [SmtpCredentials](docs/models/SmtpCredentials.md)
 - [SmtpCredentialsPayload](docs/models/SmtpCredentialsPayload.md)
 - [SortOrderItem](docs/models/SortOrderItem.md)
 - [SplitOptimizationType](docs/models/SplitOptimizationType.md)
 - [SplitOptions](docs/models/SplitOptions.md)
 - [SubAccountInfo](docs/models/SubAccountInfo.md)
 - [SubaccountEmailCreditsPayload](docs/models/SubaccountEmailCreditsPayload.md)
 - [SubaccountEmailSettings](docs/models/SubaccountEmailSettings.md)
 - [SubaccountEmailSettingsPayload](docs/models/SubaccountEmailSettingsPayload.md)
 - [SubaccountPayload](docs/models/SubaccountPayload.md)
 - [SubaccountSettingsInfo](docs/models/SubaccountSettingsInfo.md)
 - [SubaccountSettingsInfoPayload](docs/models/SubaccountSettingsInfoPayload.md)
 - [Suppression](docs/models/Suppression.md)
 - [Template](docs/models/Template.md)
 - [TemplatePayload](docs/models/TemplatePayload.md)
 - [TemplateScope](docs/models/TemplateScope.md)
 - [TemplateType](docs/models/TemplateType.md)
 - [TransactionalRecipient](docs/models/TransactionalRecipient.md)
 - [Utm](docs/models/Utm.md)
 - [VerificationFileResult](docs/models/VerificationFileResult.md)
 - [VerificationFileResultDetails](docs/models/VerificationFileResultDetails.md)
 - [VerificationStatus](docs/models/VerificationStatus.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## apikey

- **Type**: API key
- **API key parameter name**: X-ElasticEmail-ApiKey
- **Location**: HTTP header


## Author

support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com
support@elasticemail.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in ElasticEmail.apis and ElasticEmail.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from ElasticEmail.apis.default_api import DefaultApi`
- `from ElasticEmail.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import ElasticEmail
from ElasticEmail.apis import *
from ElasticEmail.models import *
```
