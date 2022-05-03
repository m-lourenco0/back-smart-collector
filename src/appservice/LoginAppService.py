from flask import jsonify
from src.repository.LoginRepository import LoginRepository
from src.utils.permissions import get_permissions
from flask_jwt_extended import create_access_token, set_access_cookies, create_refresh_token, set_refresh_cookies
import settings

class LoginAppService():

    def login(login, senha):
        try:
            user = LoginRepository.login(login, senha)
            
            if (len(user) > 0):
                user = user[0]
                permissions = get_permissions(user['tp_TipoUsuario'])
                access_token = create_access_token(identity=user)
                refresh_token = create_refresh_token(identity=user)
                response = jsonify({'token': access_token, 'permissions': permissions, 'refresh_token': refresh_token, 'message': 'User logged in successfully.'})
            else:
                response = jsonify({'message': 'Invalid username or password'})
                response.status_code = 401
            
            return response
        except Exception as e:
            print(f'Exception error from login function. Error: {e}', flush=True)
        