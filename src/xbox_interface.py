import xbox_model as model
import XInput as xbox

#   xbox_interface is responsible for receiving controller events, adjusting
#   the model, and returning information appropriately

#   todo reformat so read controller just returns a model - it's not a loop
#   todo add fields so that dead zones can be checked and validated prior to run
#   todo of read_controller func. Means that this file is more decoupled if it
#   is just responsible for returning instead of forwarding.

#   interface_preference is responsible for storing user preferences with regard
#   to the controller experience. For rumble_strength, any value greater than 0
#   will lead to the motor being activated
interface_preferences = {
    #   Defines stick dead zones - max 32767, min 0
    "dead_zone_left_stick": 7849,
    "dead_zone_right_stick": 8689,

    #   Defines trigger dead zones - max 255, min 0
    "dead_zone_triggers": 30,

    #   Define rumble speed - max 65535, min 0
    "rumble_strength_left": 0,
    "rumble_strength_right": 0
}


#   TODO Write tests
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

    #   TODO refactor so dead zones are applied here, not set to some dictionary - that's just inefficient

    global interface_preferences

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
                            interface_preferences["dead_zone_left_stick"] = value
                        case "RIGHT":
                            interface_preferences["dead_zone_right_stick"] = value
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
                            interface_preferences["rumble_strength_left"] = value
                        case "RIGHT":
                            #   Applies rumble strength for the right motor
                            interface_preferences["rumble_strength_right"] = value
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
                    interface_preferences["dead_zone_triggers"] = value
            case _:
                raise ValueError("Raised by Xbox_interface.set_preference(pref, modifier, value)"
                                 "\n'pref' was " + str(pref))
    else:
        raise TypeError("Raised Xbox_interface.set_preference(pref, modifier, value)"
                        "\n'value' was not of type int, was " + str(type(value)))


#   TODO Write tests - maybe just refactor so
#   get_preference is used to retrieve a specific preference.
#
#   pref     : Type String
#   modifier : Type String
#   return   : Type Int
#   error    : ValueError is raised when either pref or modifier are invalid
def get_preference(pref, modifier):

    global interface_preferences

    match pref:
        case "STICK":
            match modifier:
                case "LEFT":
                    return interface_preferences["dead_zone_left_trigger"]
                case "RIGHT":
                    return interface_preferences["dead_zone_right_trigger"]
                case _:
                    raise ValueError("Raised by Xbox_interface.get_preference(pref, modifier)"
                                     "\n'modifier' was " + str(modifier))
        case "RUMBLE":
            match modifier:
                case "LEFT":
                    return interface_preferences["rumble_strength_left"]
                case "RIGHT":
                    return interface_preferences["rumble_strength_right"]
                case _:
                    raise ValueError("Raised by Xbox_interface.get_preference(pref, modifier)"
                                     "\n'modifier' was " + str(modifier))
        case "TRIGGERS":
            return interface_preferences["dead_zone_triggers"]
        case _:
            raise ValueError("Raised by Xbox_interface.get_preference(pref, modifier)"
                             "\n'pref' was " + str(pref))


#   todo
def get_battery():
    print("1")


# todo
def cause_vibration():
    print("1")


#   read_controller is responsible for pulling in new event information, and
#   performing appropriate actions on said information. This function will
#   return if no controller is connected
def read_controller():
    current_event = xbox.get_events()

    #   Used to catch errors in the advent of a controller disconnect
    try:
        for event in current_event:

            #   Button Press
            if event.type == 3:
                model.set_button_status(event.button, True)

            #   Button Release
            if event.type == 4:
                model.set_button_status(event.button, False)

            #   Trigger Event
            if event.type == 5:
                print("1")
                #   todo
                #   Causes a vibration
                xbox.set_vibration(0, 1500, 0)

            #   Stick Event
            if event.type == 6:
                # todo
                print("sticks")

        #   Returns the modified xbox model
        return model.get_model()

    #   Take the newly modified model and forward it on.

    except xbox.XInputNotConnectedError:
        return


#   Test code
while True:
    read_controller()
