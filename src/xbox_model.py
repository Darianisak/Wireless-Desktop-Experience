#   xbox_model is a class that represents an xbox controller object, through
#   which more complicated expressions can be communicated by the end user.
#   More complicated expressions include actions that are dependant on another
#   buttons being offset concurrently, for example.

#   <---    XBOX CONTROLLER MODEL FIELDS    --->

#   Binary Control Values

button_offset_a = False
button_offset_b = False
button_offset_x = False
button_offset_y = False


#   is_button_offset is a boolean getter method for the button group.
#
#   button: Type String. Valid (A, B, X, Y)
#   return: True - button is offset. False - button is not offset
#   error : ValueError when button is invalid
def is_button_offset(button):
    global button_offset_a, button_offset_b
    global button_offset_x, button_offset_y

    match button:
        case "A":
            return button_offset_a
        case "B":
            return button_offset_b
        case "X":
            return button_offset_x
        case "Y":
            return button_offset_y
        case _:
            raise ValueError("Raised by Xbox_model.is_button_offset(button)"
                             "\n'button' is invalid - Must be (A,B,X,Y), was " + str(button))


#   set_button_offset is a boolean setter method for the button group.
#
#   button: Type String. Valid (A, B, X, Y)
#   status: Type bool
#   return: None
#   error : ValueError when status is not of type bool OR button is invalid
def set_button_offset(button, status):
    global button_offset_a, button_offset_b, button_offset_y
    global button_offset_x

    if isinstance(status, bool):

        match button:
            case "A":
                button_offset_a = status
            case "B":
                button_offset_b = status
            case "X":
                button_offset_x = status
            case "Y":
                button_offset_y = status
            case _:
                return ValueError("Raised by Xbox_model.set_button_offset(button, status)"
                                  "\n'button' is invalid - Must be (A,B,X,Y), was " + str(button))
    else:
        raise TypeError("Raised by Xbox_model.set_button_offset(button, status)"
                        "\n'status' must be of type bool, was " + str(type(status)))


shoulder_offset_left = False
shoulder_offset_right = False


#   is_shoulder_offset is a boolean getter method for the shoulder group.
#
#   shoulder: Type String. Valid (LEFT, RIGHT)
#   return  : True - shoulder is offset. False - shoulder is not offset.
#   error   : ValueError when shoulder is invalid
def is_shoulder_offset(shoulder):
    global shoulder_offset_left, shoulder_offset_right

    match shoulder:
        case "LEFT":
            return shoulder_offset_left
        case "RIGHT":
            return shoulder_offset_right
        case _:
            raise ValueError("Raised by Xbox_model.is_shoulder_offset(shoulder)"
                             "\n'shoulder' is invalid - Must be (LEFT, RIGHT), "
                             "was " + str(shoulder))


#   is_shoulder_offset is a boolean setter method for the shoulder group.
#
#   shoulder: Type String. Valid (LEFT, RIGHT)
#   status  : Type bool
#   return  : None
#   error   : ValueError when status is not of type bool OR shoulder is invalid
def set_shoulder_offset(shoulder, status):
    global shoulder_offset_right, shoulder_offset_left

    if isinstance(status, bool):

        match shoulder:
            case "LEFT":
                shoulder_offset_left = status
            case "RIGHT":
                shoulder_offset_right = status
            case _:
                raise ValueError("Raised by Xbox_model.set_shoulder_offset(shoulder, status)"
                                 "\n'shoulder' is invalid - Must be (LEFT, RIGHT), "
                                 "was " + str(shoulder))
    else:
        raise TypeError("Raised by Xbox_model.set_shoulder_offset(shoulder, status)"
                        "\n'status' must be of type bool, was " + str(type(status)))


dpad_offset_left = False
dpad_offset_right = False
dpad_offset_top = False
dpad_offset_bottom = False


#   is_dpad_offset is a boolean getter method for the dpad group.
#
#   dpad  : Type String. Valid (LEFT, RIGHT, TOP, BOTTOM)
#   return: True - dpad is offset. False - dpad is not offset
#   error : ValueError is raised when dpad is invalid
def is_dpad_offset(dpad):
    global dpad_offset_left, dpad_offset_right
    global dpad_offset_bottom, dpad_offset_top

    match dpad:
        case "LEFT":
            return dpad_offset_left
        case "RIGHT":
            return dpad_offset_right
        case "TOP":
            return dpad_offset_top
        case "BOTTOM":
            return dpad_offset_bottom
        case _:
            raise ValueError("Raised by Xbox_model.is_dpad_offset(dpad)"
                             "\n'dpad' is invalid - Must be (LEFT, RIGHT, TOP, BOTTOM), "
                             "was " + str(dpad))


#   is_dpad_offset is a boolean setter method for the dpad group.
#
#   dpad  : Type String. Valid (LEFT, RIGHT, TOP, BOTTOM)
#   status: Type bool
#   return: None
#   error : ValueError is raised when status is not of type bool OR when
#           dpad is invalid
def set_dpad_offset(dpad, status):
    global dpad_offset_left, dpad_offset_right, dpad_offset_top
    global dpad_offset_bottom

    if isinstance(status, bool):

        match dpad:
            case "LEFT":
                dpad_offset_left = status
            case "RIGHT":
                dpad_offset_right = status
            case "TOP":
                dpad_offset_top = status
            case "BOTTOM":
                dpad_offset_bottom = status
            case _:
                raise ValueError("Raised by Xbox_model.set_dpad_offset(dpad, status)"
                                 "\n'dpad' is invalid - Must be (LEFT, RIGHT, TOP, BOTTOM), "
                                 "was " + str(dpad))
    else:
        raise TypeError("Raised by Xbox_model.set_dpad_offset(dpad, status)"
                        "\n'status' must be of type bool, was " + str(type(status)))


start_offset = False
back_offset = False


#   is_option_offset is a boolean getter method for the option group.
#
#   option: Type String. Valid (START, BACK)
#   return: True - option is offset. False - option is not offset
#   error : ValueError is raised when option is invalid
def is_option_offset(option):
    global start_offset, back_offset

    match option:
        case "START":
            return start_offset
        case "BACK":
            return back_offset
        case _:
            raise ValueError("Raised by Xbox_model.is_option_offset(option)"
                             "\n'option' is invalid - Must be (START, BACK), was " + str(option))


#   is_option_offset is a boolean setter method for the option group.
#
#   option: Type String. Valid (START, BACK)
#   status: Type bool
#   return: None
#   error : ValueError is raised when status is not of type bool OR when option
#           is invalid
def set_option_offset(option, status):
    global start_offset, back_offset

    if isinstance(status, bool):

        match option:
            case "START":
                start_offset = status
            case "BACK":
                back_offset = status
            case _:
                raise ValueError("Raised by Xbox_model.set_option_offset(option, status)"
                                 "\n'option' is invalid - Must be (START, BACK), was " + str(option))
    else:
        raise TypeError("Raised by Xbox_model.set_option_offset(option, status)"
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
    #   Resets Button Defaults
    global button_offset_a, button_offset_b
    global button_offset_x, button_offset_y

    button_offset_a = False
    button_offset_b = False
    button_offset_x = False
    button_offset_y = False

    #   Resets Shoulder Defaults
    global shoulder_offset_left, shoulder_offset_right

    shoulder_offset_left = False
    shoulder_offset_right = False

    #   Resets DPAD Defaults
    global dpad_offset_left, dpad_offset_right
    global dpad_offset_top, dpad_offset_bottom

    dpad_offset_left = False
    dpad_offset_right = False
    dpad_offset_bottom = False
    dpad_offset_top = False

    #   Resets Option Defaults
    global start_offset, back_offset

    start_offset = False
    back_offset = False

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
