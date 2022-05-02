from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from src.appservice.ServiceAppService import ServiceAppService

import json

class Service():

    service_controller = Blueprint('service_controller', __name__, url_prefix='/service')

    @service_controller.route('/', methods=['GET'])
    @jwt_required()
    def get_service():
        try:
            services = ServiceAppService.get_service()
            return json.dumps(services, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_service function.'}
            return json.dumps(msg), 500

    @service_controller.route('/<id>', methods=['GET'])
    @jwt_required()
    def get_service_by_id(id):
        try:
            vehicle = ServiceAppService.get_service_by_id(id)
            return json.dumps(vehicle, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_service_by_id function.'}
            return json.dumps(msg), 500

    @service_controller.route('/', methods=['PUT'])
    @jwt_required()
    def update_service():
        try:
            data = request.get_json()
            service = ServiceAppService.update_service(data['id'], data)
            return json.dumps(service, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from update_service function.'}
            return json.dumps(msg), 500

    @service_controller.route('/add', methods=['POST'])
    @jwt_required()
    def add_service():
        try:
            data = request.get_json()
            services = ServiceAppService.add_service(data)
            return json.dumps(services, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from add_service function.'}
            return json.dumps(msg), 500

    @service_controller.route('/delete/<id>', methods=['DELETE'])
    @jwt_required()
    def delete_service(id):
        try:
            services = ServiceAppService.delete_service(id)
            return json.dumps(services, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from delete_service function.'}
            return json.dumps(msg), 500