from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from src.appservice.VehicleAppService import VehicleAppService

import json


class Vehicle():

    vehicle_controller = Blueprint('vehicle_controller', __name__, url_prefix='/vehicle')

    @vehicle_controller.route('/', methods=['GET'])
    @jwt_required()
    def get_vehicle():
        try:
            vehicles = VehicleAppService.get_vehicle()
            return json.dumps(vehicles, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_vehicles function.'}
            return json.dumps(msg), 500

    @vehicle_controller.route('/available', methods=['GET'])
    @jwt_required()
    def get_available_vehicle():
        try:
            vehicles = VehicleAppService.get_available_vehicle()
            return json.dumps(vehicles, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_available_vehicle function.'}
            return json.dumps(msg), 500

    @vehicle_controller.route('/<id>', methods=['GET'])
    @jwt_required()
    def get_vehicle_by_id(id):
        try:
            vehicle = VehicleAppService.get_vehicle_by_id(id)
            return json.dumps(vehicle, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_vehicle_by_id function.'}
            return json.dumps(msg), 500

    @vehicle_controller.route('/<id>', methods=['PUT'])
    @jwt_required()
    def update_vehicle(id):
        try:
            data = request.get_json()
            vehicle = VehicleAppService.update_vehicle(data['id'], data)
            return json.dumps(vehicle, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from update_vehicle function.'}
            return json.dumps(msg), 500

    @vehicle_controller.route('/add', methods=['POST'])
    @jwt_required()
    def add_vehicle():
        try:
            data = request.get_json()
            vehicles = VehicleAppService.add_vehicle(data)
            return json.dumps(vehicles, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from add_vehicles function.'}
            return json.dumps(msg), 500

    @vehicle_controller.route('/delete/<id>', methods=['DELETE'])
    @jwt_required()
    def delete_vehicle(id):
        try:
            vehicles = VehicleAppService.delete_vehicle(id)
            return json.dumps(vehicles, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from delete_vehicles function.'}
            return json.dumps(msg), 500