#   xbox_model represents an xbox controller object, through
#   which more complicated expressions can be communicated by the end user.
#   More complicated expressions include actions that are dependant on another
#   buttons being offset concurrently, for example.

#   <---    XBOX CONTROLLER MODEL FIELDS    --->

#   Binary Control Values

#   Primary Button Fields
pressed_button_a = False
pressed_button_b = False
pressed_button_x = False
pressed_button_y = False

#   Shoulder Fields
pressed_shoulder_left = False
pressed_shoulder_right = False

#   Thumb Click Fields
pressed_right_thumb = False # todo no tests
pressed_left_thumb = False # TODO no tests

#   Option Fields
pressed_start = False
pressed_back = False

#   DPAD Fields
pressed_dpad_up = False
pressed_dpad_right = False
pressed_dpad_down = False
pressed_dpad_left = False


#   is_button_offset is a boolean getter method for the button group.
#
#   button: Type String. Valid (A, B, X, Y)
#   return: True - button is offset. False - button is not offset
#   error : ValueError when button is invalid
def get_button_status(button):

    global pressed_button_a, pressed_button_b, pressed_button_x, pressed_button_y
    global pressed_shoulder_left, pressed_shoulder_right
    global pressed_left_thumb, pressed_right_thumb
    global pressed_start, pressed_back
    global pressed_dpad_left, pressed_dpad_right, pressed_dpad_down, pressed_dpad_up

    match button:
        case "A":
            return pressed_button_a
        case "B":
            return pressed_button_b
        case "X":
            return pressed_button_x
        case "Y":
            return pressed_button_y
        case "LEFT_SHOULDER":
            return pressed_shoulder_left
        case "RIGHT_SHOULDER":
            return pressed_shoulder_right
        case "LEFT_THUMB":
            return pressed_left_thumb
        case "RIGHT_THUMB":
            return pressed_right_thumb
        case "START":
            return pressed_start
        case "BACK":
            return pressed_back
        case "DPAD_UP":
            return pressed_dpad_up
        case "DPAD_DOWN":
            return pressed_dpad_down
        case "DPAD_LEFT":
            return pressed_dpad_left
        case "DPAD_RIGHT":
            return pressed_dpad_right
        case _:
            raise ValueError("Raised by Xbox_model.get_button_status(button)"
                             "\n'button' was " + str(button))


#   set_button_offset is a boolean setter method for the button group.
#
#   button: Type String. Valid (A, B, X, Y)
#   status: Type bool
#   return: None
#   error : ValueError when status is not of type bool OR button is invalid
def set_button_status(button, status):

    global pressed_button_a, pressed_button_b, pressed_button_x, pressed_button_y
    global pressed_shoulder_left, pressed_shoulder_right
    global pressed_left_thumb, pressed_right_thumb
    global pressed_start, pressed_back
    global pressed_dpad_left, pressed_dpad_right, pressed_dpad_down, pressed_dpad_up

    if isinstance(status, bool):

        match button:
            case "A":
                pressed_button_a = status
            case "B":
                pressed_button_b = status
            case "X":
                pressed_button_x = status
            case "Y":
                pressed_button_y = status
            case "LEFT_SHOULDER":
                pressed_shoulder_left = status
            case "RIGHT_SHOULDER":
                pressed_shoulder_right = status
            case "LEFT_THUMB":
                pressed_left_thumb = status
            case "RIGHT_THUMB":
                pressed_right_thumb = status
            case "START":
                pressed_start = status
            case "BACK":
                pressed_back = status
            case "DPAD_UP":
                pressed_dpad_up = status
            case "DPAD_DOWN":
                pressed_dpad_down = status
            case "DPAD_LEFT":
                pressed_dpad_left = status
            case "DPAD_RIGHT":
                pressed_dpad_right = status
            case _:
                return ValueError("Raised by Xbox_model.set_button_status(button, status)"
                                  "\n'button' was " + str(button))
    else:
        raise TypeError("Raised by Xbox_model.set_button_status(button, status)"
                        "\n'status' must be of type bool, was " + str(type(status)))


#   Analogue Control Values

trigger_left_offset = False
trigger_left_offset_amount = 0.00

trigger_right_offset = False
trigger_right_offset_amount = 0.00


#   is_trigger_offset is a boolean getter method for the trigger group.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   return : True - trigger is offset. False - trigger is not offset
#   error  : ValueError is raised when trigger is invalid
def is_trigger_offset(trigger):
    global trigger_left_offset, trigger_right_offset

    match trigger:
        case "LEFT":
            return trigger_left_offset
        case "RIGHT":
            return trigger_right_offset
        case _:
            raise ValueError("Raised by Xbox_model.is_trigger_offset(trigger)"
                             "\n'trigger' is invalid - Must be (LEFT, RIGHT), was " + str(trigger))


#   set_trigger_offset is a boolean setter method for the trigger group.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   status : Type bool
#   return : None
#   error  : ValueError is raised when status is not of type bool OR when
#            trigger is invalid
def set_trigger_status(trigger, status):
    global trigger_left_offset, trigger_right_offset

    if isinstance(status, bool):

        match trigger:
            case "LEFT":
                trigger_left_offset = status
            case "RIGHT":
                trigger_right_offset = status
            case _:
                raise ValueError("Raised by Xbox_model.set_trigger_offset(trigger, status)"
                                 "\n'trigger' is invalid - Must be (LEFT, RIGHT), was " + str(trigger))
    else:
        raise TypeError("Raised by Xbox_model.set_trigger_offset(trigger, status)"
                        "\n'status' must be of type bool, was " + str(type(status)))


#   get_offset_amount is a getter method for accessing the current
#   displacement of a particular trigger. The lowest value is 0.0 and the highest
#   is 1.0
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   return : Float trigger offset value
#   error  : ValueError is raised when trigger is invalid.
def get_offset_amount(trigger):
    global trigger_left_offset_amount, trigger_right_offset_amount

    match trigger:
        case "LEFT":
            return trigger_left_offset_amount
        case "RIGHT":
            return trigger_right_offset_amount
        case _:
            raise ValueError("Raised by Xbox_model.get_offset_amount(trigger)"
                             "\n'trigger' is invalid - Must be (LEFT, RIGHT), was " + str(trigger))


#   set_offset_amount is a numerical setter method for updating the model
#   view of the triggers.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   amount: Type float
#   return: None
#   error : ValueError is raised when amount is not of type float OR when
#           trigger is invalid. This can also be raised if the 'amount' value
#           is out of bounds (0.0 <= amount <= 1.0)
def set_trigger_offset(trigger, amount):
    global trigger_left_offset_amount, trigger_right_offset_amount

    if isinstance(amount, float):
        if amount < 0.0 or amount > 1.0:
            raise ValueError("Raised by Xbox_model.set_offset_amount(trigger, amount)"
                             "\n'amount' is out of bounds - must be between 0.0 and 1.0 inclusive.")
        else:
            match trigger:
                case "LEFT":
                    trigger_left_offset_amount = amount
                case "RIGHT":
                    trigger_right_offset_amount = amount
                case _:
                    raise ValueError("Raised by Xbox_model.set_offset_amount(trigger, amount)"
                                     "\n'trigger' is invalid - Must be (LEFT, RIGHT), was " + str(trigger))
    else:
        raise TypeError("Raised by Xbox_model.set_offset_amount(trigger, amount)"
                        "\n'amount' must be of type float, was " + str(type(amount)))


stick_left_x = 0.0
stick_left_y = 0.0

stick_right_x = 0.0
stick_right_y = 0.0


#   get_stick_position is a getter method for accessing the current
#   displacement of a particular stick on a particular axis.
#
#   stick  : Type String. Valid (LEFT, RIGHT)
#   axis   : Type String. Valid (X, Y)
#   return : Float stick displacement value on an axis
#   error  : ValueError is raised when trigger or axis is invalid
def get_stick_position(stick, axis):
    global stick_left_x, stick_left_y, stick_right_x, stick_right_y

    match stick:
        case "LEFT":
            match axis:
                case "X":
                    return stick_left_x
                case "Y":
                    return stick_left_y
                case _:
                    raise ValueError("Raised by Xbox_model.get_stick_position(stick, axis)"
                                     "\n'axis' is invalid - Must be (X, Y), was " + str(axis))
        case "RIGHT":
            match axis:
                case "X":
                    return stick_right_x
                case "Y":
                    return stick_right_y
                case _:
                    raise ValueError("Raised by Xbox_model.get_stick_position(stick, axis)"
                                     "\n'axis' is invalid - Must be (X, Y), was " + str(axis))
        case _:
            raise ValueError("Raised by Xbox_model.get_stick_position(stick, axis)"
                             "\n'stick' is invalid - Must be (LEFT, RIGHT), was " + str(stick))


#   set_stick_position is a numerical setter method for updating the model
#   view of the sticks along a given axis.
#
#   stick : Type String. Valid (LEFT, RIGHT)
#   axis  : Type Strong. Valid (X, Y)
#   amount: Type float
#   return: None
#   error : ValueError is raised when amount is not of type float OR when stick
#           or axis is invalid. This can also be raised if the 'amount' value
#           is out of bounds (-1.0 <= amount <= 1.0)
def set_stick_position(stick, axis, amount):

    global stick_left_x, stick_left_y, stick_right_x, stick_right_y

    if isinstance(amount, float):
        if amount < -1.0 or amount > 1.0:
            raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                             "\n'amount' is out of bounds - must be between -1.0 and 1.0 inclusive.")
        else:
            match stick:
                case "LEFT":
                    match axis:
                        case "X":
                            stick_left_x = amount
                        case "Y":
                            stick_left_y = amount
                        case _:
                            raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                                             "\n'axis' is invalid - Must be (X, Y), was " + str(axis))
                case "RIGHT":
                    match axis:
                        case "X":
                            stick_right_x = amount
                        case "Y":
                            stick_right_y = amount
                        case _:
                            raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                                             "\n'axis' is invalid - Must be (X, Y), was " + str(axis))
                case _:
                    raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                                     "\n'stick' is invalid - Must be (LEFT, RIGHT), was " + str(stick))
    else:
        raise TypeError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                        "\n'amount' was not of type float, was " + str(type(amount)))


#   reset_model is a setter method for resetting all model values to their
#   default states, e.g., 'False' and 0.00
def reset_model():

    global pressed_button_a, pressed_button_b, pressed_button_x, pressed_button_y
    global pressed_shoulder_left, pressed_shoulder_right
    global pressed_left_thumb, pressed_right_thumb
    global pressed_start, pressed_back
    global pressed_dpad_left, pressed_dpad_right, pressed_dpad_down, pressed_dpad_up

    #   Resets Button Defaults
    pressed_button_a = False
    pressed_button_b = False
    pressed_button_x = False
    pressed_button_y = False

    #   Resets Shoulder Defaults
    pressed_shoulder_left = False
    pressed_shoulder_right = False

    #   Resets DPAD Defaults
    pressed_dpad_left = False
    pressed_dpad_right = False
    pressed_dpad_down = False
    pressed_dpad_up = False

    #   Resets Option Defaults
    pressed_start = False
    pressed_back = False

    #   Resets Stick Click Defaults
    pressed_left_thumb = False
    pressed_right_thumb = False

    #   Resets Trigger Defaults
    global trigger_left_offset, trigger_right_offset
    global trigger_left_offset_amount, trigger_right_offset_amount

    trigger_left_offset = False
    trigger_right_offset = False
    trigger_left_offset_amount = 0.00
    trigger_right_offset_amount = 0.00

    #   Resets Stick Defaults
    global stick_left_x, stick_left_y, stick_right_x, stick_right_y

    stick_left_x = 0.00
    stick_left_y = 0.00
    stick_right_x = 0.00
    stick_right_y = 0.00
