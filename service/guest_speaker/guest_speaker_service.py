from src.service.general_service import GeneralService
from src.dao import guest_speaker


class GuestSpeakerDAO(GeneralService):
    _dao = guest_speaker