from flask_classy import FlaskView, route
import json
from src.appservice.OSAppService import OSAppService


class OS(FlaskView):

    @route('/<func>')
    def OS(self, func):
        try:
            OS = OSAppService.OS(func)
            return json.dumps(OS, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from OS function.'}
            return json.dumps(msg), 500