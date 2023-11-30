from src.service import group_service
from src.controller.general_controller import GeneralController


class GroupController(GeneralController):

    _service = group_service

    def get_students_in_group(self, group_id):
        return group_service.get_students_in_group(group_id)

