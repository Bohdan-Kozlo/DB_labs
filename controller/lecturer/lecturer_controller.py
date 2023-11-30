from src.controller.general_controller import GeneralController
from src.service import lecturer_service


class LecturerController(GeneralController):
    _service = lecturer_service

    def get_classes_for_lecturer(self, lecturer_id):
        return lecturer_service.get_classes_for_lecturer(lecturer_id)