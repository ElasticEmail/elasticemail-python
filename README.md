<div align="center">

<img src=".github/ee-logo.png" alt="Elastic Email" width="96" />

# Elastic Email Python SDK

The official Python client library for the [Elastic Email](https://elasticemail.com) REST API v4.

[![PyPI](https://img.shields.io/pypi/v/ElasticEmail?logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/ElasticEmail/)
[![PyPI downloads](https://img.shields.io/pypi/dm/ElasticEmail?logo=pypi&logoColor=white&label=downloads&color=3775A9)](https://pypi.org/project/ElasticEmail/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![API](https://img.shields.io/badge/API-v4-0A7BBB)](https://elasticemail.com/developers/api-documentation/rest-api)
[![OpenAPI Generator](https://img.shields.io/badge/generated%20by-OpenAPI%20Generator-6BA539?logo=openapiinitiative&logoColor=white)](https://openapi-generator.tech)
[![License: MIT](https://img.shields.io/github/license/ElasticEmail/elasticemail-python?color=yellow)](LICENSE)

[![Latest release](https://img.shields.io/github/v/release/ElasticEmail/elasticemail-python?logo=github&label=release)](https://github.com/ElasticEmail/elasticemail-python/releases)
[![Last commit](https://img.shields.io/github/last-commit/ElasticEmail/elasticemail-python?logo=github)](https://github.com/ElasticEmail/elasticemail-python/commits/master)
[![Open issues](https://img.shields.io/github/issues/ElasticEmail/elasticemail-python?logo=github)](https://github.com/ElasticEmail/elasticemail-python/issues)
[![GitHub stars](https://img.shields.io/github/stars/ElasticEmail/elasticemail-python?style=flat&logo=github)](https://github.com/ElasticEmail/elasticemail-python/stargazers)

[Installation](#installation) •
[Quick start](#quick-start) •
[Examples](#more-examples) •
[API reference](#api-reference) •
[Models](#models) •
[Contributing](#contributing)

</div>

---

## Features

- **Transactional and bulk email.** Send single messages, bulk campaigns or CSV merge-file sends.
- **Contacts, lists and segments.** Add, update, import, export and bulk-delete contacts.
- **Campaigns and automations.** Create, update, pause and trigger automations for a contact.
- **Templates, files and attachments.** Manage templates and uploaded files.
- **Domains.** Verify sending domains and check SPF, DKIM, tracking and certificate status.
- **Webhooks and inbound routes.** Receive delivery events and route incoming mail.
- **Statistics, events and suppressions.** Track delivery, bounces, complaints and unsubscribes.
- **Subaccounts and security.** Manage subaccounts and API keys.
- **Typed models.** Request and response models are [Pydantic v2](https://docs.pydantic.dev) classes, and the package ships type hints (`py.typed`).

## Requirements

| Dependency | Version |
| --- | --- |
| Python | 3.8 or later |
| [urllib3](https://pypi.org/project/urllib3/) | 1.25.3 or later, below 3.0 |
| [python-dateutil](https://pypi.org/project/python-dateutil/) | 2.8.2 or later |
| [pydantic](https://pypi.org/project/pydantic/) | 2.x |
| [typing-extensions](https://pypi.org/project/typing-extensions/) | 4.7.1 or later |

You'll also need an Elastic Email **API key**. You can create one in your [API settings](https://app.elasticemail.com/marketing/settings/new/manage-api). Each endpoint's documentation lists the access level it needs.

## Installation

Install the [`ElasticEmail`](https://pypi.org/project/ElasticEmail/) package from PyPI:

```bash
pip install ElasticEmail
```

Or with Poetry or uv:

```bash
poetry add ElasticEmail
uv add ElasticEmail
```

Then import the package:

```python
import ElasticEmail
```

## Quick start

### Configure the client

```python
import os

import ElasticEmail
from ElasticEmail.rest import ApiException
from ElasticEmail.models import (
    BodyContentType,
    BodyPart,
    EmailContent,
    EmailTransactionalMessageData,
    TransactionalRecipient,
)

configuration = ElasticEmail.Configuration(host="https://api.elasticemail.com/v4")
configuration.api_key["apikey"] = os.environ["ELASTICEMAIL_API_KEY"]
```

> [!TIP]
> Keep your API key out of source code. Load it from an environment variable, a `.env` file that isn't committed, or a secrets manager.

### Send a transactional email

```python
message = EmailTransactionalMessageData(
    recipients=TransactionalRecipient(to=["john.doe@example.com"]),
    content=EmailContent(
        var_from="My App <no-reply@yourdomain.com>",
        subject="Welcome aboard!",
        body=[
            BodyPart(content_type=BodyContentType.HTML, content="<h1>Hello!</h1><p>Thanks for signing up.</p>"),
            BodyPart(content_type=BodyContentType.PLAINTEXT, content="Hello! Thanks for signing up."),
        ],
    ),
)

with ElasticEmail.ApiClient(configuration) as api_client:
    emails = ElasticEmail.EmailsApi(api_client)
    try:
        result = emails.emails_transactional_post(message)
        print(f"Sent. TransactionID: {result.transaction_id}, MessageID: {result.message_id}")
    except ApiException as e:
        print(f"Elastic Email API error {e.status}: {e.body}")
```

The sender field is `var_from` because `from` is a reserved word in Python. The address must use a domain you've verified in your Elastic Email account.

### Send from a template with merge fields

```python
message = EmailTransactionalMessageData(
    recipients=TransactionalRecipient(to=["john.doe@example.com"]),
    content=EmailContent(
        var_from="My App <no-reply@yourdomain.com>",
        template_name="welcome-template",
        merge={"firstname": "John"},
    ),
)

with ElasticEmail.ApiClient(configuration) as api_client:
    ElasticEmail.EmailsApi(api_client).emails_transactional_post(message)
```

### Proxy, timeouts and retries

```python
configuration.proxy = "http://myProxyUrl:80/"
configuration.retries = 3

# Per-request timeout in seconds, or a (connect, read) tuple
emails.emails_transactional_post(message, _request_timeout=(5, 30))
```

## More examples

More complete, runnable samples are in the **[Elastic Email examples repository](https://github.com/ElasticEmail/elasticemail-examples)**. It covers transactional email, SMTP, webhooks, inbound email, contacts and serverless platforms across 20+ languages and frameworks.

- 🐍 [Python examples](https://github.com/ElasticEmail/elasticemail-examples/tree/main/python-elasticemail-examples)
- 📂 [All examples](https://github.com/ElasticEmail/elasticemail-examples)

<details>
<summary><strong>Snippets in this repository</strong></summary>

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

</details>

## Authentication

| Scheme | Header | Used for |
| --- | --- | --- |
| `apikey` | `X-ElasticEmail-ApiKey` | All standard API calls |
| `ApiKeyAuthCustomBranding` | `X-Auth-Token` | Custom-branding (white-label) accounts |

## API limits

- Up to **20 concurrent connections** per account
- A hard timeout of **600 seconds** per request

## API reference

All URIs are relative to `https://api.elasticemail.com/v4`. The SDK covers **114 endpoints** across 16 API classes: `CampaignsApi`, `ContactsApi`, `DomainsApi`, `EmailsApi`, `EventsApi`, `FilesApi`, `InboundRouteApi`, `ListsApi`, `SecurityApi`, `SegmentsApi`, `StatisticsApi`, `SubAccountsApi`, `SuppressionsApi`, `TemplatesApi`, `VerificationsApi` and `WebhookApi`.

<details>
<summary><strong>Show all endpoints</strong></summary>


All URIs are relative to *https://api.elasticemail.com/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CampaignsApi* | [**campaigns_automation_by_name_trigger_post**](docs/CampaignsApi.md#campaigns_automation_by_name_trigger_post) | **POST** /campaigns/automation/{name}/trigger | Trigger Automation for Contact
*CampaignsApi* | [**campaigns_by_name_delete**](docs/CampaignsApi.md#campaigns_by_name_delete) | **DELETE** /campaigns/{name} | Delete Campaign
*CampaignsApi* | [**campaigns_by_name_get**](docs/CampaignsApi.md#campaigns_by_name_get) | **GET** /campaigns/{name} | Load Campaign
*CampaignsApi* | [**campaigns_by_name_pause_put**](docs/CampaignsApi.md#campaigns_by_name_pause_put) | **PUT** /campaigns/{name}/pause | Pause Campaign
*CampaignsApi* | [**campaigns_by_name_put**](docs/CampaignsApi.md#campaigns_by_name_put) | **PUT** /campaigns/{name} | Update Campaign
*CampaignsApi* | [**campaigns_get**](docs/CampaignsApi.md#campaigns_get) | **GET** /campaigns | Load Campaigns
*CampaignsApi* | [**campaigns_post**](docs/CampaignsApi.md#campaigns_post) | **POST** /campaigns | Add Campaign
*ContactsApi* | [**contacts_by_email_delete**](docs/ContactsApi.md#contacts_by_email_delete) | **DELETE** /contacts/{email} | Delete Contact
*ContactsApi* | [**contacts_by_email_get**](docs/ContactsApi.md#contacts_by_email_get) | **GET** /contacts/{email} | Load Contact
*ContactsApi* | [**contacts_by_email_put**](docs/ContactsApi.md#contacts_by_email_put) | **PUT** /contacts/{email} | Update Contact
*ContactsApi* | [**contacts_delete_post**](docs/ContactsApi.md#contacts_delete_post) | **POST** /contacts/delete | Delete Contacts Bulk
*ContactsApi* | [**contacts_export_by_id_status_get**](docs/ContactsApi.md#contacts_export_by_id_status_get) | **GET** /contacts/export/{id}/status | Check Export Status
*ContactsApi* | [**contacts_export_post**](docs/ContactsApi.md#contacts_export_post) | **POST** /contacts/export | Export Contacts
*ContactsApi* | [**contacts_get**](docs/ContactsApi.md#contacts_get) | **GET** /contacts | Load Contacts
*ContactsApi* | [**contacts_import_post**](docs/ContactsApi.md#contacts_import_post) | **POST** /contacts/import | Upload Contacts
*ContactsApi* | [**contacts_post**](docs/ContactsApi.md#contacts_post) | **POST** /contacts | Add Contact
*DomainsApi* | [**domains_by_domain_delete**](docs/DomainsApi.md#domains_by_domain_delete) | **DELETE** /domains/{domain} | Delete Domain
*DomainsApi* | [**domains_by_domain_get**](docs/DomainsApi.md#domains_by_domain_get) | **GET** /domains/{domain} | Load Domain
*DomainsApi* | [**domains_by_domain_put**](docs/DomainsApi.md#domains_by_domain_put) | **PUT** /domains/{domain} | Update Domain
*DomainsApi* | [**domains_by_domain_restricted_get**](docs/DomainsApi.md#domains_by_domain_restricted_get) | **GET** /domains/{domain}/restricted | Check for domain restriction
*DomainsApi* | [**domains_by_domain_verification_put**](docs/DomainsApi.md#domains_by_domain_verification_put) | **PUT** /domains/{domain}/verification | Verify Domain
*DomainsApi* | [**domains_by_email_default_patch**](docs/DomainsApi.md#domains_by_email_default_patch) | **PATCH** /domains/{email}/default | Set Default
*DomainsApi* | [**domains_get**](docs/DomainsApi.md#domains_get) | **GET** /domains | Load Domains
*DomainsApi* | [**domains_post**](docs/DomainsApi.md#domains_post) | **POST** /domains | Add Domain
*EmailsApi* | [**emails_by_msgid_view_get**](docs/EmailsApi.md#emails_by_msgid_view_get) | **GET** /emails/{msgid}/view | View Email
*EmailsApi* | [**emails_by_transactionid_status_get**](docs/EmailsApi.md#emails_by_transactionid_status_get) | **GET** /emails/{transactionid}/status | Get Status
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
*ListsApi* | [**lists_by_listname_contacts_get**](docs/ListsApi.md#lists_by_listname_contacts_get) | **GET** /lists/{listname}/contacts | Load Contacts in List
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
*SubAccountsApi* | [**subaccounts_by_email_apikey_get**](docs/SubAccountsApi.md#subaccounts_by_email_apikey_get) | **GET** /subaccounts/{email}/apikey | Get SubAccount ApiKey
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
*WebhookApi* | [**webhook_by_publicid_delete**](docs/WebhookApi.md#webhook_by_publicid_delete) | **DELETE** /webhook/{publicid} | Delete Webhook
*WebhookApi* | [**webhook_by_publicid_get**](docs/WebhookApi.md#webhook_by_publicid_get) | **GET** /webhook/{publicid} | Load Webhook
*WebhookApi* | [**webhook_by_publicid_put**](docs/WebhookApi.md#webhook_by_publicid_put) | **PUT** /webhook/{publicid} | Update Webhook
*WebhookApi* | [**webhook_get**](docs/WebhookApi.md#webhook_get) | **GET** /webhook | Load Webhooks
*WebhookApi* | [**webhook_post**](docs/WebhookApi.md#webhook_post) | **POST** /webhook | Add Webhook


</details>

## Models

<details>
<summary><strong>Show all 98 models</strong></summary>

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
 - [CertificateValidationStatus](docs/CertificateValidationStatus.md)
 - [ChannelLogStatusSummary](docs/ChannelLogStatusSummary.md)
 - [CompressionFormat](docs/CompressionFormat.md)
 - [ConsentData](docs/ConsentData.md)
 - [ConsentTracking](docs/ConsentTracking.md)
 - [Contact](docs/Contact.md)
 - [ContactActivity](docs/ContactActivity.md)
 - [ContactPayload](docs/ContactPayload.md)
 - [ContactSource](docs/ContactSource.md)
 - [ContactStatus](docs/ContactStatus.md)
 - [ContactUpdatePayload](docs/ContactUpdatePayload.md)
 - [ContactsList](docs/ContactsList.md)
 - [DKIMRecord](docs/DKIMRecord.md)
 - [DeliveryOptimizationType](docs/DeliveryOptimizationType.md)
 - [DomainData](docs/DomainData.md)
 - [DomainDetail](docs/DomainDetail.md)
 - [DomainOwner](docs/DomainOwner.md)
 - [DomainPayload](docs/DomainPayload.md)
 - [DomainUpdatePayload](docs/DomainUpdatePayload.md)
 - [EmailContent](docs/EmailContent.md)
 - [EmailData](docs/EmailData.md)
 - [EmailJobFailedStatus](docs/EmailJobFailedStatus.md)
 - [EmailJobStatus](docs/EmailJobStatus.md)
 - [EmailMessageData](docs/EmailMessageData.md)
 - [EmailPredictedValidationStatus](docs/EmailPredictedValidationStatus.md)
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
 - [MessageCategoryEnum](docs/MessageCategoryEnum.md)
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
 - [TrackingType](docs/TrackingType.md)
 - [TrackingValidationStatus](docs/TrackingValidationStatus.md)
 - [TransactionalRecipient](docs/TransactionalRecipient.md)
 - [Utm](docs/Utm.md)
 - [VerificationFileResult](docs/VerificationFileResult.md)
 - [VerificationFileResultDetails](docs/VerificationFileResultDetails.md)
 - [VerificationStatus](docs/VerificationStatus.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookCreatePayload](docs/WebhookCreatePayload.md)
 - [WebhookUpdatePayload](docs/WebhookUpdatePayload.md)


</details>

## Tests

```bash
pip install -r requirements.txt -r test-requirements.txt
pytest
```

## Versioning

The SDK follows the Elastic Email API v4. Package versions and release notes are listed on [PyPI](https://pypi.org/project/ElasticEmail/#history) and in [GitHub Releases](https://github.com/ElasticEmail/elasticemail-python/releases).

<details>
<summary>Build details</summary>

- API version: 4.0.0
- SDK version: 4.2.1
- Generator version: 7.11.0
- Build package: `org.openapitools.codegen.languages.PythonClientCodegen`

</details>

## Contributing

Contributions are welcome! Most of this SDK is generated from the Elastic Email OpenAPI specification, so please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

- 🐛 [Report a bug](https://github.com/ElasticEmail/elasticemail-python/issues/new?template=bug_report.md)
- 💡 [Request a feature](https://github.com/ElasticEmail/elasticemail-python/issues/new?template=feature_request.md)
- 🔒 [Report a security issue](SECURITY.md)

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

## Support

> [!IMPORTANT]
> The fastest way to get help is the **chat widget on [elasticemail.com](https://elasticemail.com)**. Our support team can help with your account, sending, deliverability and API questions.

- 💬 [Chat with support on elasticemail.com](https://elasticemail.com) (preferred)
- 📚 [API documentation](https://elasticemail.com/developers/api-documentation/rest-api)
- 🧪 [Examples repository](https://github.com/ElasticEmail/elasticemail-examples)
- 🐛 [GitHub issues](https://github.com/ElasticEmail/elasticemail-python/issues), for bugs in this SDK only

## License

Released under the [MIT License](LICENSE). Copyright © 2021–2026 Elastic Email.
