from src.service.general_service import GeneralService
from src.dao import subject_dao


class SubjectService(GeneralService):

    _dao = subject_dao

    def get_classes_for_subject(self, subject_id):
        return subject_dao.get_classes_for_subject(subject_id)