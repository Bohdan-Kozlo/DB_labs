from src.dao.general_dao import GeneralDAO
from src.domain.subject import Subject


class SubjectDAO(GeneralDAO):

    _domain_type = Subject

    def get_classes_for_subject(self, subject_id):
        try:
            subject = self.find_by_id(subject_id)

            if subject:
                classes_list = subject.classes
                result = [{
                    "class_id": class_.id,
                    "date": class_.date,
                } for class_ in classes_list]

                return result

            return None

        except Exception as e:
            print(f"Error: {e}")
            return None