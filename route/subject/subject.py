from http import HTTPStatus

from flask import Blueprint, make_response, jsonify, request
from src.controller import subject_controller
from src.domain.subject import Subject

subjects = Blueprint('subject', __name__, url_prefix="/api/v1/subjects")


@subjects.get('/')
def get_all_subject():
    return make_response(subject_controller.find_all(), HTTPStatus.OK)


@subjects.get('/<int:subject_id>')
def get_subject_by_id(subject_id):
    return make_response(subject_controller.find_by_id(subject_id), HTTPStatus.OK)


@subjects.post('/')
def create_subject():
    context = request.get_json()
    subject = Subject.create_from_dto(context)
    subject_controller.create(subject)
    return make_response(jsonify(subject.put_into_dto()), HTTPStatus.OK)


@subjects.put('/<int:subject_id>')
def update_subject(subject_id):
    context = request.get_json()
    subject = Subject.create_from_dto(context)
    subject_controller.update(subject_id, subject)
    return make_response(jsonify('Subject update'), HTTPStatus.OK)


@subjects.patch('/<int:subject_id>')
def patch_subject(subject_id):
    context = request.get_json()
    subject_controller.patch(subject_id, context)
    return make_response(jsonify('Subject update'), HTTPStatus.OK)


@subjects.delete('/<int:subject_id>')
def delete_subject(subject_id):
    subject_controller.delete(subject_id)
    return make_response(jsonify('Subject delete'), HTTPStatus.OK)
