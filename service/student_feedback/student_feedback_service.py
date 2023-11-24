from src.service.general_service import GeneralService
from src.dao import student_feedback


class StudentFeedbackService(GeneralService):
    _dao = student_feedback