from flask_classy import FlaskView, route
import json
from src.appservice.KeypressAppService import KeypressAppService


class Keypress(FlaskView):

    @route('/<key_to_press>')
    def keypress(self, key_to_press):
        try:
            keypress = KeypressAppService.keypress(key_to_press)
            return json.dumps(keypress, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress.'}
            return json.dumps(msg), 500
    
    @route('hotkey/<combination_to_press>')
    def hotkey(self, combination_to_press):
        try:
            hotkey = KeypressAppService.hotkey(combination_to_press)
            return json.dumps(hotkey, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress > Hotkey'}
            return json.dumps(msg), 500