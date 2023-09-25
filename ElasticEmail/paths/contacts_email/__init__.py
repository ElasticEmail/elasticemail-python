# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ElasticEmail.paths.contacts_email import Api

from ElasticEmail.paths import PathValues

path = PathValues.CONTACTS_EMAIL