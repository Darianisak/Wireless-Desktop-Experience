from src import xbox_model as model
import XInput as xbox

#   xbox_interface is responsible for receiving controller events, adjusting
#   the model, and returning information appropriately

#   Controller Preference Setters
#   Each setter works in a slightly different way, or adheres to different
#   boundaries, which means that for readability sake, breaking them into
#   individual setters works best.


#   set_trigger_dead is used to apply dead zones to both triggers. Dead zones
#   work by preventing event generation until the trigger has been moved beyond
#   a border - the dead zone. Unlike the vibration motors, dead zones can be
#   applied immediately
#   value  : Type int
#   return : None
#   error  : TypeError when value is not of type int
#   error  : ValueError when value exceeds the boundaries
def set_trigger_dead(value):

    if isinstance(value, int) and not isinstance(value, bool):
        if 0 <= value <= 255:
            xbox.set_deadzone(xbox.DEADZONE_TRIGGER, value)
        else:
            raise ValueError("Raised by Xbox_interface.set_trigger_dead(value)"
                             "'value' was out of bounds - must be between 0 and 255 inclusive")
    else:
        raise TypeError("Raised by Xbox_interface.set_trigger_dead(value)"
                        "\n'value' was not of type int, was " + str(type(value)))


#   set_stick_dead is used to apply dead zones to a controller thumb stick.
#   Dead zones work by preventing event generation until the stick has been
#   moved beyond a border - the dead zone. Unlike with the vibration motors,
#   dead zones can be applied immediately
#   side   : Type String
#   value  : Type int - min 0, max 32767 inclusive
#   return : None
#   error  : TypeError when value is not of type int
#   error  : ValueError when side is invalid or value exceeds the boundaries
def set_stick_dead(side, value):

    if isinstance(value, int) and not isinstance(value, bool):
        if 0 <= value <= 32767:
            match side:
                case "LEFT":
                    xbox.set_deadzone(xbox.DEADZONE_LEFT_THUMB, value)
                case "RIGHT":
                    xbox.set_deadzone(xbox.DEADZONE_RIGHT_THUMB, value)
                case _:
                    raise ValueError("Raised by Xbox_interface.set_stick_dead(side, amount)"
                                     "\n'side' was not valid - must be LEFT or RIGHT")
        else:
            raise ValueError("Raised by Xbox_interface.set_stick_dead(side, amount)"
                             "\n'value' was out of bounds - must be between 0 and 32767 inclusive.")
    else:
        raise TypeError("Raised by Xbox_interface.set_stick_dead(side, amount)"
                        "\n'value' was not of type int, was " + str(type(value)))


#   Used to manage the state of the controllers rumble motors

motor_detail = {
    #   Define rumble speed - max 65535, min 0
    "left_strength": 0,
    "right_strength": 0,
    "left_active": False,
    "right_active": False
}


#   set_vibration_strength is used to update the motor_detail dictionary, which
#   in turn, is used to dictate how fast the controller motors operate. Unlike
#   with the dead zones, vibration values are not immediately applied to the
#   motors - doing so would cause the motors to be locked on.
#
#   side   : Type String - either LEFT or RIGHT
#   value  : Type int - min 0, max 65535 inclusive
#   return : None
#   error  : TypeError is raised if the type value is not int
#   error  : ValueError is raised if side is invalid or value exceeds the bounds
def set_vibration_strength(side, value):

    global motor_detail

    if isinstance(value, int) and not isinstance(value, bool):
        if 0 <= value <= 65535:
            match side:
                case "LEFT":
                    motor_detail["left_strength"] = value
                case "RIGHT":
                    motor_detail["right_strength"] = value
                case _:
                    raise ValueError("Raised by Xbox_interface.set_vibration_strength(side, value)"
                                     "\n'side' was invalid - must be LEFT or RIGHT")
        else:
            raise ValueError("Raised by Xbox_interface.set_vibration_strength(side, value)"
                             "\n'value' was out of bounds - must be between 0 and 65535 inclusive")
    else:
        raise TypeError("Raised by Xbox_interface.set_vibration_strength(side, value)"
                        "\n'value' was not of type int, was " + str(type(value)))


#   Controller Utility Functions

#   get_battery returns the information available for the controller battery
#   Personally, I can't see any use for this - it doesn't give enough information
#   to be of any use.
#
#   return : Type Tuple - (String: Battery Type, e.g. Alkaline; String Level, e.g.
#                         medium)
def get_battery():
    return xbox.get_battery_information(0)


#   toggle_vibration is used to switch the rumble motors on and off. The system
#   refers to the motor_detail dictionary to determine which motors are on,
#   which enables a dynamic vibration model where both, one, or no motors can
#   run at once.
#
#   side   : Type String
#   return : None
#   error  : ValueError is raised when side is invalid
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


#   Controller Logic Segment

#   read_controller is responsible for pulling in new event information, and
#   performing appropriate actions on said information. Information is
#   communicated to the main process via a return - these only happen when new
#   information has been recorded so as to avoid event 'spam'
#
#   return : In the case of an event, return the controller model (type: dict),
#            Otherwise, return None
#   error  : XInputNotConnectedError is raised if the active controller is
#            disconnected during operation
#   error  : ConnectionError is raised immediately following an XInputNotConnectedError
#            to feedback to the main program loop that the controller is no
#            longer connected and it should revert to 'discovery' mode
def read_controller():

    #   Sentinel value that prevents needless event logging
    an_event_occurred = False

    current_event = xbox.get_events()

    #   Used to catch errors in the advent of a controller disconnect
    try:
        for event in current_event:

            #   Button Press
            if event.type == 3:

                an_event_occurred = True
                model.set_button_status(event.button, True)

            #   Button Release
            if event.type == 4:

                an_event_occurred = True
                model.set_button_status(event.button, False)

            #   Trigger Event
            if event.type == 5:

                an_event_occurred = True

                if event.trigger == 0:
                    model.set_trigger_offset("LEFT", event.value)
                else:
                    model.set_trigger_offset("RIGHT", event.value)

            #   Stick Event
            if event.type == 6:

                an_event_occurred = True

                if event.stick == 0:
                    model.set_stick_position("LEFT", "X", event.x)
                    model.set_stick_position("LEFT", "Y", event.y)
                else:
                    model.set_stick_position("RIGHT", "X", event.x)
                    model.set_stick_position("RIGHT", "Y", event.y)

        if an_event_occurred:

            #   In the case of a new event - return the controller model
            return model.get_model()
        else:
            #   No event was generated this cycle - do not return the model
            return None

    except xbox.XInputNotConnectedError:

        #   It's not appropriate to return a None value in the case of a
        #   controller disconnect, so relay that the controller is not active
        raise ConnectionError("Controller has been disconnected!")
