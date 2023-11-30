from src.service.general_service import GeneralService
from src.dao import cluster_program


class ClusterProgramService(GeneralService):

    _dao = cluster_program

    def get_subjects_in_cluster_program(self, cluster_program_id):
        return cluster_program.get_subjects_in_cluster_program(cluster_program_id)