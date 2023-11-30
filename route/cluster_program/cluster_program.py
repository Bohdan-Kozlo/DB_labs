from http import HTTPStatus

from flask import Blueprint, make_response, jsonify, request
from src.controller import cluster_program_controller
from src.domain.cluster_program import ClusterProgram

clusters_programs = Blueprint("cluster_program", __name__, url_prefix="/api/v1/clusters_programs")


@clusters_programs.get('/')
def get_all_program():
    return make_response(jsonify(cluster_program_controller.find_all()), HTTPStatus.OK)


@clusters_programs.get('/<int:cluster_id>')
def get_cluster_by_id(cluster_id):
    return make_response(jsonify(cluster_program_controller.find_by_id(cluster_id)), HTTPStatus.OK)


@clusters_programs.post('/')
def create_program():
    context = request.get_json()
    cluster_program = ClusterProgram.create_from_dto(context)
    cluster_program_controller.create(cluster_program)
    return make_response(jsonify(cluster_program.put_into_dto()), HTTPStatus.OK)


@clusters_programs.put('/<int:cluster_id>')
def update_program(cluster_id):
    context = request.get_json()
    cluster_program = ClusterProgram.create_from_dto(context)
    cluster_program_controller.update(cluster_id, cluster_program)
    return make_response(jsonify("Cluster update", HTTPStatus.OK))


@clusters_programs.patch('/<int:cluster_id>')
def patch_program(cluster_id):
    context = request.get_json()
    cluster_program_controller.patch(cluster_id, context)
    return make_response("Cluster update", HTTPStatus.OK)


@clusters_programs.delete('/<int:cluster_id>')
def delete_program(cluster_id):
    cluster_program_controller.delete(cluster_id)
    return make_response("Cluster delete", HTTPStatus.OK)


@clusters_programs.get('/get_subject/<int:cluster_program_id>')
def get_subject(cluster_program_id):
    return make_response(jsonify(cluster_program_controller.get_subjects_in_cluster_program(cluster_program_id)))


