from src.dao.general_dao import GeneralDAO
from src.domain.student_feedback import StudentFeedback


class StudentFeedbackDAO(GeneralDAO):
    _domain_type = StudentFeedback

    def get_students_with_feedback(self, student_id):
        try:
            feedback_objects = self.find_all()

            result = []

            for feedback in feedback_objects:
                if student_id is None or feedback.student_id == student_id:
                    student = feedback.student
                    result.append({
                        "student_id": student.id,
                        "student_name": student.first_name,
                        "feedback_text": feedback.text,
                        "feedback_rating": feedback.rating,
                    })

            return result

        except Exception as e:

            print(f"Error: {e}")
            return None