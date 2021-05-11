
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.campaigns_api import CampaignsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ElasticEmail.api.campaigns_api import CampaignsApi
from ElasticEmail.api.contacts_api import ContactsApi
from ElasticEmail.api.emails_api import EmailsApi
from ElasticEmail.api.events_api import EventsApi
from ElasticEmail.api.files_api import FilesApi
from ElasticEmail.api.inbound_route_api import InboundRouteApi
from ElasticEmail.api.lists_api import ListsApi
from ElasticEmail.api.security_api import SecurityApi
from ElasticEmail.api.segments_api import SegmentsApi
from ElasticEmail.api.statistics_api import StatisticsApi
from ElasticEmail.api.sub_accounts_api import SubAccountsApi
from ElasticEmail.api.suppressions_api import SuppressionsApi
from ElasticEmail.api.templates_api import TemplatesApi
from ElasticEmail.api.verifications_api import VerificationsApi
