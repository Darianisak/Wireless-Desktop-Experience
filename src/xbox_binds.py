class XboxBinds:
    """
    class.functions works in tandem with a config/bind file to perform system
    actions, when supplied with a given input action
    """

    current_profile = {
        "buttons": {
            "A": 0,
            "Y": 0,
            "B": 0,
            "X": 0,
            "START": 0,
            "BACK": 0,
            "RIGHT_SHOULDER": 0,
            "LEFT_SHOULDER": 0,
            "RIGHT_THUMB": 0,
            "LEFT_THUMB": 0,
            "DPAD_DOWN": 0,
            "DPAD_UP": 0,
            "DPAD_RIGHT": 0,
            "DPAD_LEFT": 0
        },

        "sticks": {
            "left_dead": 0,
            "right_dead": 0,
            "left_move": "",
            "right_move": ""
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
