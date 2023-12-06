from src.service.general_service import GeneralService
from src.dao import classes_lecturer


class ClassesLecturerService(GeneralService):
    _dao = classes_lecturer

    def get_all_relationship_data(self):
        return self._dao.get_all_relationship_data()