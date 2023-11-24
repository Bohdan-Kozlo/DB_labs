from src.dao.general_dao import GeneralDAO
from src.domain.student_feedback import StudentFeedback


class StudentFeedbackDAO(GeneralDAO):
    _domain_type = StudentFeedback