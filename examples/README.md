# Python Snippets
Snippets prepared for Python 3.

Written and tested in Python 3.8

The lib requires Python >= 3.6

## Prepare test enviroment
Install Python 3.

Install `elasticemail-python` lib

Eg. run in terminal `pip install git+https://github.com/elasticemail/elasticemail-python.git`

## Set your API key
Every snippet reads the API key from the `ELASTICEMAIL_API_KEY` environment variable and stops with a message if it isn't set:

```
export ELASTICEMAIL_API_KEY=...
```

## Prepare a snippet
Replace other data if needed eg.: 
- your validated email address, 
- your email address to receive example email.
- template name
- campaign name
- ...etc

## Running a snippet
Run

`cd functions`

`python3 snippetFile.py`

## Snippets

Snippet | What it does | Guide
--- | --- | ---
[addCampaign](functions/addCampaign.py) | Create a campaign | [readme](functions/addCampaign.md)
[addContacts](functions/addContacts.py) | Add contacts | [readme](functions/addContacts.md)
[addList](functions/addList.py) | Create a contact list | [readme](functions/addList.md)
[addTemplate](functions/addTemplate.py) | Create a template | [readme](functions/addTemplate.md)
[deleteCampaign](functions/deleteCampaign.py) | Delete a campaign by name | [readme](functions/deleteCampaign.md)
[deleteContact](functions/deleteContact.py) | Delete one contact by email address | [readme](functions/deleteContact.md)
[deleteContacts](functions/deleteContacts.py) | Delete many contacts in one call | [readme](functions/deleteContacts.md)
[deleteList](functions/deleteList.py) | Delete a list by name | [readme](functions/deleteList.md)
[deleteTemplate](functions/deleteTemplate.py) | Delete a template by name | [readme](functions/deleteTemplate.md)
[exportContacts](functions/exportContacts.py) | Export contacts to a downloadable file | [readme](functions/exportContacts.md)
[loadCampaign](functions/loadCampaign.py) | Load a campaign by name | [readme](functions/loadCampaign.md)
[loadCampaignsStats](functions/loadCampaignsStats.py) | Load statistics for campaigns | [readme](functions/loadCampaignsStats.md)
[loadChannelsStats](functions/loadChannelsStats.py) | Load statistics for channels | [readme](functions/loadChannelsStats.md)
[loadList](functions/loadList.py) | Load a list by name | [readme](functions/loadList.md)
[loadStatistics](functions/loadStatistics.py) | Load account statistics | [readme](functions/loadStatistics.md)
[loadTemplate](functions/loadTemplate.py) | Load a template by name | [readme](functions/loadTemplate.md)
[sendBulkEmails](functions/sendBulkEmails.py) | Send a bulk email with merge fields | [readme](functions/sendBulkEmails.md)
[sendTransactionalEmails](functions/sendTransactionalEmails.py) | Send a transactional email | [readme](functions/sendTransactionalEmails.md)
[sendTransactionalEmailsWithAttachment](functions/sendTransactionalEmailsWithAttachment.py) | Send a transactional email with an attachment | [readme](functions/sendTransactionalEmailsWithAttachment.md)
[updateCampaign](functions/updateCampaign.py) | Update a campaign | [readme](functions/updateCampaign.md)
[uploadContacts](functions/uploadContacts.py) | Import contacts from a CSV file | [readme](functions/uploadContacts.md)
