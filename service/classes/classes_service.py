from src.service.general_service import GeneralService
from src.dao import classes_dao


class ClassesService(GeneralService):
    _dao = classes_dao

    def get_feedback_for_class(self, classes_id):
        return classes_dao.get_feedback_for_class(classes_id)