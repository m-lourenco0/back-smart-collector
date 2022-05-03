from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, unset_jwt_cookies, jwt_required, set_access_cookies, get_jwt
from src.appservice.LoginAppService import LoginAppService
from src.utils.permissions import get_permissions

import json
import settings

class Login():

    login_controller = Blueprint('login_controller', __name__, url_prefix='/login')

    @login_controller.route('/', methods=['POST'])
    def login():
        try:
            data = request.get_json()
            user = LoginAppService.login(data['user'], data['pass'])
            return user
        except Exception as e:
            msg = {'msg': 'Exception error from user function.'}
            return json.dumps(msg), 500

    @login_controller.route('/refresh', methods=['GET'])
    @jwt_required(refresh=True, locations=['cookies'])
    def refresh_token():
        current_user = get_jwt()
        permissions = get_permissions(current_user['sub']['tp_TipoUsuario'])
        access_token = create_access_token(identity=get_jwt_identity(), fresh=False)
        response = jsonify({'msg': 'Token refreshed.', 'token': access_token, 'permissions': permissions})
        set_access_cookies(response, access_token, domain=settings.COOKIE_DOMAIN)
        return response

    @login_controller.route('/logout', methods=['POST'])
    def logout():
        try:
            response = jsonify({'msg': 'User logged out successfully.'})
            unset_jwt_cookies(response)
            return response
        except Exception as e:
            msg = {'msg': 'Exception error from user function.'}
            return json.dumps(msg), 500