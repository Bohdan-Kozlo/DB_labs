from src import db


class Lecturer(db.Model):
    __tablename__ = "lecturer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    classes = db.relationship("Classes",  backref='lecturer')
    classes_lecturers = db.relationship('ClassesLecturer', back_populates='lecturer')

    def put_into_dto(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Lecturer(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            phone=dto_dict.get("phone"),
            email=dto_dict.get("email")
        )
        return obj