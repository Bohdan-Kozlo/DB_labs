from src.service.general_service import GeneralService
from src.dao import group_dao


class GroupService(GeneralService):

    _dao = group_dao

    def get_students_in_group(self, group_id):
        return group_dao.get_students_in_group(group_id)

