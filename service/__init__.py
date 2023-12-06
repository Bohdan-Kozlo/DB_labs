from .cluster_program.cluster_program_service import ClusterProgramService
from .subject_service.subject_service import SubjectService
from .group.group_service import GroupService
from .student.student_service import StudentService
from .classes.classes_service import ClassesService
from .lecturer.lecturer_service import LecturerService
from .guest_speaker.guest_speaker_service import GuestSpeakerDAO
from .reviews.reviews_service import ReviewsService
from .student_feedback.student_feedback_service import StudentFeedbackService
from .classes_lecturer.classes_lecturer_service import ClassesLecturerService

cluster_program_service = ClusterProgramService()
subject_service = SubjectService()
group_service = GroupService()
student_service = StudentService()
classes_service = ClassesService()
lecturer_service = LecturerService()
guest_speaker_service = GuestSpeakerDAO()
reviews_service = ReviewsService()
student_feedback_service = StudentFeedbackService()
classes_lecturer_service = ClassesLecturerService()