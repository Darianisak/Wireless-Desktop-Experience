import App_Exceptions as AE

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
#   error : AE.InvalidModelSelection when button is invalid
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
            raise AE.InvalidModelSelection #todo


#   set_button_depressed is a boolean setter method for the button group.
#
#   button: Type String. Valid (A, B, X, Y)
#   status: Type bool
#   return: None
#   error : AE.InvalidModelSelection when button is invalid
#   error : ValueError when status is not of type bool
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
                return AE.InvalidModelSelection #todo
    else:
        raise ValueError #todo


shoulder_depressed_left = False
shoulder_depressed_right = False


#   is_shoulder_depressed is a boolean getter method for the shoulder group.
#
#   shoulder: Type String. Valid (LEFT, RIGHT)
#   return  : True - shoulder is depressed. False - shoulder is not depressed.
#   error   : InvalidModelSelection when shoulder is invalid
def is_shoulder_depressed(shoulder):

    match shoulder:
        case "LEFT":
            return shoulder_depressed_left
        case "RIGHT":
            return shoulder_depressed_right
        case _:
            raise AE.InvalidModelSelection # todo


#   is_shoulder_depressed is a boolean setter method for the shoulder group.
#
#   shoulder: Type String. Valid (LEFT, RIGHT)
#   status  : Type bool
#   return  : None
#   error   : AE.InvalidModelSelection when shoulder is invalid
#   error   : ValueError when status is not of type bool
def set_shoulder_depressed(shoulder, status):

    global shoulder_depressed_right, shoulder_depressed_left

    if isinstance(status, bool):

        match shoulder:
            case "LEFT":
                shoulder_depressed_left = status
            case "RIGHT":
                shoulder_depressed_right = status
            case _:
                raise AE.InvalidModelSelection  #todo
    else:
        raise ValueError #todo


dpad_depressed_left = False
dpad_depressed_right = False
dpad_depressed_top = False
dpad_depressed_bottom = False


#   is_dpad_depressed is a boolean getter method for the dpad group.
#
#   dpad  : Type String. Valid (LEFT, RIGHT, TOP, BOTTOM)
#   return: True - dpad is depressed. False - dpad is not depressed
#   error : InvalidModelSelection is raised when dpad is invalid
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
            raise AE.InvalidModelSelection #todo


#   is_dpad_depressed is a boolean setter method for the dpad group.
#
#   dpad  : Type String. Valid (LEFT, RIGHT, TOP, BOTTOM)
#   status: Type bool
#   return: None
#   error : InvalidModelSelection is raised when dpad is invalid
#   error : ValueError is raised when status is not of type bool
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
                raise AE.InvalidModelSelection #todo
    else:
        raise ValueError #todo


start_depressed = False
back_depressed = False


#   is_option_depressed is a boolean getter method for the option group.
#
#   option: Type String. Valid (START, BACK)
#   return: True - option is depressed. False - option is not depressed
#   error : InvalidModelSelection is raised when option is invalid
def is_option_depressed(option):

    match option:
        case "START":
            return start_depressed
        case "BACK":
            return back_depressed
        case _:
            raise AE.InvalidModelSelection #todo


#   is_option_depressed is a boolean setter method for the option group.
#
#   option: Type String. Valid (START, BACK)
#   status: Type bool
#   return: None
#   error : InvalidModelSelection is raised when option is invalid
#   error : ValueError is raised when status is not of type bool
def set_option_depressed(option, status):

    global start_depressed, back_depressed

    if isinstance(status, bool):

        match option:
            case "START":
                start_depressed = status
            case "BACK":
                back_depressed = status
            case _:
                raise AE.InvalidModelSelection #todo
    else:
        raise ValueError #todo


#   Analogue Control Values

trigger_left_depressed = False
trigger_left_depression_amount = 0.00

trigger_right_depressed = False
trigger_right_depression_amount = 0.00


#   is_trigger_depressed is a boolean getter method for the trigger group.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   return : True - trigger is depressed. False - trigger is not depressed
#   error  : InvalidModelSelection is raised when trigger is invalid
def is_trigger_depressed(trigger):

    match trigger:
        case "LEFT":
            return trigger_left_depressed
        case "RIGHT":
            return trigger_right_depressed
        case _:
            raise AE.InvalidModelSelection #todo


#   set_trigger_depressed is a boolean setter method for the trigger group.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   status : Type bool
#   return : None
#   error  : InvalidModelSelection is raised when trigger is invalid
#   error  : ValueError is raised when status is not of type bool
def set_trigger_depressed(trigger, status):

    global trigger_left_depressed, trigger_right_depressed

    if isinstance(status, bool):

        match trigger:
            case "LEFT":
                trigger_left_depressed = status
            case "RIGHT":
                trigger_right_depressed = status
            case _:
                raise AE.InvalidModelSelection#todo
    else:
        raise ValueError#todo


#   get_depression_amount is a getter method for accessing the current
#   displacement of a particular trigger.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   return : Float trigger depression value
#   error  : InvalidModelSelection is raised when trigger is invalid
def get_depression_amount(trigger):

    match trigger:
        case "LEFT":
            return trigger_left_depression_amount
        case "RIGHT":
            return trigger_right_depression_amount
        case _:
            raise AE.InvalidModelSelection #todo


#   set_depression_amount is a numerical setter method for updating the model
#   view of the triggers.
#
#   trigger: Type String. Valid (LEFT, RIGHT)
#   amount: Type float
#   return: None
#   error : InvalidModelSelection is raised when trigger is invalid
#   error : ValueError is raised when amount is not of type float
def set_depression_amount(trigger, amount):

    global trigger_left_depression_amount, trigger_right_depression_amount

    if isinstance(amount, float):

        match trigger:
            case "LEFT":
                trigger_left_depression_amount = amount
            case "RIGHT":
                trigger_right_depression_amount = amount
            case _:
                raise AE.InvalidModelSelection#todo
    else:
        raise ValueError #todo


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
#   error  : InvalidModelSelection is raised when trigger or axis is invalid
def get_stick_position(stick, axis):

    match stick:
        case "LEFT":
            match axis:
                case "X":
                    return stick_left_x
                case "Y":
                    return stick_left_y
                case _:
                    raise AE.InvalidModelSelection #todo
        case "RIGHT":
            match axis:
                case "X":
                    return stick_right_x
                case "Y":
                    return stick_right_y
                case _:
                    raise AE.InvalidModelSelection#todo
        case _:
            raise AE.InvalidModelSelection #todo


#   set_stick_position is a numerical setter method for updating the model
#   view of the sticks along a given axis.
#
#   stick : Type String. Valid (LEFT, RIGHT)
#   axis  : Type Strong. Valid (X, Y)
#   amount: Type float
#   return: None
#   error : InvalidModelSelection is raised when stick or axis is invalid
#   error : ValueError is raised when amount is not of type float
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
                        raise AE.InvalidModelSelection #todo
            case "RIGHT":
                match axis:
                    case "X":
                        stick_right_x = amount
                    case "Y":
                        stick_right_y = amount
                    case _:
                        raise AE.InvalidModelSelection # todo
            case _:
                raise AE.InvalidModelSelection #todo
    else:
        raise ValueError #todo
