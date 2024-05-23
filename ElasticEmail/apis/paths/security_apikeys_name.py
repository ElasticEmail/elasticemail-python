from ElasticEmail.paths.security_apikeys_name.get import ApiForget
from ElasticEmail.paths.security_apikeys_name.put import ApiForput
from ElasticEmail.paths.security_apikeys_name.delete import ApiFordelete


class SecurityApikeysName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
