from src.service.general_service import GeneralService
from src.dao import student_dao


class StudentService(GeneralService):
    _dao = student_dao