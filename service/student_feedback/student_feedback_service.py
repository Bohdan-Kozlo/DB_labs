from src.service.general_service import GeneralService
from src.dao import student_feedback


class StudentFeedbackService(GeneralService):
    _dao = student_feedback

    def get_students_with_feedback(self, student_id):
        return self._dao.get_students_with_feedback(student_id)

