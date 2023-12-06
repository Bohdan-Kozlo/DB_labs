from flask import Flask

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)

    from src.domain.student_feedback import StudentFeedback
    from src.domain.reviews import Reviews
    from src.route.cluster_program.cluster_program import clusters_programs
    from src.domain.cluster_program import ClusterProgram
    from src.domain.subject import Subject
    from src.route.subject.subject import subjects
    from src.route.eror_handler import err_handler_bp
    from src.domain.group import Group
    from src.route.group.group import groups
    from src.domain.student import Student
    from src.route.student.student import students
    from src.domain.classes import Classes
    from src.route.classes.classes import classes
    from src.domain.lecturer import Lecturer
    from src.route.lecturer.lecturer import lecturers
    from src.domain.guest_speaker import GuestSpeaker
    from src.route.guest_speaker.guest_speaker import guest_speakers
    from src.route.reviews.reviews import reviews
    from src.route.student_feedback.student_feedback import student_feedback
    from src.domain.classes_lecturer import ClassesLecturer
    from src.route.classe_lecturer.classe_lecturer import classes_lecturers


    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:user@localhost/labs5'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config.update(test_config)

    db.app = app
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(clusters_programs)
    app.register_blueprint(subjects)
    app.register_blueprint(err_handler_bp)
    app.register_blueprint(groups)
    app.register_blueprint(students)
    app.register_blueprint(classes)
    app.register_blueprint(lecturers)
    app.register_blueprint(guest_speakers)
    app.register_blueprint(reviews)
    app.register_blueprint(student_feedback)
    app.register_blueprint(classes_lecturers)

    return app


