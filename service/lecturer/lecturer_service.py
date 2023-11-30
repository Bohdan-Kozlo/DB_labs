from src.service.general_service import GeneralService
from src.dao import lecturer_dao


class LecturerService(GeneralService):
    _dao = lecturer_dao

    def get_classes_for_lecturer(self, lecturer_id):
        return lecturer_dao.get_classes_for_lecturer(lecturer_id)