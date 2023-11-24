from src import db


class ClassesLecturer(db.Model):
    __tablename__ = "classes_lecturers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'), nullable=False)

    lecturer = db.relationship('Lecturer', back_populates='classes_lecturers')

    def put_into_dto(self):
        return {
            "id": self.id,
            "class_id": self.class_id,
            "lecturer_id": self.lecturer_id
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = ClassesLecturer(
            class_id=dto_dict.get("class_id"),
            lecturer_id=dto_dict.get("lecturer_id"),
        )
        return obj