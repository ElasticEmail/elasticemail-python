# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ElasticEmail.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CAMPAIGNS = "Campaigns"
    CONTACTS = "Contacts"
    EMAILS = "Emails"
    EVENTS = "Events"
    FILES = "Files"
    INBOUND_ROUTE = "InboundRoute"
    LISTS = "Lists"
    SECURITY = "Security"
    SEGMENTS = "Segments"
    STATISTICS = "Statistics"
    SUB_ACCOUNTS = "SubAccounts"
    SUPPRESSIONS = "Suppressions"
    TEMPLATES = "Templates"
    VERIFICATIONS = "Verifications"
