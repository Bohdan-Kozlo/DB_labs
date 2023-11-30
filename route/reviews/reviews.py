from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from src.controller import reviews_controller
from src.domain.reviews import Reviews

reviews = Blueprint("reviews", __name__, url_prefix="/api/v1/reviews")


@reviews.get('/')
def get_all_reviews():
    return make_response(jsonify(reviews_controller.find_all()), HTTPStatus.OK)


@reviews.get('/<int:review_id>')
def get_review_by_id(review_id):
    return make_response(jsonify(reviews_controller.find_by_id(review_id)), HTTPStatus.OK)


@reviews.post('/')
def create_review():
    context = request.get_json()
    review = Reviews.create_from_dto(context)
    reviews_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.OK)


@reviews.put('/<int:review_id>')
def update_review(review_id):
    context = request.get_json()
    review = Reviews.create_from_dto(context)
    reviews_controller.update(review_id, review)
    return make_response(jsonify("Review updated"), HTTPStatus.OK)


@reviews.patch('/<int:review_id>')
def patch_review(review_id):
    context = request.get_json()
    reviews_controller.patch(review_id, context)
    return make_response(jsonify("Update review"), HTTPStatus.OK)


@reviews.delete('/<int:review_id>')
def delete_review(review_id):
    reviews_controller.delete(review_id)
    return make_response(jsonify("Delete review"), HTTPStatus.OK)
