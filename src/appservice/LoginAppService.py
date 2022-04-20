from src.repository.LoginRepository import LoginRepository
from src.utils.permissions import get_permissions

class LoginAppService():

    def login(login, senha):
        try:
            user = LoginRepository.login(login, senha)
            if (len(user) > 0):
                user = user[0]
                msg = 'User logged in successfully.'
                permissions = get_permissions(user['tp_TipoUsuario'])
                return {'user': user, 'permissions': permissions, 'message': msg}, 200
            else:
                msg = 'User not found.'
                permissions = []
                return {'user': user, 'permissions': permissions, 'message': msg}, 401
        except Exception as e:
            print(e)
        