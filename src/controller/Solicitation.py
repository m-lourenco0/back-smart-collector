from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from src.appservice.SolicitationAppService import SolicitationAppService

import json

class Solicitation():

    solicitation_controller = Blueprint('solicitation_controller', __name__, url_prefix='/solicitation')


    @solicitation_controller.route('/', methods=['GET'])
    @jwt_required()
    def get_solicitation():
        try:
            solicitations = SolicitationAppService.get_solicitation()
            return json.dumps(solicitations, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_solicitation function.'}
            return json.dumps(msg), 500

    @solicitation_controller.route('/list', methods=['GET'])
    @jwt_required()
    def get_solicitation_list():
        try:
            solicitations = SolicitationAppService.get_solicitation_list()
            return json.dumps(solicitations, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_solicitation_list function.'}
            return json.dumps(msg), 500

    @solicitation_controller.route('/<id>', methods=['GET'])
    @jwt_required()
    def get_solicitation_by_id(id):
        try:
            vehicle = SolicitationAppService.get_solicitation_by_id(id)
            return json.dumps(vehicle, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_solicitation_by_id function.'}
            return json.dumps(msg), 500

    @solicitation_controller.route('/', methods=['PUT'])
    @jwt_required()
    def update_solicitation():
        try:
            data = request.get_json()
            solicitation = SolicitationAppService.update_solicitation(data['id'], data)
            return json.dumps(solicitation, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from update_solicitation function.'}
            return json.dumps(msg), 500

    @solicitation_controller.route('/add', methods=['POST'])
    @jwt_required()
    def add_solicitation():
        try:
            data = request.get_json()
            solicitations = SolicitationAppService.add_solicitation(data)
            return json.dumps(solicitations, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from add_solicitation function.'}
            return json.dumps(msg), 500

    @solicitation_controller.route('/delete/<id>', methods=['DELETE'])
    @jwt_required()
    def delete_solicitation(id):
        try:
            solicitations = SolicitationAppService.delete_solicitation(id)
            return json.dumps(solicitations, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from delete_solicitation function.'}
            return json.dumps(msg), 500