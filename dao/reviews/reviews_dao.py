from src.dao.general_dao import GeneralDAO
from src.domain.reviews import Reviews


class ReviewsDAO(GeneralDAO):
    _domain_type = Reviews
