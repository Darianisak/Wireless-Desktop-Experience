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
#
#   button: Type String. Valid (A, B, X, Y)
#   return: True - button is depressed. False - button is not depressed
#   error : ValueError when button is invalid
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
            raise ValueError("Raised by Xbox_model.is_button_depressed(button)"
                             "\n'button' is invalid - Must be (A,B,X,Y), was " + str(button))


#   set_button_depressed is a boolean setter method for the button group.
#
#   button: Type String. Valid (A, B, X, Y)
#   status: Type bool
#   return: None
#   error : ValueError when status is not of type bool OR button is invalid
def set_button_depressed(button, status):

    global button_depressed_a, button_depressed_b, button_depressed_y
    global button_depressed_x

    if isinstance(status, bool):

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
                return ValueError("Raised by Xbox_model.set_button_depressed(button, status)"
                                  "\n'button' is invalid - Must be (A,B,X,Y), was " + str(button))
    else:
        raise ValueError("Raised by Xbox_model.set_button_depressed(button, status)"
                         "\n'status' must be of type bool, was " + str(type(status)))


shoulder_depressed_left = False
shoulder_depressed_right = False


#   is_shoulder_depressed is a boolean getter method for the shoulder group.
#
#   shoulder: Type String. Valid (LEFT, RIGHT)
#   return  : True - shoulder is depressed. False - shoulder is not depressed.
#   error   : ValueError when shoulder is invalid
def is_shoulder_depressed(shoulder):

    match shoulder:
        case "LEFT":
            return shoulder_depressed_left
        case "RIGHT":
            return shoulder_depressed_right
        case _:
            raise ValueError("Raised by Xbox_model.is_shoulder_depressed(shoulder)"
                             "\n'shoulder' is invalid - Must be (LEFT, RIGHT), "
                             "was " + str(shoulder))


#   is_shoulder_depressed is a boolean setter method for the shoulder group.
#
#   shoulder: Type String. Valid (LEFT, RIGHT)
#   status  : Type bool
#   return  : None
#   error   : ValueError when status is not of type bool OR shoulder is invalid
def set_shoulder_depressed(shoulder, status):

    global shoulder_depressed_right, shoulder_depressed_left

    if isinstance(status, bool):

        match shoulder:
            case "LEFT":
                shoulder_depressed_left = status
            case "RIGHT":
                shoulder_depressed_right = status
            case _:
                raise ValueError("Raised by Xbox_model.set_shoulder_depressed(shoulder, status)"
                                 "\n'shoulder' is invalid - Must be (LEFT, RIGHT), "
                                 "was " + str(shoulder))
    else:
        raise ValueError("Raised by Xbox_model.set_shoulder_depressed(shoulder, status)"
                         "\n'status' must be of type bool, was " + str(type(status)))


dpad_depressed_left = False
dpad_depressed_right = False
dpad_depressed_top = False
dpad_depressed_bottom = False


#   is_dpad_depressed is a boolean getter method for the dpad group.
#
#   dpad  : Type String. Valid (LEFT, RIGHT, TOP, BOTTOM)
#   return: True - dpad is depressed. False - dpad is not depressed
#   error : ValueError is raised when dpad is invalid
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
            raise ValueError("Raised by Xbox_model.is_dpad_depressed(dpad)"
                             "\n'dpad' is invalid - Must be (LEFT, RIGHT, TOP, BOTTOM), "
                             "was " + str(dpad))


#   is_dpad_depressed is a boolean setter method for the dpad group.
#
#   dpad  : Type String. Valid (LEFT, RIGHT, TOP, BOTTOM)
#   status: Type bool
#   return: None
#   error : ValueError is raised when status is not of type bool OR when
#           dpad is invalid
def set_dpad_depressed(dpad, status):

    global dpad_depressed_left, dpad_depressed_right, dpad_depressed_top
    global dpad_depressed_bottom

    if isinstance(status, bool):

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
                raise ValueError("Raised by Xbox_model.set_dpad_depressed(dpad, status)"
                                 "\n'dpad' is invalid - Must be (LEFT, RIGHT, TOP, BOTTOM), "
                                 "was " + str(dpad))
    else:
        raise ValueError("Raised by Xbox_model.set_dpad_depressed(dpad, status)"
                         "\n'status' must be of type bool, was " + str(type(status)))


start_depressed = False
back_depressed = False


#   is_option_depressed is a boolean getter method for the option group.
#
#   option: Type String. Valid (START, BACK)
#   return: True - option is depressed. False - option is not depressed
#   error : ValueError is raised when option is invalid
def is_option_depressed(option):

    match option:
        case "START":
            return start_depressed
        case "BACK":
            return back_depressed
        case _:
            raise ValueError("Raised by Xbox_model.is_option_depressed(option)"
                             "\n'option' is invalid - Must be (START, BACK), was " + str(option))


#   is_option_depressed is a boolean setter method for the option group.
#
#   option: Type String. Valid (START, BACK)
#   status: Type bool
#   return: None
#   error : ValueError is raised when status is not of type bool OR when option
#           is invalid
def set_option_depressed(option, status):

    global start_depressed, back_depressed

    if isinstance(status, bool):

        match option:
            case "START":
                start_depressed = status
            case "BACK":
                back_depressed = status
            case _:
                raise ValueError("Raised by Xbox_model.set_option_depressed(option, status)"
                                 "\n'option' is invalid - Must be (START, BACK), was " + str(option))
    else:
        raise ValueError("Raised by Xbox_model.set_option_depressed(option, status)"
                         "\n'status' must be of type bool, was " + str(type(status)))


#   Analogue Control Values

trigger_left_depressed = False
trigger_left_depression_amount = 0.00

trigger_right_depressed = False
trigger_right_depression_amount = 0.00


#   is_trigger_depressed is a boolean getter method for the trigger group.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   return : True - trigger is depressed. False - trigger is not depressed
#   error  : ValueError is raised when trigger is invalid
def is_trigger_depressed(trigger):

    match trigger:
        case "LEFT":
            return trigger_left_depressed
        case "RIGHT":
            return trigger_right_depressed
        case _:
            raise ValueError("Raised by Xbox_model.is_trigger_depressed(trigger)"
                             "\n'trigger' is invalid - Must be (LEFT, RIGHT), was " + str(trigger))


#   set_trigger_depressed is a boolean setter method for the trigger group.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   status : Type bool
#   return : None
#   error  : ValueError is raised when status is not of type bool OR when
#            trigger is invalid
def set_trigger_depressed(trigger, status):

    global trigger_left_depressed, trigger_right_depressed

    if isinstance(status, bool):

        match trigger:
            case "LEFT":
                trigger_left_depressed = status
            case "RIGHT":
                trigger_right_depressed = status
            case _:
                raise ValueError("Raised by Xbox_model.set_trigger_depressed(trigger, status)"
                                 "\n'trigger' is invalid - Must be (LEFT, RIGHT), was " + str(trigger))
    else:
        raise ValueError("Raised by Xbox_model.set_trigger_depressed(trigger, status)"
                         "\n'status' must be of type bool, was " + str(type(status)))


#   get_depression_amount is a getter method for accessing the current
#   displacement of a particular trigger.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   return : Float trigger depression value
#   error  : ValueError is raised when trigger is invalid
def get_depression_amount(trigger):

    match trigger:
        case "LEFT":
            return trigger_left_depression_amount
        case "RIGHT":
            return trigger_right_depression_amount
        case _:
            raise ValueError("Raised by Xbox_model.get_depression_amount(trigger)"
                             "\n'trigger' is invalid - Must be (LEFT, RIGHT), was " + str(trigger))


#   set_depression_amount is a numerical setter method for updating the model
#   view of the triggers.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   amount: Type float
#   return: None
#   error : ValueError is raised when amount is not of type float OR when
#           trigger is invalid
def set_depression_amount(trigger, amount):

    global trigger_left_depression_amount, trigger_right_depression_amount

    if isinstance(amount, float):

        match trigger:
            case "LEFT":
                trigger_left_depression_amount = amount
            case "RIGHT":
                trigger_right_depression_amount = amount
            case _:
                raise ValueError("Raised by Xbox_model.set_depression_amount(trigger, amount)"
                                 "\n'trigger' is invalid - Must be (LEFT, RIGHT), was " + str(trigger))
    else:
        raise ValueError("Raised by Xbox_model.set_depressions_amount(trigger, amount)"
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
#           or axis is invalid
def set_stick_position(stick, axis, amount):

    global stick_left_x, stick_left_y, stick_right_x, stick_right_y

    if isinstance(amount, float):

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
        raise ValueError("Raised by Xbox_model.set_stick_position(stick, axis, amount)"
                         "\n'amount' was not of type float, was " + str(type(amount)))


print(set_stick_position("LEFT", 1, 1.0))
