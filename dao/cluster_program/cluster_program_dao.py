from src.dao.general_dao import GeneralDAO
from src.domain.cluster_program import ClusterProgram


class ClusterProgramDao(GeneralDAO):
    _domain_type = ClusterProgram
