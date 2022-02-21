import xbox_model as model
import XInput as xbox

#   xbox_interface is responsible for receiving controller events, adjusting
#   the model, and forwarding information appropriately


#   read_controller is responsible for pulling in new event information, and
#   performing appropriate actions on said information. This function will
#   return if no controller is connected
def read_controller():

    #   Validates that a controller is connected
    while xbox.get_connected()[0]:

        current_event = xbox.get_events()

        #   Try bracket takes new events and modifies the xbox model
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
                    xbox.set_vibration(0,1500, 0)

                #   Stick Event
                if event.type == 6:
                    #todo
                    print("sticks")

        #   Take the newly modified model and forward it on.

        except xbox.XInputNotConnectedError:
            continue


#   update_dead_zone is a setter method for changing the dead_zone activation
#   minimum during runtime
def update_dead_zone(region, amount):
    print("1")
    #   todo
    #triggers, both sticks

def get_battery():
    print("1")
    #   todo

def set_vibration():
    print("1")
    #   todo

def cause_vibration():
    print("1")
    #   todo

#   Test code
while True:
    read_controller()

