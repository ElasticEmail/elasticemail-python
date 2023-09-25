from ElasticEmail.paths.templates_name.get import ApiForget
from ElasticEmail.paths.templates_name.put import ApiForput
from ElasticEmail.paths.templates_name.delete import ApiFordelete


class TemplatesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
