from src.service.general_service import GeneralService
from src.dao import classes_dao


class ClassesService(GeneralService):
    _dao = classes_dao