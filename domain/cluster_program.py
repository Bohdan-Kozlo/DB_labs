from src import db


class ClusterProgram(db.Model):
    __tablename__ = "cluster_program"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    university = db.Column(db.String(100), nullable=False)
    subjects = db.relationship('Subject', backref='cluster_program')
    groups = db.relationship("Group", backref='cluster_program')
    reviews = db.relationship('Reviews', backref='cluster_program')

    def __repr__(self):
        return f"Cluster_Program({self.id}, {self.name}, {self.description}, {self.university}"

    def put_into_dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "university": self.university
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = ClusterProgram(
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            university=dto_dict.get("university")
        )
        return obj

