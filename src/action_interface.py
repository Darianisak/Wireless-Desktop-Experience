import mouse as ms
import keyboard as kb

#   TODO ~ Create documentation
class ActionInterface:

    current_binds = {}

    def __init__(self, bind_profile: {}):
        self.current_binds = bind_profile
        print(self.current_binds)

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
        print("")

    def reformat_macro(self, macro: []):
        """
        reformat_macro is a utility function that allows plain english phrases
        in conf.txt to be parsed into the correct format for keyboard.lib

        :param macro: The 'action' for a specific button, as defined in conf.txt
        :return: A formatted string
        """
        if len(macro) > 1:
            #   Given an action that involves spaces, e.g., 'test string'
            #   we parse each individual word to add '+'s, and then return the
            #   output of concatenation via '+space+'
            tmp = []
            for arg in macro:
                tmp.append(arg.replace("", "+")[1:-1])
            return "+space+".join(tmp)
        else:
            #   Format single argument actions
            return macro[0].replace("", "+")[1:-1]

