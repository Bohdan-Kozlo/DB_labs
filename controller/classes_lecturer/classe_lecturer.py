from src.controller.general_controller import GeneralController
from src.service import classes_lecturer_service


class ClassesLecturerController(GeneralController):
    _service = classes_lecturer_service

    def get_all_relationship_data(self):
        return self._service.get_all_relationship_data()