import xbox_model as model
import XInput as xbox

#   xbox_interface is responsible for receiving controller events, adjusting
#   the model, and returning information appropriately

#   Used to manage the state of the controllers rumble motors
motor_detail = {
    #   Define rumble speed - max 65535, min 0
    "left_strength": 0,
    "right_strength": 0,
    "left_active": False,
    "right_active":False
}


#   TODO Refactor this into smaller more specific methods - this is clunky
#   set_preference is used to update controller variables. This in turn impacts
#   the values outputted by read_controller, e.g. higher dead zone values lead to
#   less stick events
#
#   pref    : Type String
#   modifier: Type String
#   value   : Type Integer
#   return  : None
#   Stick   : max 32767   min 0
#   Trigger : max 255     min 0
#   Rumble  : max 65535   min 0
#   error   : TypeError when value is not of type Integer
#   error   : ValueError when pref is invalid. This can also be raised if 'value'
#            exceeds or proceeds the max/min for a given assignment.
def set_preference(pref, modifier, value):

    global rumble_strength

    if isinstance(value, int):

        match pref:
            case "STICK":
                if value < 0 or value > 32767:
                    #   Raises an error in the case of the stick dead zone being
                    #   out of bounds
                    raise ValueError("Raised by Xbox_interface.set_preference(pref, modifier, value)"
                                     "\n'value' was " + str(value))
                else:
                    match modifier:
                        case "LEFT":
                            xbox.set_deadzone(xbox.DEADZONE_LEFT_THUMB, value)
                        case "RIGHT":
                            xbox.set_deadzone(xbox.DEADZONE_RIGHT_THUMB, value)
                        case _:
                            raise ValueError("Raised by Xbox_interface.set_preference(pref, modifier, value)"
                                             "\n'dir was " + str(dir))
            case "RUMBLE":
                if value < 0 or value > 65535:
                    #   Raises an error in the case of the rumble strength being
                    #   out of bounds
                    raise ValueError("Raised by Xbox_interface.set_preference(pref, modifier, value)"
                                     "\n'value' was " + str(value))
                else:
                    match modifier:
                        case "LEFT":
                            #   Applies rumble strength for the left motor
                            motor_detail["left_strength"] = value
                        case "RIGHT":
                            #   Applies rumble strength for the right motor
                            motor_detail["right_strength"] = value
                        case _:
                            raise ValueError("Raised by Xbox_interface.set_preference(pref, modifier, value)"
                                             "\n'dir was " + str(dir))
            case "TRIGGERS":
                if value < 0 or value > 255:
                    #   Raises an error in the case of the trigger dead zone being
                    #   out of bounds
                    raise ValueError("Raised by Xbox_interface.set_preference(pref, modifier, value)"
                                     "\n'value' was " + str(value))
                else:
                    #   Applies dead zone value for the triggers
                    xbox.set_deadzone(xbox.DEADZONE_TRIGGER)
            case _:
                raise ValueError("Raised by Xbox_interface.set_preference(pref, modifier, value)"
                                 "\n'pref' was " + str(pref))
    else:
        raise TypeError("Raised Xbox_interface.set_preference(pref, modifier, value)"
                        "\n'value' was not of type int, was " + str(type(value)))


#   todo
def get_battery():
    print("1")


#   TODO write tests
#   toggle_vibration is used to switch the rumble motors on and off
#
#   side    : Type String
#   return  : None
#   error   : ValueError is raised when side is invalid
def toggle_vibration(side):

    global motor_detail

    match side:
        case "LEFT":
            if motor_detail["left_active"]:
                #   The left motor was on originally
                if motor_detail["right_active"]:
                    #   Left off, right on
                    motor_detail["left_active"] = False
                    xbox.set_vibration(0, 0, motor_detail["right_strength"])
                else:
                    #   Left off, right off
                    motor_detail["left_active"] = False
                    xbox.set_vibration(0, 0, 0)
            else:
                #   The left motor was off originally
                if motor_detail["right_active"]:
                    #   Left on, right on
                    motor_detail["left_active"] = True
                    xbox.set_vibration(0, motor_detail["left_strength"], motor_detail["right_strength"])
                else:
                    #   Left on, right off
                    motor_detail["left_active"] = True
                    xbox.set_vibration(0, motor_detail["left_strength"], 0)
        case "RIGHT":
            if motor_detail["right_active"]:
                #   The right motor was on originally
                if motor_detail["left_active"]:
                    #   Left on, right off
                    motor_detail["right_active"] = False
                    xbox.set_vibration(0, motor_detail["left_strength"], 0)
                else:
                    #   Left off, right off
                    motor_detail["right_active"] = False
                    xbox.set_vibration(0, 0, 0)
            else:
                #   The right motor was off originally
                if motor_detail["left_active"]:
                    #   Left on, right on
                    motor_detail["right_active"] = True
                    xbox.set_vibration(0, motor_detail["left_strength"], motor_detail["right_strength"])
                else:
                    #   Left off, right on
                    motor_detail["right_active"] = True
                    xbox.set_vibration(0, 0, motor_detail["right_strength"])
        case _:
            raise ValueError("Raised by Xbox_interface.toggle_vibration(side)"
                             "\n'side' was " + str(side))


#   read_controller is responsible for pulling in new event information, and
#   performing appropriate actions on said information. This function will
#   return if no controller is connected
def read_controller():

    #   Todo refine this - currently it returns a whole lot of none lists, i.e. cycles where nothing has happened
    #   todo    so why don't we just add a sentinenl so it only returns an event dict when something actually
    #   todo happens

    #   todo this works really well - tidy implementation up though
    sentinel_value = False

    current_event = xbox.get_events()

    #   Used to catch errors in the advent of a controller disconnect
    try:
        for event in current_event:

            #   Button Press
            if event.type == 3:

                sentinel_value = True

                model.set_button_status(event.button, True)

            #   Button Release
            if event.type == 4:

                sentinel_value = True

                model.set_button_status(event.button, False)

            #   Trigger Event
            if event.type == 5:

                sentinel_value = True

                if event.trigger == 0:
                    model.set_trigger_offset("LEFT", event.value)
                else:
                    model.set_trigger_offset("RIGHT", event.value)

            #   Stick Event
            if event.type == 6:

                sentinel_value = True

                if event.stick == 0:
                    model.set_stick_position("LEFT", "X", event.x)
                    model.set_stick_position("LEFT", "Y", event.y)
                else:
                    model.set_stick_position("RIGHT", "X", event.x)
                    model.set_stick_position("RIGHT", "Y", event.y)

        #   Returns the modified xbox model
        if sentinel_value:
            return model.get_model()
        else:
            return None

    #   Take the newly modified model and forward it on.

    except xbox.XInputNotConnectedError:
        return None
