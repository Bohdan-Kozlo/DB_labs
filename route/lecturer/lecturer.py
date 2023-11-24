from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from src.controller import lecturer_controller
from src.domain.lecturer import Lecturer


lecturers = Blueprint("lecturer", __name__, url_prefix="/api/v1/lecturer")


@lecturers.get('/')
def get_all_lecturer():
    return make_response(jsonify(lecturer_controller.find_all()), HTTPStatus.OK)


@lecturers.get('/<int:lecturer_id>')
def get_lecturer_by_id(lecturer_id):
    return make_response(jsonify(lecturer_controller.find_by_id(lecturer_id)), HTTPStatus.OK)


@lecturers.post('/')
def create_lecturer():
    context = request.get_json()
    lecturer = Lecturer.crate_from_dto(context)
    lecturer_controller.create(lecturer)
    return make_response(jsonify(lecturer.put_into_dto()), HTTPStatus.OK)


@lecturers.put('/<int:lecturer_id>')
def update_lecturer(lecturer_id):
    context = request.get_json()
    lecturer = Lecturer.put_into_dto(context)
    lecturer_controller.update(lecturer_id, lecturer)
    return make_response(jsonify("Lecturer update"), HTTPStatus.OK)


@lecturers.patch('/<int:lecturer_id>')
def patch_lecturer(lecturer_id):
    context = request.get_json()
    lecturer_controller.patch(lecturer_id, context)
    return make_response(jsonify("Update lecturer"), HTTPStatus.OK)


@lecturers.delete('<int:lecturer_id>')
def delete_lecturer(lecturer_id):
    lecturer_controller.delete(lecturer_id)
    return make_response(jsonify("Delete lecturer"), HTTPStatus.OK)
