
class XboxFunctions:

    """
    class.functions works in tandem with a config/bind file to perform system
    actions, when supplied with a given input action
    """

    current_profile = {
        "buttons": {
            "A_Press": "",
            "A_Release": "",
            "B_Press": "",
            "B_Release": "",
            "X_Press": "",
            "X_Release": "",
            "Y_Press": "",
            "Y_Release": "",
            "Start_Press": "",
            "Start_Release": "",
            "Back_Press": "",
            "Back_Release": ""
        },
        "shoulders": {
            "L_Press": "",
            "L_Release": "",
            "R_Press": "",
            "R_Release": ""
        },
        "sticks": {
            "L_Dead": 0,
            "R_Dead": 0,
            "L": "",
            "R": ""
        },
        "dpad": {
            "U_Press": "",
            "U_Release": "",
            "D_Press": "",
            "D_Release": "",
            "L_Press": "",
            "L_Release": "",
            "R_Press": "",
            "R_Release": ""
        },
        "triggers": {
            "L_Dead": 0,
            "R_Dead": 0,
            "L_Press": "",
            "R_Press": "",
        },
        "motors": {
            "L": 0,
            "R": 0
        }
    }

    def read_binds(self, path: str):
        print(path)
        file = []

        with open(path) as conf:
            file = conf.readlines()

        print("len", len(file))

