from src.controller.general_controller import GeneralController
from src.service import lecturer_service


class LecturerController(GeneralController):
    _service = lecturer_service