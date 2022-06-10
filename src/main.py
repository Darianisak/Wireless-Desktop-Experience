import xbox_interface as interface
import XInput as xbox
import xbox_functions as fn

def main_test():

    func = fn.XboxFunctions()
    func.read_binds("E:\GitHub\Xbox-Remote-Script\src\conf.txt")
    return

    while True:

        print("Waiting for connection...")

        while xbox.get_connected()[0]:

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



main_test()