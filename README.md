# ElasticEmail
This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.

Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.

The API has a limit of 20 concurrent connections and a hard timeout of 600 seconds per request.

To start using this API, you will need your Access Token (available [here](https://elasticemail.com/account#/settings/new/manage-api)). Remember to keep it safe. Required access levels are listed in the given request’s description.

Downloadable library clients can be found in our Github repository [here](https://github.com/ElasticEmail?tab=repositories&q=%22rest+api%22+in%3Areadme)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 4.0.0
- Package version: 4.0.19
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

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
from ElasticEmail.api import campaigns_api
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

## Documentation for API Endpoints

All URIs are relative to *https://api.elasticemail.com/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CampaignsApi* | [**campaigns_by_name_delete**](docs/CampaignsApi.md#campaigns_by_name_delete) | **DELETE** /campaigns/{name} | Delete Campaign
*CampaignsApi* | [**campaigns_by_name_get**](docs/CampaignsApi.md#campaigns_by_name_get) | **GET** /campaigns/{name} | Load Campaign
*CampaignsApi* | [**campaigns_by_name_put**](docs/CampaignsApi.md#campaigns_by_name_put) | **PUT** /campaigns/{name} | Update Campaign
*CampaignsApi* | [**campaigns_get**](docs/CampaignsApi.md#campaigns_get) | **GET** /campaigns | Load Campaigns
*CampaignsApi* | [**campaigns_post**](docs/CampaignsApi.md#campaigns_post) | **POST** /campaigns | Add Campaign
*ContactsApi* | [**contacts_by_email_delete**](docs/ContactsApi.md#contacts_by_email_delete) | **DELETE** /contacts/{email} | Delete Contact
*ContactsApi* | [**contacts_by_email_get**](docs/ContactsApi.md#contacts_by_email_get) | **GET** /contacts/{email} | Load Contact
*ContactsApi* | [**contacts_by_email_history_get**](docs/ContactsApi.md#contacts_by_email_history_get) | **GET** /contacts/{email}/history | Load History
*ContactsApi* | [**contacts_by_email_put**](docs/ContactsApi.md#contacts_by_email_put) | **PUT** /contacts/{email} | Update Contact
*ContactsApi* | [**contacts_delete_post**](docs/ContactsApi.md#contacts_delete_post) | **POST** /contacts/delete | Delete Contacts Bulk
*ContactsApi* | [**contacts_export_by_id_status_get**](docs/ContactsApi.md#contacts_export_by_id_status_get) | **GET** /contacts/export/{id}/status | Check Export Status
*ContactsApi* | [**contacts_export_post**](docs/ContactsApi.md#contacts_export_post) | **POST** /contacts/export | Export Contacts
*ContactsApi* | [**contacts_get**](docs/ContactsApi.md#contacts_get) | **GET** /contacts | Load Contacts
*ContactsApi* | [**contacts_import_post**](docs/ContactsApi.md#contacts_import_post) | **POST** /contacts/import | Upload Contacts
*ContactsApi* | [**contacts_post**](docs/ContactsApi.md#contacts_post) | **POST** /contacts | Add Contact
*EmailsApi* | [**emails_by_msgid_view_get**](docs/EmailsApi.md#emails_by_msgid_view_get) | **GET** /emails/{msgid}/view | View Email
*EmailsApi* | [**emails_mergefile_post**](docs/EmailsApi.md#emails_mergefile_post) | **POST** /emails/mergefile | Send Bulk Emails CSV
*EmailsApi* | [**emails_post**](docs/EmailsApi.md#emails_post) | **POST** /emails | Send Bulk Emails
*EmailsApi* | [**emails_transactional_post**](docs/EmailsApi.md#emails_transactional_post) | **POST** /emails/transactional | Send Transactional Email
*EventsApi* | [**events_by_transactionid_get**](docs/EventsApi.md#events_by_transactionid_get) | **GET** /events/{transactionid} | Load Email Events
*EventsApi* | [**events_channels_by_name_export_post**](docs/EventsApi.md#events_channels_by_name_export_post) | **POST** /events/channels/{name}/export | Export Channel Events
*EventsApi* | [**events_channels_by_name_get**](docs/EventsApi.md#events_channels_by_name_get) | **GET** /events/channels/{name} | Load Channel Events
*EventsApi* | [**events_channels_export_by_id_status_get**](docs/EventsApi.md#events_channels_export_by_id_status_get) | **GET** /events/channels/export/{id}/status | Check Channel Export Status
*EventsApi* | [**events_export_by_id_status_get**](docs/EventsApi.md#events_export_by_id_status_get) | **GET** /events/export/{id}/status | Check Export Status
*EventsApi* | [**events_export_post**](docs/EventsApi.md#events_export_post) | **POST** /events/export | Export Events
*EventsApi* | [**events_get**](docs/EventsApi.md#events_get) | **GET** /events | Load Events
*FilesApi* | [**files_by_name_delete**](docs/FilesApi.md#files_by_name_delete) | **DELETE** /files/{name} | Delete File
*FilesApi* | [**files_by_name_get**](docs/FilesApi.md#files_by_name_get) | **GET** /files/{name} | Download File
*FilesApi* | [**files_by_name_info_get**](docs/FilesApi.md#files_by_name_info_get) | **GET** /files/{name}/info | Load File Details
*FilesApi* | [**files_get**](docs/FilesApi.md#files_get) | **GET** /files | List Files
*FilesApi* | [**files_post**](docs/FilesApi.md#files_post) | **POST** /files | Upload File
*InboundRouteApi* | [**inboundroute_by_id_delete**](docs/InboundRouteApi.md#inboundroute_by_id_delete) | **DELETE** /inboundroute/{id} | Delete Route
*InboundRouteApi* | [**inboundroute_by_id_get**](docs/InboundRouteApi.md#inboundroute_by_id_get) | **GET** /inboundroute/{id} | Get Route
*InboundRouteApi* | [**inboundroute_by_id_put**](docs/InboundRouteApi.md#inboundroute_by_id_put) | **PUT** /inboundroute/{id} | Update Route
*InboundRouteApi* | [**inboundroute_get**](docs/InboundRouteApi.md#inboundroute_get) | **GET** /inboundroute | Get Routes
*InboundRouteApi* | [**inboundroute_order_put**](docs/InboundRouteApi.md#inboundroute_order_put) | **PUT** /inboundroute/order | Update Sorting
*InboundRouteApi* | [**inboundroute_post**](docs/InboundRouteApi.md#inboundroute_post) | **POST** /inboundroute | Create Route
*ListsApi* | [**lists_by_name_contacts_post**](docs/ListsApi.md#lists_by_name_contacts_post) | **POST** /lists/{name}/contacts | Add Contacts to List
*ListsApi* | [**lists_by_name_contacts_remove_post**](docs/ListsApi.md#lists_by_name_contacts_remove_post) | **POST** /lists/{name}/contacts/remove | Remove Contacts from List
*ListsApi* | [**lists_by_name_delete**](docs/ListsApi.md#lists_by_name_delete) | **DELETE** /lists/{name} | Delete List
*ListsApi* | [**lists_by_name_get**](docs/ListsApi.md#lists_by_name_get) | **GET** /lists/{name} | Load List
*ListsApi* | [**lists_by_name_put**](docs/ListsApi.md#lists_by_name_put) | **PUT** /lists/{name} | Update List
*ListsApi* | [**lists_get**](docs/ListsApi.md#lists_get) | **GET** /lists | Load Lists
*ListsApi* | [**lists_post**](docs/ListsApi.md#lists_post) | **POST** /lists | Add List
*SecurityApi* | [**security_apikeys_by_name_delete**](docs/SecurityApi.md#security_apikeys_by_name_delete) | **DELETE** /security/apikeys/{name} | Delete ApiKey
*SecurityApi* | [**security_apikeys_by_name_get**](docs/SecurityApi.md#security_apikeys_by_name_get) | **GET** /security/apikeys/{name} | Load ApiKey
*SecurityApi* | [**security_apikeys_by_name_put**](docs/SecurityApi.md#security_apikeys_by_name_put) | **PUT** /security/apikeys/{name} | Update ApiKey
*SecurityApi* | [**security_apikeys_get**](docs/SecurityApi.md#security_apikeys_get) | **GET** /security/apikeys | List ApiKeys
*SecurityApi* | [**security_apikeys_post**](docs/SecurityApi.md#security_apikeys_post) | **POST** /security/apikeys | Add ApiKey
*SecurityApi* | [**security_smtp_by_name_delete**](docs/SecurityApi.md#security_smtp_by_name_delete) | **DELETE** /security/smtp/{name} | Delete SMTP Credential
*SecurityApi* | [**security_smtp_by_name_get**](docs/SecurityApi.md#security_smtp_by_name_get) | **GET** /security/smtp/{name} | Load SMTP Credential
*SecurityApi* | [**security_smtp_by_name_put**](docs/SecurityApi.md#security_smtp_by_name_put) | **PUT** /security/smtp/{name} | Update SMTP Credential
*SecurityApi* | [**security_smtp_get**](docs/SecurityApi.md#security_smtp_get) | **GET** /security/smtp | List SMTP Credentials
*SecurityApi* | [**security_smtp_post**](docs/SecurityApi.md#security_smtp_post) | **POST** /security/smtp | Add SMTP Credential
*SegmentsApi* | [**segments_by_name_delete**](docs/SegmentsApi.md#segments_by_name_delete) | **DELETE** /segments/{name} | Delete Segment
*SegmentsApi* | [**segments_by_name_get**](docs/SegmentsApi.md#segments_by_name_get) | **GET** /segments/{name} | Load Segment
*SegmentsApi* | [**segments_by_name_put**](docs/SegmentsApi.md#segments_by_name_put) | **PUT** /segments/{name} | Update Segment
*SegmentsApi* | [**segments_get**](docs/SegmentsApi.md#segments_get) | **GET** /segments | Load Segments
*SegmentsApi* | [**segments_post**](docs/SegmentsApi.md#segments_post) | **POST** /segments | Add Segment
*StatisticsApi* | [**statistics_campaigns_by_name_get**](docs/StatisticsApi.md#statistics_campaigns_by_name_get) | **GET** /statistics/campaigns/{name} | Load Campaign Stats
*StatisticsApi* | [**statistics_campaigns_get**](docs/StatisticsApi.md#statistics_campaigns_get) | **GET** /statistics/campaigns | Load Campaigns Stats
*StatisticsApi* | [**statistics_channels_by_name_get**](docs/StatisticsApi.md#statistics_channels_by_name_get) | **GET** /statistics/channels/{name} | Load Channel Stats
*StatisticsApi* | [**statistics_channels_get**](docs/StatisticsApi.md#statistics_channels_get) | **GET** /statistics/channels | Load Channels Stats
*StatisticsApi* | [**statistics_get**](docs/StatisticsApi.md#statistics_get) | **GET** /statistics | Load Statistics
*SubAccountsApi* | [**subaccounts_by_email_credits_patch**](docs/SubAccountsApi.md#subaccounts_by_email_credits_patch) | **PATCH** /subaccounts/{email}/credits | Add, Subtract Email Credits
*SubAccountsApi* | [**subaccounts_by_email_delete**](docs/SubAccountsApi.md#subaccounts_by_email_delete) | **DELETE** /subaccounts/{email} | Delete SubAccount
*SubAccountsApi* | [**subaccounts_by_email_get**](docs/SubAccountsApi.md#subaccounts_by_email_get) | **GET** /subaccounts/{email} | Load SubAccount
*SubAccountsApi* | [**subaccounts_by_email_settings_email_put**](docs/SubAccountsApi.md#subaccounts_by_email_settings_email_put) | **PUT** /subaccounts/{email}/settings/email | Update SubAccount Email Settings
*SubAccountsApi* | [**subaccounts_get**](docs/SubAccountsApi.md#subaccounts_get) | **GET** /subaccounts | Load SubAccounts
*SubAccountsApi* | [**subaccounts_post**](docs/SubAccountsApi.md#subaccounts_post) | **POST** /subaccounts | Add SubAccount
*SuppressionsApi* | [**suppressions_bounces_get**](docs/SuppressionsApi.md#suppressions_bounces_get) | **GET** /suppressions/bounces | Get Bounce List
*SuppressionsApi* | [**suppressions_bounces_import_post**](docs/SuppressionsApi.md#suppressions_bounces_import_post) | **POST** /suppressions/bounces/import | Add Bounces Async
*SuppressionsApi* | [**suppressions_bounces_post**](docs/SuppressionsApi.md#suppressions_bounces_post) | **POST** /suppressions/bounces | Add Bounces
*SuppressionsApi* | [**suppressions_by_email_delete**](docs/SuppressionsApi.md#suppressions_by_email_delete) | **DELETE** /suppressions/{email} | Delete Suppression
*SuppressionsApi* | [**suppressions_by_email_get**](docs/SuppressionsApi.md#suppressions_by_email_get) | **GET** /suppressions/{email} | Get Suppression
*SuppressionsApi* | [**suppressions_complaints_get**](docs/SuppressionsApi.md#suppressions_complaints_get) | **GET** /suppressions/complaints | Get Complaints List
*SuppressionsApi* | [**suppressions_complaints_import_post**](docs/SuppressionsApi.md#suppressions_complaints_import_post) | **POST** /suppressions/complaints/import | Add Complaints Async
*SuppressionsApi* | [**suppressions_complaints_post**](docs/SuppressionsApi.md#suppressions_complaints_post) | **POST** /suppressions/complaints | Add Complaints
*SuppressionsApi* | [**suppressions_get**](docs/SuppressionsApi.md#suppressions_get) | **GET** /suppressions | Get Suppressions
*SuppressionsApi* | [**suppressions_unsubscribes_get**](docs/SuppressionsApi.md#suppressions_unsubscribes_get) | **GET** /suppressions/unsubscribes | Get Unsubscribes List
*SuppressionsApi* | [**suppressions_unsubscribes_import_post**](docs/SuppressionsApi.md#suppressions_unsubscribes_import_post) | **POST** /suppressions/unsubscribes/import | Add Unsubscribes Async
*SuppressionsApi* | [**suppressions_unsubscribes_post**](docs/SuppressionsApi.md#suppressions_unsubscribes_post) | **POST** /suppressions/unsubscribes | Add Unsubscribes
*TemplatesApi* | [**templates_by_name_delete**](docs/TemplatesApi.md#templates_by_name_delete) | **DELETE** /templates/{name} | Delete Template
*TemplatesApi* | [**templates_by_name_get**](docs/TemplatesApi.md#templates_by_name_get) | **GET** /templates/{name} | Load Template
*TemplatesApi* | [**templates_by_name_put**](docs/TemplatesApi.md#templates_by_name_put) | **PUT** /templates/{name} | Update Template
*TemplatesApi* | [**templates_get**](docs/TemplatesApi.md#templates_get) | **GET** /templates | Load Templates
*TemplatesApi* | [**templates_post**](docs/TemplatesApi.md#templates_post) | **POST** /templates | Add Template
*VerificationsApi* | [**verifications_by_email_delete**](docs/VerificationsApi.md#verifications_by_email_delete) | **DELETE** /verifications/{email} | Delete Email Verification Result
*VerificationsApi* | [**verifications_by_email_get**](docs/VerificationsApi.md#verifications_by_email_get) | **GET** /verifications/{email} | Get Email Verification Result
*VerificationsApi* | [**verifications_by_email_post**](docs/VerificationsApi.md#verifications_by_email_post) | **POST** /verifications/{email} | Verify Email
*VerificationsApi* | [**verifications_files_by_id_delete**](docs/VerificationsApi.md#verifications_files_by_id_delete) | **DELETE** /verifications/files/{id} | Delete File Verification Result
*VerificationsApi* | [**verifications_files_by_id_result_download_get**](docs/VerificationsApi.md#verifications_files_by_id_result_download_get) | **GET** /verifications/files/{id}/result/download | Download File Verification Result
*VerificationsApi* | [**verifications_files_by_id_result_get**](docs/VerificationsApi.md#verifications_files_by_id_result_get) | **GET** /verifications/files/{id}/result | Get Detailed File Verification Result
*VerificationsApi* | [**verifications_files_by_id_verification_post**](docs/VerificationsApi.md#verifications_files_by_id_verification_post) | **POST** /verifications/files/{id}/verification | Start verification
*VerificationsApi* | [**verifications_files_post**](docs/VerificationsApi.md#verifications_files_post) | **POST** /verifications/files | Upload File with Emails
*VerificationsApi* | [**verifications_files_result_get**](docs/VerificationsApi.md#verifications_files_result_get) | **GET** /verifications/files/result | Get Files Verification Results
*VerificationsApi* | [**verifications_get**](docs/VerificationsApi.md#verifications_get) | **GET** /verifications | Get Emails Verification Results


## Documentation For Models

 - [AccessLevel](docs/AccessLevel.md)
 - [AccountStatusEnum](docs/AccountStatusEnum.md)
 - [ApiKey](docs/ApiKey.md)
 - [ApiKeyPayload](docs/ApiKeyPayload.md)
 - [BodyContentType](docs/BodyContentType.md)
 - [BodyPart](docs/BodyPart.md)
 - [Campaign](docs/Campaign.md)
 - [CampaignOptions](docs/CampaignOptions.md)
 - [CampaignRecipient](docs/CampaignRecipient.md)
 - [CampaignStatus](docs/CampaignStatus.md)
 - [CampaignTemplate](docs/CampaignTemplate.md)
 - [ChannelLogStatusSummary](docs/ChannelLogStatusSummary.md)
 - [CompressionFormat](docs/CompressionFormat.md)
 - [ConsentData](docs/ConsentData.md)
 - [ConsentTracking](docs/ConsentTracking.md)
 - [Contact](docs/Contact.md)
 - [ContactActivity](docs/ContactActivity.md)
 - [ContactHistEventType](docs/ContactHistEventType.md)
 - [ContactHistory](docs/ContactHistory.md)
 - [ContactPayload](docs/ContactPayload.md)
 - [ContactSource](docs/ContactSource.md)
 - [ContactStatus](docs/ContactStatus.md)
 - [ContactUpdatePayload](docs/ContactUpdatePayload.md)
 - [ContactsList](docs/ContactsList.md)
 - [DeliveryOptimizationType](docs/DeliveryOptimizationType.md)
 - [EmailContent](docs/EmailContent.md)
 - [EmailData](docs/EmailData.md)
 - [EmailMessageData](docs/EmailMessageData.md)
 - [EmailRecipient](docs/EmailRecipient.md)
 - [EmailSend](docs/EmailSend.md)
 - [EmailStatus](docs/EmailStatus.md)
 - [EmailTransactionalMessageData](docs/EmailTransactionalMessageData.md)
 - [EmailValidationResult](docs/EmailValidationResult.md)
 - [EmailValidationStatus](docs/EmailValidationStatus.md)
 - [EmailView](docs/EmailView.md)
 - [EmailsPayload](docs/EmailsPayload.md)
 - [EncodingType](docs/EncodingType.md)
 - [EventType](docs/EventType.md)
 - [EventsOrderBy](docs/EventsOrderBy.md)
 - [ExportFileFormats](docs/ExportFileFormats.md)
 - [ExportLink](docs/ExportLink.md)
 - [ExportStatus](docs/ExportStatus.md)
 - [FileInfo](docs/FileInfo.md)
 - [FilePayload](docs/FilePayload.md)
 - [FileUploadResult](docs/FileUploadResult.md)
 - [InboundPayload](docs/InboundPayload.md)
 - [InboundRoute](docs/InboundRoute.md)
 - [InboundRouteActionType](docs/InboundRouteActionType.md)
 - [InboundRouteFilterType](docs/InboundRouteFilterType.md)
 - [ListPayload](docs/ListPayload.md)
 - [ListUpdatePayload](docs/ListUpdatePayload.md)
 - [LogJobStatus](docs/LogJobStatus.md)
 - [LogStatusSummary](docs/LogStatusSummary.md)
 - [MergeEmailPayload](docs/MergeEmailPayload.md)
 - [MessageAttachment](docs/MessageAttachment.md)
 - [MessageCategory](docs/MessageCategory.md)
 - [NewApiKey](docs/NewApiKey.md)
 - [NewSmtpCredentials](docs/NewSmtpCredentials.md)
 - [Options](docs/Options.md)
 - [RecipientEvent](docs/RecipientEvent.md)
 - [Segment](docs/Segment.md)
 - [SegmentPayload](docs/SegmentPayload.md)
 - [SmtpCredentials](docs/SmtpCredentials.md)
 - [SmtpCredentialsPayload](docs/SmtpCredentialsPayload.md)
 - [SortOrderItem](docs/SortOrderItem.md)
 - [SplitOptimizationType](docs/SplitOptimizationType.md)
 - [SplitOptions](docs/SplitOptions.md)
 - [SubAccountInfo](docs/SubAccountInfo.md)
 - [SubaccountEmailCreditsPayload](docs/SubaccountEmailCreditsPayload.md)
 - [SubaccountEmailSettings](docs/SubaccountEmailSettings.md)
 - [SubaccountEmailSettingsPayload](docs/SubaccountEmailSettingsPayload.md)
 - [SubaccountPayload](docs/SubaccountPayload.md)
 - [SubaccountSettingsInfo](docs/SubaccountSettingsInfo.md)
 - [SubaccountSettingsInfoPayload](docs/SubaccountSettingsInfoPayload.md)
 - [Suppression](docs/Suppression.md)
 - [Template](docs/Template.md)
 - [TemplatePayload](docs/TemplatePayload.md)
 - [TemplateScope](docs/TemplateScope.md)
 - [TemplateType](docs/TemplateType.md)
 - [TransactionalRecipient](docs/TransactionalRecipient.md)
 - [Utm](docs/Utm.md)
 - [VerificationFileResult](docs/VerificationFileResult.md)
 - [VerificationFileResultDetails](docs/VerificationFileResultDetails.md)
 - [VerificationStatus](docs/VerificationStatus.md)


## Documentation For Authorization


## apikey

- **Type**: API key
- **API key parameter name**: X-ElasticEmail-ApiKey
- **Location**: HTTP header


## Author

support@elasticemail.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in ElasticEmail.apis and ElasticEmail.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from ElasticEmail.api.default_api import DefaultApi`
- `from ElasticEmail.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import ElasticEmail
from ElasticEmail.apis import *
from ElasticEmail.models import *
```

