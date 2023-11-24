from src import db


class Subject(db.Model):

    __tablename__ = "subject"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    cluster_program_id = db.Column(db.Integer, db.ForeignKey('cluster_program.id'))

    classes = db.relationship('Classes', backref='subject')


    def __repr__(self):
        return f"Subject({self.id}, {self.name}, {self.description}, {self.cluster_program_id})"

    def put_into_dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "cluster_program_id": self.cluster_program_id or ""
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Subject(
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            cluster_program_id=dto_dict.get("cluster_program_id ")
        )
        return obj
