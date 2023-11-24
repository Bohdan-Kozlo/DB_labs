from src.dao.general_dao import GeneralDAO
from src.domain.lecturer import Lecturer


class LecturerDAO(GeneralDAO):
    _domain_type = Lecturer