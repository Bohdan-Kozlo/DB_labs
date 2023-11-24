from src.domain.classes_lecturer import ClassesLecturer
from src.dao.general_dao import GeneralDAO
from src.domain.classes import Classes
from src.domain.lecturer import Lecturer


class ClassesLecturerDAO(GeneralDAO):

    _domain_type = ClassesLecturer

    def get_all_relationship_data(self):
        try:

            relationship_data = ClassesLecturer.query.all()

            result = []

            for entry in relationship_data:

                class_data = Classes.query.get(entry.class_id)
                lecturer_data = Lecturer.query.get(entry.lecturer_id)

                result.append({
                    'classes_id': entry.class_id,
                    'lecturer_id': entry.lecturer_id,
                    'class_data': {
                        'id': class_data.id,
                        'date': class_data.date,
                        'subject_id': class_data.subject_id,

                    },
                    'lecturer_data': {
                        'id': lecturer_data.id,
                        'first_name': lecturer_data.first_name,
                        'last_name': lecturer_data.last_name,
                        'phone': lecturer_data.phone,
                        'email': lecturer_data.email,
                        # Додайте інші поля, які вам потрібні
                    },

                })

            return result

        except Exception as e:
            # Обробка помилок
            print(f"Error: {e}")
            return None