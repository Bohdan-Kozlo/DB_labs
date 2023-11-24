from src.controller.general_controller import GeneralController
from src.service import classes_service


class ClassesController(GeneralController):
    _service = classes_service
