# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from ElasticEmail.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from ElasticEmail.model.access_level import AccessLevel
from ElasticEmail.model.account_status_enum import AccountStatusEnum
from ElasticEmail.model.api_key import ApiKey
from ElasticEmail.model.api_key_payload import ApiKeyPayload
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.campaign import Campaign
from ElasticEmail.model.campaign_options import CampaignOptions
from ElasticEmail.model.campaign_recipient import CampaignRecipient
from ElasticEmail.model.campaign_status import CampaignStatus
from ElasticEmail.model.campaign_template import CampaignTemplate
from ElasticEmail.model.channel_log_status_summary import ChannelLogStatusSummary
from ElasticEmail.model.compression_format import CompressionFormat
from ElasticEmail.model.consent_data import ConsentData
from ElasticEmail.model.consent_tracking import ConsentTracking
from ElasticEmail.model.contact import Contact
from ElasticEmail.model.contact_activity import ContactActivity
from ElasticEmail.model.contact_hist_event_type import ContactHistEventType
from ElasticEmail.model.contact_history import ContactHistory
from ElasticEmail.model.contact_payload import ContactPayload
from ElasticEmail.model.contact_source import ContactSource
from ElasticEmail.model.contact_status import ContactStatus
from ElasticEmail.model.contact_update_payload import ContactUpdatePayload
from ElasticEmail.model.contacts_list import ContactsList
from ElasticEmail.model.delivery_optimization_type import DeliveryOptimizationType
from ElasticEmail.model.email_content import EmailContent
from ElasticEmail.model.email_data import EmailData
from ElasticEmail.model.email_message_data import EmailMessageData
from ElasticEmail.model.email_recipient import EmailRecipient
from ElasticEmail.model.email_send import EmailSend
from ElasticEmail.model.email_status import EmailStatus
from ElasticEmail.model.email_transactional_message_data import EmailTransactionalMessageData
from ElasticEmail.model.email_validation_result import EmailValidationResult
from ElasticEmail.model.email_validation_status import EmailValidationStatus
from ElasticEmail.model.email_view import EmailView
from ElasticEmail.model.emails_payload import EmailsPayload
from ElasticEmail.model.encoding_type import EncodingType
from ElasticEmail.model.event_type import EventType
from ElasticEmail.model.events_order_by import EventsOrderBy
from ElasticEmail.model.export_file_formats import ExportFileFormats
from ElasticEmail.model.export_link import ExportLink
from ElasticEmail.model.export_status import ExportStatus
from ElasticEmail.model.file_info import FileInfo
from ElasticEmail.model.file_payload import FilePayload
from ElasticEmail.model.file_upload_result import FileUploadResult
from ElasticEmail.model.inbound_payload import InboundPayload
from ElasticEmail.model.inbound_route import InboundRoute
from ElasticEmail.model.inbound_route_action_type import InboundRouteActionType
from ElasticEmail.model.inbound_route_filter_type import InboundRouteFilterType
from ElasticEmail.model.list_payload import ListPayload
from ElasticEmail.model.list_update_payload import ListUpdatePayload
from ElasticEmail.model.log_job_status import LogJobStatus
from ElasticEmail.model.log_status_summary import LogStatusSummary
from ElasticEmail.model.merge_email_payload import MergeEmailPayload
from ElasticEmail.model.message_attachment import MessageAttachment
from ElasticEmail.model.message_category import MessageCategory
from ElasticEmail.model.new_api_key import NewApiKey
from ElasticEmail.model.new_smtp_credentials import NewSmtpCredentials
from ElasticEmail.model.options import Options
from ElasticEmail.model.recipient_event import RecipientEvent
from ElasticEmail.model.segment import Segment
from ElasticEmail.model.segment_payload import SegmentPayload
from ElasticEmail.model.smtp_credentials import SmtpCredentials
from ElasticEmail.model.smtp_credentials_payload import SmtpCredentialsPayload
from ElasticEmail.model.sort_order_item import SortOrderItem
from ElasticEmail.model.split_optimization_type import SplitOptimizationType
from ElasticEmail.model.split_options import SplitOptions
from ElasticEmail.model.sub_account_info import SubAccountInfo
from ElasticEmail.model.subaccount_email_credits_payload import SubaccountEmailCreditsPayload
from ElasticEmail.model.subaccount_email_settings import SubaccountEmailSettings
from ElasticEmail.model.subaccount_email_settings_payload import SubaccountEmailSettingsPayload
from ElasticEmail.model.subaccount_payload import SubaccountPayload
from ElasticEmail.model.subaccount_settings_info import SubaccountSettingsInfo
from ElasticEmail.model.subaccount_settings_info_payload import SubaccountSettingsInfoPayload
from ElasticEmail.model.suppression import Suppression
from ElasticEmail.model.template import Template
from ElasticEmail.model.template_payload import TemplatePayload
from ElasticEmail.model.template_scope import TemplateScope
from ElasticEmail.model.template_type import TemplateType
from ElasticEmail.model.transactional_recipient import TransactionalRecipient
from ElasticEmail.model.utm import Utm
from ElasticEmail.model.verification_file_result import VerificationFileResult
from ElasticEmail.model.verification_file_result_details import VerificationFileResultDetails
from ElasticEmail.model.verification_status import VerificationStatus
