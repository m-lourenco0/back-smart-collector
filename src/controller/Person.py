from flask import request
from flask_classy import FlaskView, route
import json
from src.appservice.PersonAppService import PersonAppService


class Person(FlaskView):

    @route('/', methods=['GET'])
    def get_person(self):
        try:
            person = PersonAppService.get_person()
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_person function.'}
            return json.dumps(msg), 500

    @route('/<id>', methods=['GET'])
    def get_person_by_id(self, id):
        try:
            person = PersonAppService.get_person_by_id(id)
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_person_by_id function.'}
            return json.dumps(msg), 500

    @route('/', methods=['PUT'])
    def update_person(self):
        try:
            data = request.get_json()
            person = PersonAppService.update_person(data['id'], data)
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from update_person function.'}
            return json.dumps(msg), 500

    @route('/add', methods=['POST'])
    def add_person(self):
        try:
            data = request.get_json()
            person = PersonAppService.add_person(data)
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from add_person function.'}
            return json.dumps(msg), 500

    @route('/delete/<id>', methods=['POST'])
    def delete_person(self, id):
        try:
            person = PersonAppService.delete_person(id)
            return json.dumps(person, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from delete_person function.'}
            return json.dumps(msg), 500