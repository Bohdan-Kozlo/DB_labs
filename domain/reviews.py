from src import db


class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cluster_program_id = db.Column(db.Integer, db.ForeignKey('cluster_program.id'), nullable=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'),  nullable=True)
    guest_speaker_id = db.Column(db.Integer, db.ForeignKey('guest_speaker.id'),  nullable=True)
    student_feedback = db.relationship("StudentFeedback", backref='reviews')

    def put_into_dto(self):
        return {
            "id": self.id,
            "cluster_program_id": self.cluster_program_id,
            "group_id": self.group_id,
            "guest_speaker_id": self.guest_speaker_id
        }

    @staticmethod
    def crate_from_dto(dto_dict):
        obj = Reviews(
            cluster_program_id=dto_dict.get("cluster_program_id"),
            group_id=dto_dict.get("group_id"),
            guest_speaker_id=dto_dict.get("guest_speaker_id")
        )
        return obj
