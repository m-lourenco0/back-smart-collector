from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from src.appservice.PersonAppService import PersonAppService

import json

class Person():

    person_controller = Blueprint('person_controller', __name__, url_prefix='/person')

    @person_controller.route('/', methods=['GET'])
    @jwt_required()
    def get_person():
        try:
            person = PersonAppService.get_person()
            response = jsonify(person)
            return response
        except Exception as e:
            msg = {'msg': 'Exception error from get_person function.'}
            return json.dumps(msg), 500

    @person_controller.route('/<id>', methods=['GET'])
    @jwt_required()
    def get_person_by_id(id):
        try:
            person = PersonAppService.get_person_by_id(id)
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_person_by_id function.'}
            return json.dumps(msg), 500

    @person_controller.route('/', methods=['PUT'])
    @jwt_required()
    def update_person():
        try:
            data = request.get_json()
            person = PersonAppService.update_person(data['id'], data)
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from update_person function.'}
            return json.dumps(msg), 500

    @person_controller.route('/add', methods=['POST'])
    @jwt_required()
    def add_person():
        try:
            data = request.get_json()
            person = PersonAppService.add_person(data)
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from add_person function.'}
            return json.dumps(msg), 500

    @person_controller.route('/delete/<id>', methods=['DELETE'])
    @jwt_required()
    def delete_person(id):
        try:
            person = PersonAppService.delete_person(id)
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from delete_person function.'}
            return json.dumps(msg), 500