import xbox_interface as interface
import XInput as xbox


def main_test():

    while True:

        print("Waiting for connection...")
        interface.set_vibration_strength("LEFT", 1500)
        interface.set_vibration_strength("RIGHT", 1500)

        while xbox.get_connected()[0]:

            event_dict = interface.read_controller()
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