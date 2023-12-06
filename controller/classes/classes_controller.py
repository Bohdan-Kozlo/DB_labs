from src.controller.general_controller import GeneralController
from src.service import classes_service


class ClassesController(GeneralController):
    _service = classes_service

    def get_feedback_for_class(self, classes_id):
        return classes_service.get_feedback_for_class(classes_id)
