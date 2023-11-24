from src.service.general_service import GeneralService
from src.dao import lecturer_dao


class LecturerService(GeneralService):
    _dao = lecturer_dao