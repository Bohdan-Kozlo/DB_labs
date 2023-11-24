from src.service.general_service import GeneralService
from src.dao import subject_dao


class SubjectService(GeneralService):

    _dao = subject_dao