from src.dao.general_dao import GeneralDAO
from src.domain.lecturer import Lecturer


class LecturerDAO(GeneralDAO):
    _domain_type = Lecturer

    def get_classes_for_lecturer(self, lecturer_id):
        try:
            lecturer = Lecturer.query.get(lecturer_id)

            if lecturer:
                classes_for_lecturer = lecturer.classes

                result = [{
                    'class_id': class_obj.id,
                    'class_date': class_obj.date,
                    'class_subject_id': class_obj.subject_id,
                } for class_obj in classes_for_lecturer]

                return result

            else:
                return None

        except Exception as e:
            print(f"Error: {e}")
            return None
