from ElasticEmail.paths.security_smtp_name.get import ApiForget
from ElasticEmail.paths.security_smtp_name.put import ApiForput
from ElasticEmail.paths.security_smtp_name.delete import ApiFordelete


class SecuritySmtpName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
