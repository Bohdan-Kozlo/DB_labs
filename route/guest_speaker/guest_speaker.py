from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request
from src.controller import guest_speaker_controller
from src.domain.guest_speaker import GuestSpeaker

guest_speakers = Blueprint("guest_speaker", __name__, url_prefix="/api/v1/guest_speakers")


@guest_speakers.get('/')
def get_all_speakers():
    return make_response(jsonify(guest_speaker_controller.find_all()), HTTPStatus.OK)


@guest_speakers.get('/<int:speaker_id>')
def get_speaker_by_id(speaker_id):
    return make_response(jsonify(guest_speaker_controller.find_by_id(speaker_id)), HTTPStatus.OK)


@guest_speakers.post('/')
def create_speaker():
    context = request.get_json()
    guest_speaker = GuestSpeaker.crate_from_dto(context)
    guest_speaker_controller.create(guest_speaker)
    return make_response(jsonify(guest_speaker.put_into_dto()), HTTPStatus.OK)


@guest_speakers.put('/<int:speaker_id>')
def update_speaker(speaker_id):
    context = request.get_json()
    guest_speaker = GuestSpeaker.create_from_dto(context)
    guest_speaker_controller.update(speaker_id, guest_speaker)
    return make_response(jsonify("Speaker update"), HTTPStatus.OK)


@guest_speakers.patch('/<int:speaker_id>')
def patch_speaker(speaker_id):
    context = request.get_json()
    guest_speaker_controller.patch(speaker_id, context)
    return make_response(jsonify("Update speaker"), HTTPStatus.OK)


@guest_speakers.delete('/<int:speaker_id>')
def delete_speaker(speaker_id):
    guest_speaker_controller.delete(speaker_id)
    return make_response(jsonify("Delete speaker"), HTTPStatus.OK)
