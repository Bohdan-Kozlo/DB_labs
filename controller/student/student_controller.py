from src.controller.general_controller import GeneralController
from src.service import student_service


class StudentController(GeneralController):
    _service = student_service