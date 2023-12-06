from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from src.controller import classes_controller
from src.domain.classes import Classes


classes = Blueprint("classes", __name__, url_prefix="/api/v1/classes")


@classes.get('/')
def get_all_classes():
    return make_response(jsonify(classes_controller.find_all()), HTTPStatus.OK)


@classes.get('/<int:classes_id>')
def get_class_by_id(classes_id):
    return make_response(jsonify(classes_controller.find_by_id(classes_id)), HTTPStatus.OK)


@classes.post('/')
def create_classe():
    context = request.get_json()
    classe = Classes.create_from_dto(context)
    classes_controller.create(classe)
    return make_response(jsonify(classe.put_into_dto()), HTTPStatus.OK)


@classes.put('/<int:classes_id>')
def update_classe(classes_id):
    context = request.get_json()
    classe = Classes.create_from_dto(context)
    classes_controller.update(classes_id, classe)
    return make_response(jsonify("Classe update"), HTTPStatus.OK)


@classes.patch('/<int:classes_id>')
def patch_classe(classes_id):
    context = request.get_json()
    classes_controller.patch(classes_id, context)
    return make_response(jsonify("Classe update"), HTTPStatus.OK)


@classes.delete('/<int:classes_id>')
def delete_classe(classes_id):
    classes_controller.delete(classes_id)
    return make_response(jsonify("Delete classe"), HTTPStatus.OK)


@classes.get('/get_feedback/<int:classes_id>')
def get_feedback(classes_id):
    return make_response(jsonify(classes_controller.get_feedback_for_class(classes_id)), HTTPStatus.OK)