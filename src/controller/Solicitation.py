from flask import request
from flask_classy import FlaskView, route
import json
from src.appservice.SolicitationAppService import SolicitationAppService


class Solicitation(FlaskView):

    @route('/', methods=['GET'])
    def get_solicitation(self):
        try:
            solicitations = SolicitationAppService.get_solicitation()
            return json.dumps(solicitations, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_solicitation function.'}
            return json.dumps(msg), 500

    @route('/list', methods=['GET'])
    def get_solicitation_list(self):
        try:
            solicitations = SolicitationAppService.get_solicitation_list()
            return json.dumps(solicitations, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_solicitation_list function.'}
            return json.dumps(msg), 500

    @route('/<id>', methods=['GET'])
    def get_solicitation_by_id(self, id):
        try:
            vehicle = SolicitationAppService.get_solicitation_by_id(id)
            return json.dumps(vehicle, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_solicitation_by_id function.'}
            return json.dumps(msg), 500

    @route('/', methods=['PUT'])
    def update_solicitation(self):
        try:
            data = request.get_json()
            solicitation = SolicitationAppService.update_solicitation(data['id'], data)
            return json.dumps(solicitation, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from update_solicitation function.'}
            return json.dumps(msg), 500

    @route('/add', methods=['POST'])
    def add_solicitation(self):
        try:
            data = request.get_json()
            solicitations = SolicitationAppService.add_solicitation(data)
            return json.dumps(solicitations, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from add_solicitation function.'}
            return json.dumps(msg), 500

    @route('/delete/<id>', methods=['DELETE'])
    def delete_solicitation(self, id):
        try:
            solicitations = SolicitationAppService.delete_solicitation(id)
            return json.dumps(solicitations, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from delete_solicitation function.'}
            return json.dumps(msg), 500