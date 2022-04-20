from flask import request
from flask_classy import FlaskView, route
import json
from src.appservice.LoginAppService import LoginAppService


class Login(FlaskView):

    @route('/', methods=['POST'])
    def login(self):
        try:
            data = request.get_json()
            user = LoginAppService.login(data['user'], data['pass'])
            return json.dumps(user[0], default=str), user[1]
        except Exception as e:
            msg = {'msg': 'Exception error from user function.'}
            return json.dumps(msg), 500