import XInput as xi
import mouse as ms
import keyboard as kb

#   https://www.thepythoncode.com/article/control-mouse-python
#   https://pypi.org/project/XInput-Python/

#   The purpose of this application is to provide universal Windows support
#   for controller based user interaction, i.e. using controllers to browse
#   the web, pause netflix, or in advanced cases, act as a proper controller
#   emulator for video games that lack controller support.


#   Main is the primary application loop and consists of an always active
#   while loop. This loop is only exited on application close events, with
#   the assumption being that if you have the application open, you're either
#   using a controller, or about to connect one.
def main():

    #   List responsible for holding user config data
    user_config = []

    #   Loads user config file and applies values to relevant fields. In the
    #   advent that the required amount of arguments isn't loaded or the config
    #   file can not be found, the application will use the default values.
    try:
        user_config = load_user_config()
    except FileNotFoundError:

        #   Assigns default values if the config file can't be found.
        assign_defaults()
    except IndexError:

        #   Assigns default values if the config file doesn't have the required
        #   amount of data entries.
        assign_defaults()

    #   Sentinel values used to communicate connection information.
    connected = False
    disconnected = False
    print_sentinel = True

    #   x_offset and y_offset are storage variables used purely to store the current
    #   location of the cursor.
    x_offset = 0
    y_offset = 0

    #   x_sens and y_sens are used to control the base sensitivity of the left
    #   analog stick.
    x_sens = 0.4
    y_sens = 0.4

    #   x_bound and y_bound are used to define boundary ranges for cursor
    #   acceleration activation.
    x_bound = 0.85
    y_bound = 0.85

    #   x_accel and y_accel are used to specify the speeds at which cursor acceleration
    #   is implemented.
    x_accel = 0.4
    y_accel = 0.4

    #   x_screen and y_screen are used to define screen space boundaries for mouse
    #   control.
    x_screen = 2560
    y_screen = 1440

    #   zoom_lower, zoom_mid, and zoom_upper are responsible for defining the stepping
    #   rates for each boundary range; tied to the stick displacement value.
    zoom_lower = 0.0085
    zoom_mid = 0.02
    zoom_upper = 0.04

    #   Primary "Discovery" Loop.
    while True:

        #   Communication conditionals that communicate the current application
        #   to controller connection status, specifically, when searching for
        #   connections.
        if not connected and print_sentinel:
            if disconnected:
                print("Connection Terminated!\n")
                disconnected = True
            print("Checking For Connections...")
            print_sentinel = False

        #   Primary "Action" loop. Index 0 corresponds to Xbox controllers;
        #   I have no idea what the other indices correspond to.
        while xi.get_connected()[0]:
            #   Updates the event generator log; sort of like an input buffer
            events = xi.get_events()

            #   Conditional that communicates that a connection has been
            #   established, while also flipping the previously established
            #   print_sentinel value for use in case of a disconnect.
            if not print_sentinel:
                print("Connection Established!")
                print_sentinel = True
                connected = True
                x_offset = ms.get_position()[0]
                y_offset = ms.get_position()[1]

                #   Sets the deadzone value for the left stick. The default deadzone
                #   is 7489, and anything below 1000 is intolerable in terms of drag.
                xi.set_deadzone(xi.DEADZONE_LEFT_THUMB, 1300)
                xi.set_deadzone(xi.DEADZONE_RIGHT_THUMB, 1200)

            #   Logic Segment

            #   In the event of a disconnect, the XInput library raises the
            #   XInputNotConnectedError. This exception handling lets users just
            #   reconnect their controller without too much fuss.
            try:

                #   Iterates through the event generator. This is used to handle
                #   events relating to button presses.
                for i in events:

                    #   Determines if the event was a button press, in which case
                    #   it has the button member, which returns a representation
                    #   of the pressed button
                    if i.type == 3:

                        #   Handles events related to the 'A' Button.
                        if i.button == 'A':
                            ms.click("left")

                        #   Handles events related to the 'B' Button.
                        if i.button == 'B':
                            ms.click("right")

                        #   Handles events related to the 'X' Button.
                        if i.button == 'X':
                            ms.click("middle")

                        #   Handles events related to the 'Y' Button.
                        if i.button == 'Y':
                            kb.press('enter')

                        #   Handles events tied to DPAD_UP
                        if i.button == "DPAD_UP":
                            kb.press_and_release('n+e+t+f+l+i+x+.+c+o+m')

                        #   Handles events tied to DPAD_LEFT
                        if i.button == "DPAD_LEFT":
                            kb.press_and_release('f+a+c+e, b+o+o+k+.+c+o+m')

                        #   Handles events tied to DPAD_RIGHT
                        if i.button == "DPAD_RIGHT":
                            kb.press_and_release('d+i+s+c+o+r+d+.+c+o+m+/+l+o+g+i+n')

                        #   Handles events tied to DPAD_DOWN
                        if i.button == "DPAD_DOWN":
                            kb.press_and_release('y+o+u+t+u+b+e+.+c+o+m')

                        #   Handles events tied to the left bumper.
                        if i.button == "LEFT_SHOULDER":
                            kb.press_and_release('space, ctrl+w')

                        #   Handles events tied to the right bumper.
                        if i.button == "RIGHT_SHOULDER":
                            #   Used to create new web tabs
                            kb.press_and_release('space, ctrl+t')

                        #   Handles events tied to START button.
                        if i.button == "START":
                            #   This function is only supported in IDE run mode.
                            kb.press_and_release('shift+f10')

                        #   Handles events tied to BACK button.
                        if i.button == "BACK":
                            return

                    elif i.type == 5:

                        #   Handles events tied to the left trigger.
                        if i.trigger == 0:
                            if i.value == 1.0:
                                kb.press_and_release('ctrl+-')

                        #   Handles events tied to the right trigger.
                        if i.trigger == 1:
                            if i.value == 1.0:
                                kb.press_and_release('ctrl+plus')

                #   Makes calls to cursor_update, which returns new mouse positional
                #   arguments.
                x_offset = cursor_update(x_screen, xi.get_thumb_values(xi.get_state(0))[0][0], x_offset, x_sens,
                                         x_accel, x_bound)
                y_offset = cursor_update(y_screen, -xi.get_thumb_values(xi.get_state(0))[0][1], y_offset, y_sens,
                                         y_accel, y_bound)

                #   Moves the cursor, according to the thumb sticks.
                ms.move(x_offset, y_offset, True, 0)

                #   Makes call to wheel_update as a means of determining which
                #   step 'speed' should be applied to the active scrolling.
                ms.wheel(wheel_update(xi.get_thumb_values(xi.get_state(0))[1][1], zoom_lower, zoom_mid, zoom_upper))

            except xi.XInputNotConnectedError:
                continue

        #   Updates sentinel values so that appropriate output is printed. This
        #   only occurs if a connection has been made prior.
        if connected:
            disconnected = True
            connected = False


#   Determining the value by which the mouse should be moved is a common operation,
#   so cursor_update is intended to reduce unneeded code. This function returns numeric
#   displacement values.
#
#   Params
#   screen_max  :   defines the maximum value that the screen reaches on this axis.
#   stick_value :   is the value of displacement of the stick.
#   offset      :   is the position of the cursor on the screen for the axis.
#   sens        :   is the base sensitivity value of the axis.
#   accel       :   is the factor by which acceleration is applied.
#   bound       :   is the boundary at which acceleration is applied.
def cursor_update(screen_max, stick_value, offset, sens, accel, bound):

    #   Default case whereby the current offset is equivalent to the screen_max
    #   or screen min value, 0, so just return the current offset
    if offset < 0:
        #   This return is mindful that problems can arise, so should return
        #   the lowest actual possible value, which may not be the current offset.
        return 0
    elif offset > screen_max:
        #   Likewise, this is mindful that offset could be beyond the actual max.
        return screen_max

    #   Primary calculation step - bounds checking is already performed so doesn't
    #   recheck
    if abs(stick_value) > bound:
        return offset + (stick_value * (sens + accel))
    else:
        return offset + (stick_value * sens)


#   wheel_update is a function definition primarily used to reduce code clutter
#   within main. This function doesn't update the mouse wheel directly, it just
#   computes the step value and returns it.
#
#   Params
#   stick_value     :   is the value displacement of the sticks y axis.
#   lower           :   is the scroll rate for the lower bound.
#   mid             :   is the scroll rate for the mid bound.
#   upper           :   is the scroll rate for the upper bound.
def wheel_update(stick_value, lower, mid, upper):

    if 0.2 <= abs(stick_value) < 0.4:
        if stick_value > 0:
            return lower
        else:
            return -lower
    elif 0.4 <= abs(stick_value) < 0.9:
        if stick_value > 0:
            return mid
        else:
            return -mid
    elif 0.9 <= abs(stick_value) <= 1.0:
        if stick_value > 0:
            return upper
        else:
            return -upper
    else:
        return 0


#   load_user_config is a function definition used to load in user configuration
#   files. This allows for more accessible application use by non programmers.
def load_user_config():

    config = []

    #   Loads raw text file into list
    with open('userconfig.txt') as cfg:
        config = cfg.readlines()
        cfg.close()

    tmp = []

    #   Cleans out hashed lines.
    for index in config:
        if index[0] != "#":
            tmp.append(index)

    pre_return = []

    #   Cleans "\n" characters from entries
    for index in tmp:
        pre_return.append(index[0:len(index) - 1])

    return_list = []

    #   Removes zero length indices from the list
    for index in pre_return:
        if len(index) != 0:
            return_list.append(index)

    if len(return_list) != 15:
        raise IndexError()

    #   Returns the processed list
    return return_list


def assign_defaults():
    print("assign defaults")


main()

print("Application Terminated")

exit(0)
