import mouse as ms
import keyboard as kb
from ctypes import windll as os


#   TODO ~ Create documentation
class ActionInterface:

    current_binds = {}
    modifiers = ["ctrl", "shift", "esc", "enter", "alt", "windows"]
    screensize = {
        "Width": 0,
        "Height": 0
    }

    def __init__(self, bind_profile: {}):
        self.current_binds = bind_profile
        self.screensize["Width"] = os.user32.GetSystemMetrics(78)
        self.screensize["Height"] = os.user32.GetSystemMetrics(79)

    def do_button_press(self, arg):
        if arg[0] in ["left", "right", "middle"]:
            #   Branch handles mouse bound buttons
            ms.click(arg[0])
        else:
            #   Branch handles 'macro-ing', e.g., entering an entire web
            #   predefined web address
            kb.press_and_release(self.reformat_macro(arg))

    def do_trigger_press(self):
        print("")

    def do_stick_movement(self):
        ms.get_position()
        print("")

    def reformat_macro(self, macro: []):
        """
        reformat_macro is a utility function that allows plain english phrases
        in conf.txt to be parsed into the correct format for keyboard.lib

        :param macro: The 'action' for a specific button, as defined in conf.txt
        :return: A formatted string
        """
        if len(macro) > 1:
            #   Formats multi argument actions for use by keyboard.lib
            tmp = []
            for arg in macro:
                if arg in self.modifiers:
                    tmp.append(arg)
                else:
                    tmp.append(arg.replace("", "+")[1:-1])
            return "+space+".join(tmp)
        else:
            if macro[0] in self.modifiers:
                return macro[0]
            else:
                return macro[0].replace("", "+")[1:-1]

