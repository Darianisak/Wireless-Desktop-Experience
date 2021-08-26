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

    #   Sentinel values used to communicate connection information.
    connected = False
    disconnected = False
    print_sentinel = True

    #   x_offset and y_offset are storage variables used purely to store the current
    #   location of the cursor.
    x_offset = ms.get_position()[0]
    y_offset = ms.get_position()[1]

    #   List responsible for holding user config data
    user_config = []

    #   Loads user config file and applies values to relevant fields. In the
    #   advent that the required amount of arguments isn't loaded or the config
    #   file can not be found, the application will use the default values.
    try:

        #   Assuming no file errors, assign file specified values
        user_config = load_user_config()
        print("The userconfig.txt file had no errors! Loading user values...")
        assign_config(user_config)
    except FileNotFoundError:

        #   Assigns default values if the config file can't be found.
        print("The userconfig.txt file could not be found. Loading default values...")
        assign_defaults()
    except IndexError:

        #   Assigns default values if the config file doesn't have the required
        #   amount of data entries.
        assign_defaults()
        print("The userconfig.txt file did not contain the required 15 arguments. Loading default values...")

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

                global left_dead, right_dead
                xi.set_deadzone(xi.DEADZONE_LEFT_THUMB, left_dead)
                xi.set_deadzone(xi.DEADZONE_RIGHT_THUMB, right_dead)

                global x_sens, y_sens, x_bound, y_bound, x_accel, y_accel, x_screen, y_screen
                global zoom_lower, zoom_mid, zoom_upper, up_fill, left_fill, right_fill, down_fill
                global button_a, button_b, button_x, button_y, left_bumper, right_bumper, start_button
                global right_trigger, left_trigger

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
                            ms.click(button_a)

                        #   Handles events related to the 'B' Button.
                        if i.button == 'B':
                            ms.click(button_b)

                        #   Handles events related to the 'X' Button.
                        if i.button == 'X':
                            ms.click(button_x)

                        #   Handles events related to the 'Y' Button.
                        if i.button == 'Y':
                            kb.press(button_y)

                        #   Handles events tied to DPAD_UP
                        if i.button == "DPAD_UP":
                            kb.press_and_release(up_fill)

                        #   Handles events tied to DPAD_LEFT
                        if i.button == "DPAD_LEFT":
                            kb.press_and_release(left_fill)

                        #   Handles events tied to DPAD_RIGHT
                        if i.button == "DPAD_RIGHT":
                            kb.press_and_release(right_fill)

                        #   Handles events tied to DPAD_DOWN
                        if i.button == "DPAD_DOWN":
                            kb.press_and_release(down_fill)

                        #   Handles events tied to the left bumper.
                        if i.button == "LEFT_SHOULDER":
                            kb.press_and_release(left_bumper)

                        #   Handles events tied to the right bumper.
                        if i.button == "RIGHT_SHOULDER":
                            #   Used to create new web tabs
                            kb.press_and_release(right_bumper)

                        #   Handles events tied to START button.
                        if i.button == "START":
                            #   This function is only supported in IDE run mode.
                            kb.press_and_release(start_button)

                        #   Handles events tied to BACK button. This should not be rebound, as without it, the program
                        #   can't easily be closed.
                        if i.button == "BACK":
                            return

                    elif i.type == 5:

                        #   Handles events tied to the left trigger.
                        if i.trigger == 0:
                            if i.value == 1.0:
                                kb.press_and_release(left_trigger)

                        #   Handles events tied to the right trigger.
                        if i.trigger == 1:
                            if i.value == 1.0:
                                kb.press_and_release(right_trigger)

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
            except ValueError as msg:

                #   Used to gracefully handle errors stemming from users defining
                #   faulty config files.
                print("A text shortcut is improperly defined: " + str(msg))

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


#   assign_defaults is used to define controller variables in the advent that
#   the userconfig.txt file can not be found, or the user config file does not
#   contain the required amount of arguments.
def assign_defaults():

    global x_sens, y_sens, x_bound, y_bound, x_accel, y_accel, x_screen, y_screen
    global zoom_lower, zoom_mid, zoom_upper, up_fill, left_fill, right_fill, down_fill
    global button_a, button_b, button_x, button_y, left_bumper, right_bumper, start_button
    global right_trigger, left_trigger, left_dead, right_dead

    x_sens = 0.4
    y_sens = 0.4
    x_bound = 0.85
    y_bound = 0.85
    x_accel = 0.4
    y_accel = 0.4
    x_screen = 2560
    y_screen = 1440
    zoom_lower = 0.0085
    zoom_mid = 0.02
    zoom_upper = 0.04
    up_fill = 'n+e+t+f+l+i+x+.+c+o+m'
    left_fill = 'y+o+u+t+u+b+e+.+c+o+m'
    right_fill = 'd+i+s+c+o+r+d+.+c+o+m+/+l+o+g+i+n'
    down_fill = 'f+a+c+e+b+o+o+k+.+c+o+m'
    button_a = "left"
    button_b = "right"
    button_x = "middle"
    button_y = 'enter'
    left_bumper = 'ctrl+w'
    right_bumper = 'ctrl+t'
    start_button = 'windows'
    left_trigger = 'ctrl+-'
    right_trigger = 'ctrl+plus'
    left_dead = 1300
    right_dead = 1200


#   assign_config is used to define controller variables when the program is
#   supplied with a valid userconfig.txt file.
def assign_config(config_list):

    global x_sens, y_sens, x_bound, y_bound, x_accel, y_accel, x_screen, y_screen
    global zoom_lower, zoom_mid, zoom_upper, up_fill, left_fill, right_fill, down_fill
    global button_a, button_b, button_x, button_y, left_bumper, right_bumper, start_button
    global right_trigger, left_trigger, left_dead, right_dead

    x_sens = float(config_list[0])
    y_sens = float(config_list[1])
    x_bound = float(config_list[2])
    y_bound = float(config_list[3])
    x_accel = float(config_list[4])
    y_accel = float(config_list[5])
    x_screen = float(config_list[6])
    y_screen = float(config_list[7])
    zoom_lower = float(config_list[8])
    zoom_mid = float(config_list[9])
    zoom_upper = float(config_list[10])
    up_fill = config_list[11]
    left_fill = config_list[12]
    right_fill = config_list[13]
    down_fill = config_list[14]
    button_a = str(config_list[15])
    button_b = str(config_list[16])
    button_x = str(config_list[17])
    button_y = config_list[18]
    left_bumper = config_list[19]
    right_bumper = config_list[20]
    start_button = config_list[21]
    left_trigger = config_list[22]
    right_trigger = config_list[23]
    left_dead = int(config_list[24])
    right_dead = int(config_list[25])


#   <<< GLOBAL VARIABLES >>>    #

#   x_sens and y_sens are used to control the base sensitivity of the left
#   analog stick.
x_sens = 0
y_sens = 0

#   x_bound and y_bound are used to define boundary ranges for cursor
#   acceleration activation.
x_bound = 0
y_bound = 0

#   x_accel and y_accel are used to specify the speeds at which cursor acceleration
#   is implemented.
x_accel = 0
y_accel = 0

#   x_screen and y_screen are used to define screen space boundaries for mouse
#   control.
x_screen = 0
y_screen = 0

#   zoom_lower, zoom_mid, and zoom_upper are responsible for defining the stepping
#   rates for each boundary range; tied to the stick displacement value.
zoom_lower = 0
zoom_mid = 0
zoom_upper = 0

#   up_fill, left_fill, right_fill, down_fill are variables used by the DPAD to
#   to auto fill string entry forms.
up_fill = 0
left_fill = 0
right_fill = 0
down_fill = 0

#   button_a, button_b, button_x, button_y are variables used to bind different
#   functions to the controllers primary buttons.
button_a = 0
button_b = 0
button_x = 0
button_y = 0

#   left_bumper and right_bumper are variables used to bind shortcut keys to their
#   respective controller bumpers.
left_bumper = 0
right_bumper = 0

#   start_button is used to define shortcuts tied to the start button
start_button = 0

#   left_trigger and right_trigger are variables used to bind shortcuts to the
#   maximum displacement value of the triggers.
left_trigger = 0
right_trigger = 0

#   left_dead and right_dead are used to define the left and right stick
#   dead zones. These values should never really be dropped below 1200~1300
#   as any lower results in drastic levels of drag.
left_dead = 0
right_dead = 0


#   <<< PRIMARY LOGIC SEQUENCE >>>    #

main()

print("Application Terminated")

exit(0)
