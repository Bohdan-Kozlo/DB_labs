from src.dao.general_dao import GeneralDAO
from src.domain.student import Student


class StudentDAO(GeneralDAO):
    _domain_type = Student
