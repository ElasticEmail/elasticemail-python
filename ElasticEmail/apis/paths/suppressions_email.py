from ElasticEmail.paths.suppressions_email.get import ApiForget
from ElasticEmail.paths.suppressions_email.delete import ApiFordelete


class SuppressionsEmail(
    ApiForget,
    ApiFordelete,
):
    pass
