from src import db


class StudentFeedback(db.Model):
    __tablename__ = "student_feedback"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.String(5), nullable=False)
    date = db.Column(db.Date, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    classes_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=True)
    reviews_id = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=True)

    def put_into_dto(self):
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "date": self.date or "",
            "student_id": self.student_id or "",
            "classes_id": self.classes_id or "",
            "reviews_id": self.reviews_id or ""
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = StudentFeedback(
            text=dto_dict.get("text"),
            date=dto_dict.get("date "),
            rating=dto_dict.get("rating "),
            student_id=dto_dict.get("student_id "),
            classes_id=dto_dict.get("classes_id "),
            reviews_id=dto_dict.get("reviews_id ")
        )
        return obj

