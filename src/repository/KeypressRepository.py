import pyautogui

class KeypressRepository():
    def keypress(key_to_press):
        try:
            pyautogui.press(key_to_press)
            keypress = 'Pressed key ' + key_to_press
        except Exception as e:
            print(e)
        return keypress

    def hotkey(combination_to_press):
        try:
            keys = combination_to_press.split(',')
            count = len(keys)
            if count == 2:
                pyautogui.hotkey(keys[0], keys[1])
            elif count == 3:
                pyautogui.hotkey(keys[0], keys[1], keys[2])

            hotkey = 'Pressed hotkey ' + combination_to_press
        except Exception as e:
            print(e)
        return hotkey