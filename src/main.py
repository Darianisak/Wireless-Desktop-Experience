import xbox_interface as interface
import XInput as xbox
import xbox_binds as fn
import action_interface as ai

def main_test():

    func = fn.XboxBinds()
    func.read_binds("E:\GitHub\Xbox-Remote-Script\src\conf.txt")

    action = ai.ActionInterface(func.current_profile)
    print(action.current_binds)

    end_message = False
    currently_pressed = set()

    print("\nWelcome to the Wireless Desktop Experience! Waiting for"
          " initial connection...")

    while True:

        while xbox.get_connected()[0]:
            #   Indentation level indicates functions associated with a connected
            #   controller

            if not end_message:
                print("\nController connection established!")
                end_message = True

            #   Gets all actions associated with the previous action cycle
            p_buttons, r_buttons, t_events, s_events = interface.get_current_events()

            #   TODO ~ There seem to be some issues with events not getting registered, or duplicated
            #   TODO ~ in the released list leading to set key errors

            #   <---    PROCESS ACTIONS     --->
            for pressed_button in p_buttons:
                currently_pressed.add(pressed_button)
                print("fuck 1", pressed_button)

            for released_button in r_buttons:
                currently_pressed.remove(released_button)
                print("fuck 2", released_button)

            for trigger_event in t_events:
                print("fuck 3", trigger_event)

            for stick_event in s_events:
                print("fuck 4", stick_event)
            #   <---    END OF PROCESSING   --->

        if end_message:
            print("\nController has been disconnected! Waiting for new connection...")
            print(currently_pressed)
            end_message = False




main_test()