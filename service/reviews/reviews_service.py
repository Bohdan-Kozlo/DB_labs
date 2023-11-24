from src.service.general_service import GeneralService
from src.dao import reviews_dao


class ReviewsService(GeneralService):
    _dao = reviews_dao