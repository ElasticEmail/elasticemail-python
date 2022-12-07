from ElasticEmail.paths.segments_name.get import ApiForget
from ElasticEmail.paths.segments_name.put import ApiForput
from ElasticEmail.paths.segments_name.delete import ApiFordelete


class SegmentsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
