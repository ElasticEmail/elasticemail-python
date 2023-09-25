from ElasticEmail.paths.inboundroute_id.get import ApiForget
from ElasticEmail.paths.inboundroute_id.put import ApiForput
from ElasticEmail.paths.inboundroute_id.delete import ApiFordelete


class InboundrouteId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
