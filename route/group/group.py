from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from src.controller import group_controller
from src.domain.group import Group


groups = Blueprint('group', __name__, url_prefix="/api/v1/groups")


@groups.get('/')
def get_all_group():
    return make_response(jsonify(group_controller.find_all()), HTTPStatus.OK)


@groups.get('/<int:group_id>')
def get_group_by_id(group_id):
    return make_response(jsonify(group_controller.find_by_id(group_id)), HTTPStatus.OK)


@groups.post('/')
def create_program():
    context = request.get_json()
    group = Group.create_from_dto(context)
    group_controller.create(group)
    return make_response(jsonify(group.put_into_dto()), HTTPStatus.OK)


@groups.put('/<int:group_id>')
def update_program(group_id):
    context = request.get_json()
    group = Group.create_from_dto(context)
    group_controller.update(group_id, group)
    return make_response(jsonify("Group update", HTTPStatus.OK))


@groups.patch('/<int:group_id>')
def patch_program(group_id):
    context = request.get_json()
    group_controller.patch(group_id, context)
    return make_response("Group update", HTTPStatus.OK)


@groups.delete('/<int:group_id>')
def delete_group(group_id):
    group_controller.delete(group_id)
    make_response(jsonify("Group delete"), HTTPStatus.OK)