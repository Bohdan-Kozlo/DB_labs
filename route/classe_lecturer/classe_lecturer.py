from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from src.controller import classes_lecturer_controller
from src.domain.classes_lecturer import ClassesLecturer


classes_lecturers = Blueprint("classes_lecturer", __name__, url_prefix="/api/v1/classes_lecturers")


@classes_lecturers.get('/')
def get_all_classes_lecturer():
    return make_response(jsonify(classes_lecturer_controller.get_all_relationship_data()), HTTPStatus.OK)


@classes_lecturers.post('/')
def create_classes_lecturer():
    context = request.get_json()
    classes_lecturer = ClassesLecturer.create_from_dto(context)
    classes_lecturer_controller.create(classes_lecturer)
    return make_response(jsonify(classes_lecturer.put_into_dto()), HTTPStatus.OK)


@classes_lecturers.put('/<int:classes_lecturers_id>')
def update_classes_lecturer(classes_lecturers_id):
    context = request.get_json()
    classes_lecturer = ClassesLecturer.create_from_dto(context)
    classes_lecturer_controller.update(classes_lecturers_id, classes_lecturer)
    return make_response()


@classes_lecturers.get('/get_data')
def get_date():
    return make_response(jsonify(classes_lecturer_controller.get_all_relationship_data()), HTTPStatus.OK)