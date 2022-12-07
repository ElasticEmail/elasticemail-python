# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ElasticEmail.paths.security_smtp_name import Api

from ElasticEmail.paths import PathValues

path = PathValues.SECURITY_SMTP_NAME