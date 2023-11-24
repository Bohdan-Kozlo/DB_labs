from src.service import subject_service
from src.controller.general_controller import GeneralController


class SubjectController(GeneralController):
    _service = subject_service