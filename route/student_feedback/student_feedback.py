from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from src.controller import student_feedback_controller
from src.domain.student_feedback import StudentFeedback

student_feedback = Blueprint("student_feedback", __name__, url_prefix="/api/v1/student_feedback")


@student_feedback.get('/')
def get_all_student_feedback():
    return make_response(jsonify(student_feedback_controller.find_all()), HTTPStatus.OK)


@student_feedback.get('/<int:feedback_id>')
def get_student_feedback_by_id(feedback_id):
    return make_response(jsonify(student_feedback_controller.find_by_id(feedback_id)), HTTPStatus.OK)


@student_feedback.post('/')
def create_student_feedback():
    context = request.get_json()
    feedback = StudentFeedback.create_from_dto(context)
    student_feedback_controller.create(feedback)
    return make_response(jsonify(feedback.put_into_dto()), HTTPStatus.OK)


@student_feedback.put('/<int:feedback_id>')
def update_student_feedback(feedback_id):
    context = request.get_json()
    feedback = StudentFeedback.create_from_dto(context)
    student_feedback_controller.update(feedback_id, feedback)
    return make_response(jsonify("Student feedback updated"), HTTPStatus.OK)


@student_feedback.patch('/<int:feedback_id>')
def patch_student_feedback(feedback_id):
    context = request.get_json()
    student_feedback_controller.patch(feedback_id, context)
    return make_response(jsonify("Update student feedback"), HTTPStatus.OK)


@student_feedback.delete('/<int:feedback_id>')
def delete_student_feedback(feedback_id):
    student_feedback_controller.delete(feedback_id)
    return make_response(jsonify("Delete student feedback"), HTTPStatus.OK)


@student_feedback.get('/get_student/<int:feedback_id>')
def get_student(feedback_id):
    return make_response(jsonify(student_feedback_controller.get_students_with_feedback(feedback_id)), HTTPStatus.OK)