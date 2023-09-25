import typing_extensions

from ElasticEmail.paths import PathValues
from ElasticEmail.apis.paths.campaigns import Campaigns
from ElasticEmail.apis.paths.campaigns_name import CampaignsName
from ElasticEmail.apis.paths.contacts import Contacts
from ElasticEmail.apis.paths.contacts_email import ContactsEmail
from ElasticEmail.apis.paths.contacts_delete import ContactsDelete
from ElasticEmail.apis.paths.contacts_export import ContactsExport
from ElasticEmail.apis.paths.contacts_export_id_status import ContactsExportIdStatus
from ElasticEmail.apis.paths.contacts_import import ContactsImport
from ElasticEmail.apis.paths.emails import Emails
from ElasticEmail.apis.paths.emails_msgid_view import EmailsMsgidView
from ElasticEmail.apis.paths.emails_mergefile import EmailsMergefile
from ElasticEmail.apis.paths.emails_transactional import EmailsTransactional
from ElasticEmail.apis.paths.events import Events
from ElasticEmail.apis.paths.events_transactionid import EventsTransactionid
from ElasticEmail.apis.paths.events_channels_name import EventsChannelsName
from ElasticEmail.apis.paths.events_channels_name_export import EventsChannelsNameExport
from ElasticEmail.apis.paths.events_channels_export_id_status import EventsChannelsExportIdStatus
from ElasticEmail.apis.paths.events_export import EventsExport
from ElasticEmail.apis.paths.events_export_id_status import EventsExportIdStatus
from ElasticEmail.apis.paths.files import Files
from ElasticEmail.apis.paths.files_name import FilesName
from ElasticEmail.apis.paths.files_name_info import FilesNameInfo
from ElasticEmail.apis.paths.inboundroute import Inboundroute
from ElasticEmail.apis.paths.inboundroute_id import InboundrouteId
from ElasticEmail.apis.paths.inboundroute_order import InboundrouteOrder
from ElasticEmail.apis.paths.lists import Lists
from ElasticEmail.apis.paths.lists_name import ListsName
from ElasticEmail.apis.paths.lists_name_contacts import ListsNameContacts
from ElasticEmail.apis.paths.lists_name_contacts_remove import ListsNameContactsRemove
from ElasticEmail.apis.paths.security_apikeys import SecurityApikeys
from ElasticEmail.apis.paths.security_apikeys_name import SecurityApikeysName
from ElasticEmail.apis.paths.security_smtp import SecuritySmtp
from ElasticEmail.apis.paths.security_smtp_name import SecuritySmtpName
from ElasticEmail.apis.paths.segments import Segments
from ElasticEmail.apis.paths.segments_name import SegmentsName
from ElasticEmail.apis.paths.statistics import Statistics
from ElasticEmail.apis.paths.statistics_campaigns import StatisticsCampaigns
from ElasticEmail.apis.paths.statistics_campaigns_name import StatisticsCampaignsName
from ElasticEmail.apis.paths.statistics_channels import StatisticsChannels
from ElasticEmail.apis.paths.statistics_channels_name import StatisticsChannelsName
from ElasticEmail.apis.paths.subaccounts import Subaccounts
from ElasticEmail.apis.paths.subaccounts_email import SubaccountsEmail
from ElasticEmail.apis.paths.subaccounts_email_credits import SubaccountsEmailCredits
from ElasticEmail.apis.paths.subaccounts_email_settings_email import SubaccountsEmailSettingsEmail
from ElasticEmail.apis.paths.suppressions import Suppressions
from ElasticEmail.apis.paths.suppressions_email import SuppressionsEmail
from ElasticEmail.apis.paths.suppressions_bounces import SuppressionsBounces
from ElasticEmail.apis.paths.suppressions_bounces_import import SuppressionsBouncesImport
from ElasticEmail.apis.paths.suppressions_complaints import SuppressionsComplaints
from ElasticEmail.apis.paths.suppressions_complaints_import import SuppressionsComplaintsImport
from ElasticEmail.apis.paths.suppressions_unsubscribes import SuppressionsUnsubscribes
from ElasticEmail.apis.paths.suppressions_unsubscribes_import import SuppressionsUnsubscribesImport
from ElasticEmail.apis.paths.templates import Templates
from ElasticEmail.apis.paths.templates_name import TemplatesName
from ElasticEmail.apis.paths.verifications import Verifications
from ElasticEmail.apis.paths.verifications_email import VerificationsEmail
from ElasticEmail.apis.paths.verifications_files import VerificationsFiles
from ElasticEmail.apis.paths.verifications_files_id import VerificationsFilesId
from ElasticEmail.apis.paths.verifications_files_id_result import VerificationsFilesIdResult
from ElasticEmail.apis.paths.verifications_files_id_result_download import VerificationsFilesIdResultDownload
from ElasticEmail.apis.paths.verifications_files_id_verification import VerificationsFilesIdVerification
from ElasticEmail.apis.paths.verifications_files_result import VerificationsFilesResult

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CAMPAIGNS: Campaigns,
        PathValues.CAMPAIGNS_NAME: CampaignsName,
        PathValues.CONTACTS: Contacts,
        PathValues.CONTACTS_EMAIL: ContactsEmail,
        PathValues.CONTACTS_DELETE: ContactsDelete,
        PathValues.CONTACTS_EXPORT: ContactsExport,
        PathValues.CONTACTS_EXPORT_ID_STATUS: ContactsExportIdStatus,
        PathValues.CONTACTS_IMPORT: ContactsImport,
        PathValues.EMAILS: Emails,
        PathValues.EMAILS_MSGID_VIEW: EmailsMsgidView,
        PathValues.EMAILS_MERGEFILE: EmailsMergefile,
        PathValues.EMAILS_TRANSACTIONAL: EmailsTransactional,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_TRANSACTIONID: EventsTransactionid,
        PathValues.EVENTS_CHANNELS_NAME: EventsChannelsName,
        PathValues.EVENTS_CHANNELS_NAME_EXPORT: EventsChannelsNameExport,
        PathValues.EVENTS_CHANNELS_EXPORT_ID_STATUS: EventsChannelsExportIdStatus,
        PathValues.EVENTS_EXPORT: EventsExport,
        PathValues.EVENTS_EXPORT_ID_STATUS: EventsExportIdStatus,
        PathValues.FILES: Files,
        PathValues.FILES_NAME: FilesName,
        PathValues.FILES_NAME_INFO: FilesNameInfo,
        PathValues.INBOUNDROUTE: Inboundroute,
        PathValues.INBOUNDROUTE_ID: InboundrouteId,
        PathValues.INBOUNDROUTE_ORDER: InboundrouteOrder,
        PathValues.LISTS: Lists,
        PathValues.LISTS_NAME: ListsName,
        PathValues.LISTS_NAME_CONTACTS: ListsNameContacts,
        PathValues.LISTS_NAME_CONTACTS_REMOVE: ListsNameContactsRemove,
        PathValues.SECURITY_APIKEYS: SecurityApikeys,
        PathValues.SECURITY_APIKEYS_NAME: SecurityApikeysName,
        PathValues.SECURITY_SMTP: SecuritySmtp,
        PathValues.SECURITY_SMTP_NAME: SecuritySmtpName,
        PathValues.SEGMENTS: Segments,
        PathValues.SEGMENTS_NAME: SegmentsName,
        PathValues.STATISTICS: Statistics,
        PathValues.STATISTICS_CAMPAIGNS: StatisticsCampaigns,
        PathValues.STATISTICS_CAMPAIGNS_NAME: StatisticsCampaignsName,
        PathValues.STATISTICS_CHANNELS: StatisticsChannels,
        PathValues.STATISTICS_CHANNELS_NAME: StatisticsChannelsName,
        PathValues.SUBACCOUNTS: Subaccounts,
        PathValues.SUBACCOUNTS_EMAIL: SubaccountsEmail,
        PathValues.SUBACCOUNTS_EMAIL_CREDITS: SubaccountsEmailCredits,
        PathValues.SUBACCOUNTS_EMAIL_SETTINGS_EMAIL: SubaccountsEmailSettingsEmail,
        PathValues.SUPPRESSIONS: Suppressions,
        PathValues.SUPPRESSIONS_EMAIL: SuppressionsEmail,
        PathValues.SUPPRESSIONS_BOUNCES: SuppressionsBounces,
        PathValues.SUPPRESSIONS_BOUNCES_IMPORT: SuppressionsBouncesImport,
        PathValues.SUPPRESSIONS_COMPLAINTS: SuppressionsComplaints,
        PathValues.SUPPRESSIONS_COMPLAINTS_IMPORT: SuppressionsComplaintsImport,
        PathValues.SUPPRESSIONS_UNSUBSCRIBES: SuppressionsUnsubscribes,
        PathValues.SUPPRESSIONS_UNSUBSCRIBES_IMPORT: SuppressionsUnsubscribesImport,
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_NAME: TemplatesName,
        PathValues.VERIFICATIONS: Verifications,
        PathValues.VERIFICATIONS_EMAIL: VerificationsEmail,
        PathValues.VERIFICATIONS_FILES: VerificationsFiles,
        PathValues.VERIFICATIONS_FILES_ID: VerificationsFilesId,
        PathValues.VERIFICATIONS_FILES_ID_RESULT: VerificationsFilesIdResult,
        PathValues.VERIFICATIONS_FILES_ID_RESULT_DOWNLOAD: VerificationsFilesIdResultDownload,
        PathValues.VERIFICATIONS_FILES_ID_VERIFICATION: VerificationsFilesIdVerification,
        PathValues.VERIFICATIONS_FILES_RESULT: VerificationsFilesResult,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CAMPAIGNS: Campaigns,
        PathValues.CAMPAIGNS_NAME: CampaignsName,
        PathValues.CONTACTS: Contacts,
        PathValues.CONTACTS_EMAIL: ContactsEmail,
        PathValues.CONTACTS_DELETE: ContactsDelete,
        PathValues.CONTACTS_EXPORT: ContactsExport,
        PathValues.CONTACTS_EXPORT_ID_STATUS: ContactsExportIdStatus,
        PathValues.CONTACTS_IMPORT: ContactsImport,
        PathValues.EMAILS: Emails,
        PathValues.EMAILS_MSGID_VIEW: EmailsMsgidView,
        PathValues.EMAILS_MERGEFILE: EmailsMergefile,
        PathValues.EMAILS_TRANSACTIONAL: EmailsTransactional,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_TRANSACTIONID: EventsTransactionid,
        PathValues.EVENTS_CHANNELS_NAME: EventsChannelsName,
        PathValues.EVENTS_CHANNELS_NAME_EXPORT: EventsChannelsNameExport,
        PathValues.EVENTS_CHANNELS_EXPORT_ID_STATUS: EventsChannelsExportIdStatus,
        PathValues.EVENTS_EXPORT: EventsExport,
        PathValues.EVENTS_EXPORT_ID_STATUS: EventsExportIdStatus,
        PathValues.FILES: Files,
        PathValues.FILES_NAME: FilesName,
        PathValues.FILES_NAME_INFO: FilesNameInfo,
        PathValues.INBOUNDROUTE: Inboundroute,
        PathValues.INBOUNDROUTE_ID: InboundrouteId,
        PathValues.INBOUNDROUTE_ORDER: InboundrouteOrder,
        PathValues.LISTS: Lists,
        PathValues.LISTS_NAME: ListsName,
        PathValues.LISTS_NAME_CONTACTS: ListsNameContacts,
        PathValues.LISTS_NAME_CONTACTS_REMOVE: ListsNameContactsRemove,
        PathValues.SECURITY_APIKEYS: SecurityApikeys,
        PathValues.SECURITY_APIKEYS_NAME: SecurityApikeysName,
        PathValues.SECURITY_SMTP: SecuritySmtp,
        PathValues.SECURITY_SMTP_NAME: SecuritySmtpName,
        PathValues.SEGMENTS: Segments,
        PathValues.SEGMENTS_NAME: SegmentsName,
        PathValues.STATISTICS: Statistics,
        PathValues.STATISTICS_CAMPAIGNS: StatisticsCampaigns,
        PathValues.STATISTICS_CAMPAIGNS_NAME: StatisticsCampaignsName,
        PathValues.STATISTICS_CHANNELS: StatisticsChannels,
        PathValues.STATISTICS_CHANNELS_NAME: StatisticsChannelsName,
        PathValues.SUBACCOUNTS: Subaccounts,
        PathValues.SUBACCOUNTS_EMAIL: SubaccountsEmail,
        PathValues.SUBACCOUNTS_EMAIL_CREDITS: SubaccountsEmailCredits,
        PathValues.SUBACCOUNTS_EMAIL_SETTINGS_EMAIL: SubaccountsEmailSettingsEmail,
        PathValues.SUPPRESSIONS: Suppressions,
        PathValues.SUPPRESSIONS_EMAIL: SuppressionsEmail,
        PathValues.SUPPRESSIONS_BOUNCES: SuppressionsBounces,
        PathValues.SUPPRESSIONS_BOUNCES_IMPORT: SuppressionsBouncesImport,
        PathValues.SUPPRESSIONS_COMPLAINTS: SuppressionsComplaints,
        PathValues.SUPPRESSIONS_COMPLAINTS_IMPORT: SuppressionsComplaintsImport,
        PathValues.SUPPRESSIONS_UNSUBSCRIBES: SuppressionsUnsubscribes,
        PathValues.SUPPRESSIONS_UNSUBSCRIBES_IMPORT: SuppressionsUnsubscribesImport,
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_NAME: TemplatesName,
        PathValues.VERIFICATIONS: Verifications,
        PathValues.VERIFICATIONS_EMAIL: VerificationsEmail,
        PathValues.VERIFICATIONS_FILES: VerificationsFiles,
        PathValues.VERIFICATIONS_FILES_ID: VerificationsFilesId,
        PathValues.VERIFICATIONS_FILES_ID_RESULT: VerificationsFilesIdResult,
        PathValues.VERIFICATIONS_FILES_ID_RESULT_DOWNLOAD: VerificationsFilesIdResultDownload,
        PathValues.VERIFICATIONS_FILES_ID_VERIFICATION: VerificationsFilesIdVerification,
        PathValues.VERIFICATIONS_FILES_RESULT: VerificationsFilesResult,
    }
)
