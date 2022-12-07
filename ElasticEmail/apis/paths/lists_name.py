from ElasticEmail.paths.lists_name.get import ApiForget
from ElasticEmail.paths.lists_name.put import ApiForput
from ElasticEmail.paths.lists_name.delete import ApiFordelete


class ListsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
