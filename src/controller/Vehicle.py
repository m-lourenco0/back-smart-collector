from flask import request
from flask_classy import FlaskView, route
import json
from src.appservice.VehicleAppService import VehicleAppService


class Vehicle(FlaskView):

    @route('/', methods=['GET'])
    def get_vehicle(self):
        try:
            vehicles = VehicleAppService.get_vehicle()
            return json.dumps(vehicles, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_vehicles function.'}
            return json.dumps(msg), 500

    @route('/<id>', methods=['GET'])
    def get_vehicle_by_id(self, id):
        try:
            vehicle = VehicleAppService.get_vehicle_by_id(id)
            return json.dumps(vehicle, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from get_vehicle_by_id function.'}
            return json.dumps(msg), 500

    @route('/<id>', methods=['PUT'])
    def update_vehicle(self, id):
        try:
            data = request.get_json()
            vehicle = VehicleAppService.update_vehicle(data['id'], data)
            return json.dumps(vehicle, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from update_vehicle function.'}
            return json.dumps(msg), 500

    @route('/add', methods=['POST'])
    def add_vehicle(self):
        try:
            data = request.get_json()
            vehicles = VehicleAppService.add_vehicle(data)
            return json.dumps(vehicles, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from add_vehicles function.'}
            return json.dumps(msg), 500

    @route('/delete/<id>', methods=['DELETE'])
    def delete_vehicle(self, id):
        try:
            vehicles = VehicleAppService.delete_vehicle(id)
            return json.dumps(vehicles, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from delete_vehicles function.'}
            return json.dumps(msg), 500