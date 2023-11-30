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
    return make_response(jsonify("Classes lecturer update"), HTTPStatus.OK)


@classes_lecturers.patch('/<int:classes_lecturers_id>')
def patch_classes_lecturer(classes_lecturers_id):
    context = request.get_json()
    classes_lecturer_controller.patch(classes_lecturers_id, context)
    return make_response(jsonify("Classes lecture update"), HTTPStatus.OK)


@classes_lecturers.delete('/<int:classes_lecturers_id>')
def delete_classes_lecturer(classes_lecturers_id):
    classes_lecturer_controller.delete(classes_lecturers_id)
    return make_response(jsonify("Update classes lecturer"), HTTPStatus.OK)



