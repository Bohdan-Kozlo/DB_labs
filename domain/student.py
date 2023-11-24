from src import db


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    reviews = db.relationship("StudentFeedback", backref='student')


    def __repr__(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "group_id": self.group_id
        }

    def put_into_dto(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "group_id": self.group_id
        }

    @staticmethod
    def crate_from_dto(dto_dict):
        obj = Student(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            phone=dto_dict.get("phone"),
            email=dto_dict.get("email"),
            group_id=dto_dict.get("group_id")
        )
        return obj
