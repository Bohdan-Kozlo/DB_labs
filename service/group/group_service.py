from src.service.general_service import GeneralService
from src.dao import group_dao


class GroupService(GeneralService):

    _dao = group_dao

