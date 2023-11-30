from src.controller.general_controller import GeneralController
from src.service import cluster_program_service


class ClusterProgramController(GeneralController):
    _service = cluster_program_service

    def get_subjects_in_cluster_program(self, cluster_program_id):
        return cluster_program_service.get_subjects_in_cluster_program(cluster_program_id)
