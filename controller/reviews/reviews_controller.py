from src.controller.general_controller import GeneralController
from src.service import reviews_service


class ReviewsController(GeneralController):
    _service = reviews_service
