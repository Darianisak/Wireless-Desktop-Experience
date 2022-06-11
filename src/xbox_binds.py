class XboxBinds:
    """
    class.functions works in tandem with a config/bind file to perform system
    actions, when supplied with a given input action
    """

    current_profile = {
        "buttons": {
            "a_pressed": "",
            "a_released": "",
            "b_pressed": "",
            "b_released": "",
            "x_pressed": "",
            "x_released": "",
            "y_pressed": "",
            "y_released": "",
            "start_pressed": "",
            "start_released": "",
            "back_pressed": "",
            "back_released": ""
        },
        "shoulders": {
            "left_pressed": "",
            "left_released": "",
            "right_pressed": "",
            "right_released": ""
        },
        "sticks": {
            "left_dead": 0,
            "right_dead": 0,
            "left_move": "",
            "right_move": ""
        },
        "dpad": {
            "up_pressed": "",
            "up_released": "",
            "down_pressed": "",
            "down_released": "",
            "left_pressed": "",
            "left_released": "",
            "right_pressed": "",
            "right_released": ""
        },
        "triggers": {
            "left_dead": 0,
            "right_dead": 0,
            "left_press": "",
            "right_press": "",
        },
        "motors": {
            "left_strength": 0,
            "right_strength": 0
        }
    }

    def read_binds(self, path: str):

        """
        Read_binds, when given a conf file, will specify the system actions
        performed for any given button press, etc.

        :param path: Conf file
        :return: None
        """
        with open(path) as conf:
            file = conf.readlines()
        current_set = ""

        for line in range(len(file)):
            if file[line][0] == "#":
                #   Ignores comment lines
                continue
            elif file[line][0] == "!":
                #   Gets a super key for a given trigger/button group
                current_set = file[line].split()[1]
                if current_set not in self.current_profile.keys():
                    raise KeyError("Malformed conf file @", current_set,
                                   "! Check that all super key names are correct!")
            elif len(file[line].split()) > 1:
                #   Gets a specific button or trigger, as well as its action
                trigger = file[line].split()[0]
                action = file[line].split()[1]
                if trigger not in self.current_profile[current_set].keys():
                    raise KeyError("Malformed conf file @", current_set, ":",
                                   trigger, "! Check that all sub keys are correct!")
                self.current_profile[current_set][trigger] = action
