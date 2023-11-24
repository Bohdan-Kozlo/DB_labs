from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from src.controller import student_controller
from src.domain.student import Student

students = Blueprint("student", __name__, url_prefix="/api/v1/students")


@students.get('/')
def get_all_students():
    return make_response(jsonify(student_controller.find_all()), HTTPStatus.OK)


@students.get('/<int:students_id>')
def get_students_by_id(students_id):
    return make_response(jsonify(student_controller.find_by_id(students_id)), HTTPStatus.OK)


@students.post('/')
def create_student():
    context = request.get_json()
    student = Student.crate_from_dto(context)
    student_controller.create(student)
    return make_response(jsonify("Student create"), HTTPStatus.OK)


@students.put('/<int:students_id>')
def update_student(students_id):
    context = request.get_json()
    student = Student.crate_from_dto(context)
    student_controller.update(students_id, student)
    return make_response(jsonify("Student update"), HTTPStatus.OK)


@students.patch('/<int:students_id>')
def patch_student(students_id):
    context = request.get_json()
    student_controller.patch(students_id, context)
    return make_response(jsonify("Student update"), HTTPStatus.OK)


@students.delete('/<int:students_id>')
def delete_student(students_id):
    student_controller.delete(students_id)
    return make_response(jsonify("Student delete"), HTTPStatus.OK)
