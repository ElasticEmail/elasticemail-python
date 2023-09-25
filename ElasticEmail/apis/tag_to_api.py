import typing_extensions

from ElasticEmail.apis.tags import TagValues
from ElasticEmail.apis.tags.campaigns_api import CampaignsApi
from ElasticEmail.apis.tags.contacts_api import ContactsApi
from ElasticEmail.apis.tags.emails_api import EmailsApi
from ElasticEmail.apis.tags.events_api import EventsApi
from ElasticEmail.apis.tags.files_api import FilesApi
from ElasticEmail.apis.tags.inbound_route_api import InboundRouteApi
from ElasticEmail.apis.tags.lists_api import ListsApi
from ElasticEmail.apis.tags.security_api import SecurityApi
from ElasticEmail.apis.tags.segments_api import SegmentsApi
from ElasticEmail.apis.tags.statistics_api import StatisticsApi
from ElasticEmail.apis.tags.sub_accounts_api import SubAccountsApi
from ElasticEmail.apis.tags.suppressions_api import SuppressionsApi
from ElasticEmail.apis.tags.templates_api import TemplatesApi
from ElasticEmail.apis.tags.verifications_api import VerificationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.EMAILS: EmailsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FILES: FilesApi,
        TagValues.INBOUND_ROUTE: InboundRouteApi,
        TagValues.LISTS: ListsApi,
        TagValues.SECURITY: SecurityApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.STATISTICS: StatisticsApi,
        TagValues.SUB_ACCOUNTS: SubAccountsApi,
        TagValues.SUPPRESSIONS: SuppressionsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.VERIFICATIONS: VerificationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.EMAILS: EmailsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FILES: FilesApi,
        TagValues.INBOUND_ROUTE: InboundRouteApi,
        TagValues.LISTS: ListsApi,
        TagValues.SECURITY: SecurityApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.STATISTICS: StatisticsApi,
        TagValues.SUB_ACCOUNTS: SubAccountsApi,
        TagValues.SUPPRESSIONS: SuppressionsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.VERIFICATIONS: VerificationsApi,
    }
)
