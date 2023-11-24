from src.dao.cluster_program.cluster_program_dao import ClusterProgramDao
from src.dao.subject.subject_dao import SubjectDAO
from src.dao.group.group_dao import GroupDAO
from src.dao.student.student_dao import StudentDAO
from src.dao.classes.classes import ClassesDAO
from .lecturer.lecturer import LecturerDAO
from .guest_speaker.guest_speaker import GuestSpeakerDAO
from .classes_lecturer.classes_lecturer_dao import ClassesLecturerDAO
from .reviews.reviews_dao import ReviewsDAO
from .student_feedback.student_feedback import StudentFeedbackDAO

cluster_program = ClusterProgramDao()
subject_dao = SubjectDAO()
group_dao = GroupDAO()
student_dao = StudentDAO()
classes_dao = ClassesDAO()
lecturer_dao = LecturerDAO()
guest_speaker = GuestSpeakerDAO()
classes_lecturer_dao = ClassesLecturerDAO()
reviews_dao = ReviewsDAO()
student_feedback = StudentFeedbackDAO()
