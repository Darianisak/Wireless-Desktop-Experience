#   xbox_model represents an xbox controller object, through
#   which more complicated expressions can be communicated by the end user.
#   More complicated expressions include actions that are dependant on another
#   buttons being offset concurrently, for example.

#   <---    XBOX CONTROLLER MODEL FIELDS    --->

xbox_model = {
    #   Primary Buttons
    "pressed_button_a": False,
    "pressed_button_b": False,
    "pressed_button_x": False,
    "pressed_button_y": False,

    #   Shoulders
    "pressed_shoulder_left": False,
    "pressed_shoulder_right": False,

    #   Thumb Clicks
    "pressed_right_thumb": False,
    "pressed_left_thumb": False,

    #   Options
    "pressed_start": False,
    "pressed_back": False,

    #   DPAD
    "pressed_dpad_up": False,
    "pressed_dpad_right": False,
    "pressed_dpad_down": False,
    "pressed_dpad_left": False,

    #   Triggers - max 1.0, min 0.0
    "trigger_left_offset": False,
    "trigger_left_offset_amount": 0.00,
    "trigger_right_offset": False,
    "trigger_right_offset_amount": 0.00,

    #   Sticks - max 1.0, min -1.0
    "stick_left_x": 0.00,
    "stick_left_y": 0.00,
    "stick_right_x": 0.00,
    "stick_right_y": 0.00
}


#   get_button_status is a boolean getter method for the button group.
#
#   button: Type String
#   return: True - button is pressed. False - button is not pressed
#   error : ValueError when button is invalid
def get_button_status(button):

    global xbox_model

    match button:
        case "A":
            return xbox_model["pressed_button_a"]
        case "B":
            return xbox_model["pressed_button_b"]
        case "X":
            return xbox_model["pressed_button_x"]
        case "Y":
            return xbox_model["pressed_button_y"]
        case "LEFT_SHOULDER":
            return xbox_model["pressed_shoulder_left"]
        case "RIGHT_SHOULDER":
            return xbox_model["pressed_shoulder_right"]
        case "LEFT_THUMB":
            return xbox_model["pressed_left_thumb"]
        case "RIGHT_THUMB":
            return xbox_model["pressed_right_thumb"]
        case "START":
            return xbox_model["pressed_start"]
        case "BACK":
            return xbox_model["pressed_back"]
        case "DPAD_UP":
            return xbox_model["pressed_dpad_up"]
        case "DPAD_DOWN":
            return xbox_model["pressed_dpad_down"]
        case "DPAD_LEFT":
            return xbox_model["pressed_dpad_left"]
        case "DPAD_RIGHT":
            return xbox_model["pressed_dpad_right"]
        case _:
            raise ValueError("Raised by Xbox_model.get_button_status(button)"
                             "\n'button' was " + str(button))


#   set_button_offset is a boolean setter method for the button group.
#
#   button: Type String
#   status: Type bool
#   return: None
#   error : TypeError when status is not of type bool
#   error : ValueError when button is invalid
def set_button_status(button, status):

    global xbox_model

    if isinstance(status, bool):

        match button:
            case "A":
                xbox_model["pressed_button_a"] = status
            case "B":
                xbox_model["pressed_button_b"] = status
            case "X":
                xbox_model["pressed_button_x"] = status
            case "Y":
                xbox_model["pressed_button_y"] = status
            case "LEFT_SHOULDER":
                xbox_model["pressed_shoulder_left"] = status
            case "RIGHT_SHOULDER":
                xbox_model["pressed_shoulder_right"] = status
            case "LEFT_THUMB":
                xbox_model["pressed_left_thumb"] = status
            case "RIGHT_THUMB":
                xbox_model["pressed_right_thumb"] = status
            case "START":
                xbox_model["pressed_start"] = status
            case "BACK":
                xbox_model["pressed_back"] = status
            case "DPAD_UP":
                xbox_model["pressed_dpad_up"] = status
            case "DPAD_DOWN":
                xbox_model["pressed_dpad_down"] = status
            case "DPAD_LEFT":
                xbox_model["pressed_dpad_left"] = status
            case "DPAD_RIGHT":
                xbox_model["pressed_dpad_right"] = status
            case _:
                return ValueError("Raised by Xbox_model.set_button_status(button, status)"
                                  "\n'button' was " + str(button))
    else:
        raise TypeError("Raised by Xbox_model.set_button_status(button, status)"
                        "\n'status' must be of type bool, was " + str(type(status)))


#   is_trigger_offset is a boolean getter method for the trigger group.
#
#   trigger: Type String
#   return : True - trigger is pressed. False - trigger is not pressed
#   error  : ValueError is raised when trigger is invalid
def is_trigger_offset(trigger):

    global xbox_model

    match trigger:
        case "LEFT":
            return xbox_model["trigger_left_offset"]
        case "RIGHT":
            return xbox_model["trigger_right_offset"]
        case _:
            raise ValueError("Raised by Xbox_model.is_trigger_offset(trigger)"
                             "\n'trigger' was " + str(trigger))


#   set_trigger_offset is a boolean setter method for the trigger group.
#
#   trigger: Type String
#   status : Type bool
#   return : None
#   error  : TypeError is raised when status is not of type bool
#   error  : ValueError when trigger is invalid
def set_trigger_status(trigger, status):

    global xbox_model

    if isinstance(status, bool):

        match trigger:
            case "LEFT":
                xbox_model["trigger_left_offset"] = status
            case "RIGHT":
                xbox_model["trigger_right_offset"] = status
            case _:
                raise ValueError("Raised by Xbox_model.set_trigger_offset(trigger, status)"
                                 "\n'trigger' was " + str(trigger))
    else:
        raise TypeError("Raised by Xbox_model.set_trigger_offset(trigger, status)"
                        "\n'status' must be of type bool, was " + str(type(status)))


#   get_offset_amount is a getter method for accessing the current
#   displacement of a particular trigger. The lowest value is 0.0 and the highest
#   is 1.0
#
#   trigger: Type String
#   return : Float trigger offset value
#   error  : ValueError is raised when trigger is invalid
def get_offset_amount(trigger):

    global xbox_model

    match trigger:
        case "LEFT":
            return xbox_model["trigger_left_offset_amount"]
        case "RIGHT":
            return xbox_model["trigger_right_offset_amount"]
        case _:
            raise ValueError("Raised by Xbox_model.get_offset_amount(trigger)"
                             "\n'trigger' was " + str(trigger))


#   set_offset_amount is a numerical setter method for updating the model
#   view of the triggers.
#
#   trigger: Type String
#   amount: Type float
#   return: None
#   error : TypeError is raised when amount is not of type float
#   error : ValueError when trigger is invalid. This can also be
#           raised if the 'amount' value is out of bounds (0.0 <= amount <= 1.0)
def set_trigger_offset(trigger, amount):

    global xbox_model

    if isinstance(amount, float):
        if amount < 0.0 or amount > 1.0:
            raise ValueError("Raised by Xbox_model.set_offset_amount(trigger, amount)"
                             "\n'amount' is out of bounds - must be between 0.0 and 1.0 inclusive.")
        else:
            match trigger:
                case "LEFT":
                    xbox_model["trigger_left_offset_amount"] = amount
                case "RIGHT":
                    xbox_model["trigger_right_offset_amount"] = amount
                case _:
                    raise ValueError("Raised by Xbox_model.set_offset_amount(trigger, amount)"
                                     "\n'trigger' is invalid was " + str(trigger))
    else:
        raise TypeError("Raised by Xbox_model.set_offset_amount(trigger, amount)"
                        "\n'amount' must be of type float, was " + str(type(amount)))


#   get_stick_position is a getter method for accessing the current
#   displacement of a particular stick on a particular axis.
#
#   stick  : Type String
#   axis   : Type String
#   return : Float stick displacement value on an axis
#   error  : ValueError is raised when trigger or axis is invalid
def get_stick_position(stick, axis):

    global xbox_model

    match stick:
        case "LEFT":
            match axis:
                case "X":
                    return xbox_model["stick_left_x"]
                case "Y":
                    return xbox_model["stick_left_y"]
                case _:
                    raise ValueError("Raised by Xbox_model.get_stick_position(stick, axis)"
                                     "\n'axis' was " + str(axis))
        case "RIGHT":
            match axis:
                case "X":
                    return xbox_model["stick_right_x"]
                case "Y":
                    return xbox_model["stick_right_y"]
                case _:
                    raise ValueError("Raised by Xbox_model.get_stick_position(stick, axis)"
                                     "\n'axis' is invalid was " + str(axis))
        case _:
            raise ValueError("Raised by Xbox_model.get_stick_position(stick, axis)"
                             "\n'stick' is invalid was " + str(stick))


#   set_stick_position is a numerical setter method for updating the model
#   view of the sticks along a given axis.
#
#   stick : Type String
#   axis  : Type Strong
#   amount: Type float
#   return: None
#   error : TypeError is raised when amount is not of type float
#   error : ValueError when stick or axis is invalid. This can
#           also be raised if the 'amount' value is out of bounds
#           (-1.0 <= amount <= 1.0)
def set_stick_position(stick, axis, amount):

    global xbox_model

    if isinstance(amount, float):
        if amount < -1.0 or amount > 1.0:
            raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                             "\n'amount' is out of bounds - must be between -1.0 and 1.0 inclusive.")
        else:
            match stick:
                case "LEFT":
                    match axis:
                        case "X":
                            xbox_model["stick_left_x"] = amount
                        case "Y":
                            xbox_model["stick_left_y"] = amount
                        case _:
                            raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                                             "\n'axis' was " + str(axis))
                case "RIGHT":
                    match axis:
                        case "X":
                            xbox_model["stick_right_x"] = amount
                        case "Y":
                            xbox_model["stick_right_y"] = amount
                        case _:
                            raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                                             "\n'axis' was " + str(axis))
                case _:
                    raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                                     "\n'stick' was " + str(stick))
    else:
        raise TypeError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                        "\n'amount' was not of type float, was " + str(type(amount)))


#   reset_model is a setter method for resetting all model values to their
#   default states, e.g., 'False' and 0.00
def reset_model():

    global xbox_model

    #   Resets Button Defaults
    xbox_model["pressed_button_a"] = False
    xbox_model["pressed_button_b"] = False
    xbox_model["pressed_button_x"] = False
    xbox_model["pressed_button_y"] = False

    #   Resets Shoulder Defaults
    xbox_model["pressed_shoulder_left"] = False
    xbox_model["pressed_shoulder_right"] = False

    #   Resets DPAD Defaults
    xbox_model["pressed_dpad_left"] = False
    xbox_model["pressed_dpad_right"] = False
    xbox_model["pressed_dpad_down"] = False
    xbox_model["pressed_dpad_up"] = False

    #   Resets Option Defaults
    xbox_model["pressed_start"] = False
    xbox_model["pressed_back"] = False

    #   Resets Stick Click Defaults
    xbox_model["pressed_left_thumb"] = False
    xbox_model["pressed_right_thumb"] = False

    #   Resets Trigger Defaults
    xbox_model["trigger_left_offset"] = False
    xbox_model["trigger_right_offset"] = False
    xbox_model["trigger_left_offset_amount"] = 0.00
    xbox_model["trigger_right_offset_amount"] = 0.00

    #   Resets Stick Defaults
    xbox_model["stick_left_x"] = 0.00
    xbox_model["stick_left_y"] = 0.00
    xbox_model["stick_right_x"] = 0.00
    xbox_model["stick_right_y"] = 0.00


#   get_model returns the entire model view of the controller in the form of
#   a dictionary. The dictionary definition can be found at the head of this
#   file.
def get_model():
    global xbox_model
    return xbox_model
