from src.dao.general_dao import GeneralDAO
from src.domain.classes import Classes


class ClassesDAO(GeneralDAO):
    _domain_type = Classes

    def get_feedback_for_class(self, class_id):
        try:
            class_instance = self.find_by_id(class_id)

            if class_instance:
                feedback_list = class_instance.student_feedback
                result = [{
                    "feedback_id": feedback.id,
                    "text": feedback.text,
                    "rating": feedback.rating,
                    "date": feedback.date,
                } for feedback in feedback_list]

                return result

            return None

        except Exception as e:
            print(f"Error: {e}")
            return None