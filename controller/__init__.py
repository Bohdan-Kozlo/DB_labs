from .cluster_program.cluster_program_controller import ClusterProgramController
from .subject.subject_controller import SubjectController
from src.controller.group.group_controller import GroupController
from .student.student_controller import StudentController
from .classes.classes_controller import ClassesController
from .guest_speaker.guest_speaker_controller import GuestSpeakerController
from .lecturer.lecturer_controller import LecturerController
from .reviews.reviews_controller import ReviewsController
from .student_feedback.student_feedback_controller import StudentFeedbackController
from .classes_lecturer.classe_lecturer import ClassesLecturerController

cluster_program_controller = ClusterProgramController()
subject_controller = SubjectController()
group_controller = GroupController()
student_controller = StudentController()
classes_controller = ClassesController()
guest_speaker_controller = GuestSpeakerController()
lecturer_controller = LecturerController()
reviews_controller = ReviewsController()
student_feedback_controller = StudentFeedbackController()
classes_lecturer_controller = ClassesLecturerController()


