from src.controller.general_controller import GeneralController
from src.service import cluster_program_service


class ClusterProgramController(GeneralController):
    _service = cluster_program_service
