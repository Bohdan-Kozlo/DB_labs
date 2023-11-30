from src.dao.general_dao import GeneralDAO
from src.domain.group import Group


class GroupDAO(GeneralDAO):
    _domain_type = Group

    def get_students_in_group(self, group_id):
        try:

            group = self.find_by_id(group_id)

            if not group:
                return None

            students_in_group = group.students

            result = []

            for student in students_in_group:
                result.append({
                    "student_id": student.id,
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "phone": student.phone,
                    "email": student.email,
                })

            return result

        except Exception as e:
            print(f"Error: {e}")
            return None