from ..repository.KeypressRepository import KeypressRepository

class KeypressAppService():
    def keypress(key_to_press):
        try:
            keypress = KeypressRepository.keypress(key_to_press)
        except Exception as e:
            print(e)
        return {'data': keypress, 'message': 'Success pressing your key'}

    def hotkey(combination_to_press):
        try:
            hotkey = KeypressRepository.hotkey(combination_to_press)
        except Exception as e:
            print(e)
        return {'data': hotkey, 'message': 'Success pressing your hotkey'}