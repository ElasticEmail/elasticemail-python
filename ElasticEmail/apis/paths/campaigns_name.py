from ElasticEmail.paths.campaigns_name.get import ApiForget
from ElasticEmail.paths.campaigns_name.put import ApiForput
from ElasticEmail.paths.campaigns_name.delete import ApiFordelete


class CampaignsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
