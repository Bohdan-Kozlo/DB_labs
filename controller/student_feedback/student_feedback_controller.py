from src.controller.general_controller import GeneralController
from src.service import student_feedback_service


class StudentFeedbackController(GeneralController):
    _service = student_feedback_service