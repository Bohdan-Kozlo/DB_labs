from src import db


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    cluster_program_id = db.Column(db.Integer, db.ForeignKey('cluster_program.id'))
    students = db.relationship("Student", backref='group')




    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "cluster_program_id": self.cluster_program_id or ""
        }

    def put_into_dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "cluster_program_id": self.cluster_program_id or ""
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Group(
            name=dto_dict.get("name"),
            cluster_program_id=dto_dict.get("cluster_program_id ")
        )
        return obj

