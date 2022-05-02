from flask import Blueprint
from flask_jwt_extended import jwt_required
from src.utils.maps_utils import GoogleMaps

import json

class Routes():

    routes_controller = Blueprint('routes_controller', __name__, url_prefix='/routes')

    @routes_controller.route('/<id_coleta>', methods=['GET'])
    @jwt_required()
    def get_route(self, id_coleta):
        try:
            route = GoogleMaps.calculate_route(id_coleta)
            return json.dumps(route, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from user function.'}
            return json.dumps(msg), 500