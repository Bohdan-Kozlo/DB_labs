from src.dao.general_dao import GeneralDAO
from src.domain.group import Group


class GroupDAO(GeneralDAO):
    _domain_type = Group