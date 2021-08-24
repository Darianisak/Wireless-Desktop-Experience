import XInput as xi
import mouse as ms
import keyboard as kb
import math

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
    connected = False
    disconnected = False
    print_sentinel = True

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

    #   x_offset and y_offset are storage variables used purely to store the current
    #   location of the cursor.
    x_offset = 0
    y_offset = 0

    #   x_screen and y_screen are used to define screen space boundaries for mouse
    #   control.
    x_screen = 2560
    y_screen = 1440

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
                xi.set_deadzone(xi.DEADZONE_LEFT_THUMB, 1200)

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
                            #   TODO Needs to be refactored, maybe use TKinter? https://stackoverflow.com/questions/22519755/python-on-screen-keyboard
                            kb.press_and_release('windows+control+o')

                        #   Handles closing the application from the controller
                        if i.button == "BACK":
                            return

                #   Makes calls to cursor_update, which returns new mouse positional
                #   arguments.
                x_offset = cursor_update(x_screen, xi.get_thumb_values(xi.get_state(0))[0][0], x_offset, x_sens,
                                         x_accel, x_bound)
                y_offset = cursor_update(y_screen, -xi.get_thumb_values(xi.get_state(0))[0][1], y_offset, y_sens,
                                         y_accel, y_bound)

                #   Moves the cursor, according to the thumb sticks.
                ms.move(x_offset, y_offset, True, 0)

                #   Moves the scroll wheel, according to the right thumb stick.
                ms.wheel(xi.get_thumb_values(xi.get_state(0))[1][1] / 100)

            except xi.XInputNotConnectedError:
                continue

        #   Updates sentinel values so that appropriate output is printed. This
        #   only occurs if a connection has been made prior.
        if connected:
            disconnected = True
            connected = False


#   Determining the value by which the mouse should be moved is a common operation,
#   so cursor_update is intended to reduce unneeded code.
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


main()

print("Application Terminated")

exit(0)
