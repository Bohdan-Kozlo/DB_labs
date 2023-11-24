from src import db


class Classes(db.Model):
    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    student_feedback = db.relationship("StudentFeedback", backref='classes')

    def put_into_dto(self):
        return {
            "id": self.id,
            "date": self.date,
            "subject_id": self.subject_id
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Classes(
            name=dto_dict.get("name"),
            date=dto_dict.get("date"),
            subject_id=dto_dict.get("subject_id")
        )
        return obj