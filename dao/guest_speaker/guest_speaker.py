from src.dao.general_dao import GeneralDAO
from src.domain.guest_speaker import GuestSpeaker


class GuestSpeakerDAO(GeneralDAO):
    _domain_type = GuestSpeaker