from src.controller.general_controller import GeneralController
from src.service import student_feedback_service


class StudentFeedbackController(GeneralController):
    _service = student_feedback_service

    def get_students_with_feedback(self, student_id):
        return self._service.get_students_with_feedback(student_id)