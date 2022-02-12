#   xbox_model is a class that represents an xbox controller object, through
#   which more complicated expressions can be communicated by the end user.
#   More complicated expressions include actions that are dependant on another
#   buttons being depressed concurrently, for example.

#   <---    XBOX CONTROLLER MODEL FIELDS    --->

#   Binary Control Values

button_depressed_a = False
button_depressed_b = False
button_depressed_x = False
button_depressed_y = False


#   is_button_depressed is a boolean getter method for the button group.
#   None is returned in the case of programmer error, where an inappropriate
#   button call has been made, i.e. a button of K.
def is_button_depressed(button):

    match button:
        case "A":
            return button_depressed_a
        case "B":
            return button_depressed_a
        case "X":
            return button_depressed_a
        case "Y":
            return button_depressed_a
        case _:
            return None


#   set_button_depressed is a boolean setter method for the button group.
#   None is returned in the case of programmer error, where an inappropriate
#   button call has been made, i.e. a button of K.
def set_button_depressed(button, status):

    global button_depressed_a, button_depressed_b, button_depressed_y
    global button_depressed_x

    match button:
        case "A":
            button_depressed_a = status
        case "B":
            button_depressed_b = status
        case "X":
            button_depressed_x = status
        case "Y":
            button_depressed_y = status
        case _:
            return None


shoulder_depressed_left = False
shoulder_depressed_right = False


#   is_shoulder_depressed is a boolean getter method for the shoulder group.
#   None is returned in the case of programmer error, where an inappropriate
#   shoulder call has been made, i.e. a shoulder of middle.
def is_shoulder_depressed(shoulder):

    match shoulder:
        case "LEFT":
            return shoulder_depressed_left
        case "RIGHT":
            return shoulder_depressed_right
        case _:
            return None


#   is_shoulder_depressed is a boolean setter method for the shoulder group.
#   None is returned in the case of programmer error, where an inappropriate
#   shoulder call has been made, i.e. a shoulder of middle.
def set_shoulder_depressed(shoulder, status):

    global shoulder_depressed_right, shoulder_depressed_left

    match shoulder:
        case "LEFT":
            shoulder_depressed_left = status
        case "RIGHT":
            shoulder_depressed_right = status
        case _:
            return None


dpad_depressed_left = False
dpad_depressed_right = False
dpad_depressed_top = False
dpad_depressed_bottom = False


#   is_dpad_depressed is a boolean getter method for the dpad group.
#   None is returned in the case of programmer error, where an inappropriate
#   dpad call has been made, i.e. a dpad of middle.
def is_dpad_depressed(dpad):

    match dpad:
        case "LEFT":
            return dpad_depressed_left
        case "RIGHT":
            return dpad_depressed_right
        case "TOP":
            return dpad_depressed_top
        case "BOTTOM":
            return dpad_depressed_bottom
        case _:
            return None


#   is_dpad_depressed is a boolean setter method for the dpad group.
#   None is returned in the case of programmer error, where an inappropriate
#   dpad call has been made, i.e. a dpad of middle.
def set_dpad_depressed(dpad, status):

    global dpad_depressed_left, dpad_depressed_right, dpad_depressed_top
    global dpad_depressed_bottom

    match dpad:
        case "LEFT":
            dpad_depressed_left = status
        case "RIGHT":
            dpad_depressed_right = status
        case "TOP":
            dpad_depressed_top = status
        case "BOTTOM":
            dpad_depressed_bottom = status
        case _:
            return None


start_depressed = False
back_depressed = False


#   is_option_depressed is a boolean getter method for the option group.
#   None is returned in the case of programmer error, where an inappropriate
#   option call has been made, i.e. an option of escape.
def is_option_depressed(option):

    match option:
        case "START":
            return start_depressed
        case "BACK":
            return back_depressed
        case _:
            return None


#   is_option_depressed is a boolean setter method for the option group.
#   None is returned in the case of programmer error, where an inappropriate
#   option call has been made, i.e. an option of escape.
def set_option_depressed(option, status):

    global start_depressed, back_depressed

    match option:
        case "START":
            start_depressed = status
        case "BACK":
            back_depressed = status
        case _:
            return None


#   Analogue Control Values

print(is_button_depressed("a"))
