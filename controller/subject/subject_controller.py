from src.service import subject_service
from src.controller.general_controller import GeneralController


class SubjectController(GeneralController):
    _service = subject_service

    def get_classes_for_subject(self, subject_id):
        return subject_service.get_classes_for_subject(subject_id)