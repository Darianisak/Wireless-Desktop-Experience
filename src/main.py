import xbox_interface as interface
import XInput as xbox
import xbox_binds as fn

def main_test():

    func = fn.XboxBinds()
    func.read_binds("E:\GitHub\Xbox-Remote-Script\src\conf.txt")

    start_message = False
    end_message = False

    print("\nWelcome to the Wireless Desktop Experience! Waiting for"
          " initial connection...")

    while True:

        while xbox.get_connected()[0]:

            if not end_message:
                print("\nController connection established!")
                end_message = True

            event_dict = interface.read_controller()
            print(event_dict)

            if not isinstance(event_dict, type(None)):
                if event_dict["pressed_button_a"]:
                    print("right on")
                    print(str(interface.get_battery()) + " type " + str(type(interface.get_battery())))
                elif event_dict["pressed_button_x"]:
                    print("right off")

                    interface.toggle_vibration("RIGHT")
                if event_dict["pressed_button_b"]:
                    print("left")

                    interface.toggle_vibration("LEFT")
                elif event_dict["pressed_button_y"]:
                    print("left")

                    interface.toggle_vibration("LEFT")

        if end_message:
            print("\nController has been disconnected! Waiting for new connection...")
            end_message = False


main_test()