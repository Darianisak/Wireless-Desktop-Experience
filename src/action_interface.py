#   TODO ~ Create documentation
class ActionInterface:

    current_binds = {}

    def __init__(self, bind_profile: {}):
        self.current_binds = bind_profile
        print(self.current_binds)

    def do_button_press(self):
        print("")

    def do_trigger_press(self):
        print("")

    def do_stick_movement(self):
        print("")