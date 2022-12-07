from ElasticEmail.paths.verifications_email.get import ApiForget
from ElasticEmail.paths.verifications_email.post import ApiForpost
from ElasticEmail.paths.verifications_email.delete import ApiFordelete


class VerificationsEmail(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
