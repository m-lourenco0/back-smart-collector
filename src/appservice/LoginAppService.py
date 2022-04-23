from os import access
from src.repository.LoginRepository import LoginRepository
from src.utils.permissions import get_permissions
from flask_jwt_extended import create_access_token

class LoginAppService():

    def login(login, senha):
        try:
            user = LoginRepository.login(login, senha)
            
            if (len(user) > 0):
                user = user[0]
                msg = 'User logged in successfully.'
                permissions = get_permissions(user['tp_TipoUsuario'])
                access_token = create_access_token(identity=user)
                return {'token': access_token, 'permissions': permissions, 'message': msg}, 200
            else:
                msg = 'User not found.'
                permissions = []
                return {'message': msg}, 401
        except Exception as e:
            print(e)
        