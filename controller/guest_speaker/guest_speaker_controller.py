from src.controller.general_controller import GeneralController
from src.service import guest_speaker_service


class GuestSpeakerController(GeneralController):
    _service = guest_speaker_service