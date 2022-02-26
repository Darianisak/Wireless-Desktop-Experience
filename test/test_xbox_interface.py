from src import xbox_interface as xi
import XInput as xbox
import unittest


#   With the exception of read_controller, which relies on a live controller,
#   and get_battery, which also relies on a live controller, this test suite
#   validates the functionality of the xbox_interface file. When running tests
#   in this file, it is important that a controller is NOT connected concurrently.
#   As the suite is designed without a controller connection in mind, a connection
#   may cause the tests to behave unexpectedly
class TestXboxInterface(unittest.TestCase):

    #   DO NOT TEST WITH CONTROLLER CONNECTED
    #
    #   test_trigger_setter checks valid and invalid input arguments for the
    #   trigger dead zone setter function. Valid inputs may raise an exception
    #   regarding a disconnected controller, whereas invalid ones will raise either
    #   type or value errors
    def test_trigger_setter(self):

        #   Tests valid inputs.
        try:
            xi.set_trigger_dead(0)
            xi.set_trigger_dead(125)
            xi.set_trigger_dead(255)

        except ValueError:
            self.fail("Unexpected ValueError raised during test_trigger_setter")
        except TypeError:
            self.fail("Unexpected TypeError raised during test_trigger_setter")
        except xbox.XInputNotConnectedError:
            self.assertTrue(True)

        #   Tests out of bound values
        with self.assertRaises(ValueError):
            xi.set_trigger_dead(-1)

        with self.assertRaises(ValueError):
            xi.set_trigger_dead(256)

        #   Tests invalid data types
        with self.assertRaises(TypeError):
            xi.set_trigger_dead(0.0)

        with self.assertRaises(TypeError):
            xi.set_trigger_dead(255.0)

        with self.assertRaises(TypeError):
            xi.set_trigger_dead(125.0)

        with self.assertRaises(TypeError):
            xi.set_trigger_dead("X")

        #   Integrate this into to other tests
        with self.assertRaises(TypeError):
            xi.set_trigger_dead(True)

        with self.assertRaises(TypeError):
            xi.set_trigger_dead(False)

        with self.assertRaises(TypeError):
            xi.set_trigger_dead(None)

    #   DO NOT TEST WITH CONTROLLER CONNECTED
    #
    #   test_stick_dead checks valid and invalid input arguments for the thumb
    #   stick dead zone setter function. Valid inputs may raise an exception
    #   regarding a disconnected controller, whereas invalid ones will raise
    #   either type or value errors
    def test_stick_dead(self):

        #   Tests valid inputs
        try:
            xi.set_stick_dead("LEFT", 0)
            xi.set_stick_dead("LEFT", 16383)
            xi.set_stick_dead("LEFT", 32767)

            xi.set_stick_dead("RIGHT", 0)
            xi.set_stick_dead("RIGHT", 16383)
            xi.set_stick_dead("RIGHT", 32767)

        except ValueError:
            self.fail("Unexpected ValueError raised during test_trigger_setter")
        except TypeError:
            self.fail("Unexpected TypeError raised during test_trigger_setter")
        except xbox.XInputNotConnectedError:
            self.assertTrue(True)

        #   Tests out of bounds values
        with self.assertRaises(ValueError):
            xi.set_stick_dead("LEFT", -1)

        with self.assertRaises(ValueError):
            xi.set_stick_dead("LEFT", 32768)

        with self.assertRaises(ValueError):
            xi.set_stick_dead("RIGHT", -1)

        with self.assertRaises(ValueError):
            xi.set_stick_dead("RIGHT", 32768)

        #   Tests invalid data types - LEFT
        with self.assertRaises(TypeError):
            xi.set_stick_dead("LEFT", 0.0)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("LEFT", 16383.0)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("LEFT", 32767.0)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("LEFT", "X")

        with self.assertRaises(TypeError):
            xi.set_stick_dead("LEFT", True)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("LEFT", False)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("LEFT", None)

        #   Tests invalid data types - RIGHT
        with self.assertRaises(TypeError):
            xi.set_stick_dead("RIGHT", 0.0)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("RIGHT", 16383.0)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("RIGHT", 32767.0)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("RIGHT", "X")

        with self.assertRaises(TypeError):
            xi.set_stick_dead("RIGHT", True)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("RIGHT", False)

        with self.assertRaises(TypeError):
            xi.set_stick_dead("RIGHT", None)

        #   Invalid side arg
        with self.assertRaises(ValueError):
            xi.set_stick_dead(1, 255)

        with self.assertRaises(ValueError):
            xi.set_stick_dead(1.0, 255)

        with self.assertRaises(ValueError):
            xi.set_stick_dead("X", 255)

        with self.assertRaises(ValueError):
            xi.set_stick_dead(False, 255)

        with self.assertRaises(ValueError):
            xi.set_stick_dead(True, 255)

        with self.assertRaises(ValueError):
            xi.set_stick_dead(None, 255)

        with self.assertRaises(ValueError):
            xi.set_stick_dead("left", 255)

        with self.assertRaises(ValueError):
            xi.set_stick_dead("right", 255)

    #   DO NOT TEST WITH CONTROLLER CONNECTED
    #
    #   test_set_vibration checks valid and invalid input arguments for the
    #   left and right motor strengths. Valid inputs may raise an exception
    #   regarding a disconnected controller, whereas invalid ones will raise
    #   either type or value errors
    def test_set_vibration(self):

        #   Tests valid inputs
        try:
            xi.set_vibration_strength("LEFT", 0)
            xi.set_vibration_strength("LEFT", 32767)
            xi.set_vibration_strength("LEFT", 65535)

            xi.set_vibration_strength("RIGHT", 0)
            xi.set_vibration_strength("RIGHT", 32767)
            xi.set_vibration_strength("RIGHT", 65535)

        except ValueError:
            self.fail("Unexpected ValueError raised during test_trigger_setter")
        except TypeError:
            self.fail("Unexpected TypeError raised during test_trigger_setter")
        except xbox.XInputNotConnectedError:
            self.assertTrue(True)

        #   Tests out of boundary values
        with self.assertRaises(ValueError):
            xi.set_vibration_strength("LEFT", -1)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength("LEFT", 65536)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength("RIGHT", -1)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength("RIGHT", 65536)

        #   Tests invalid value data types - LEFT
        with self.assertRaises(TypeError):
            xi.set_vibration_strength("LEFT", 0.0)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("LEFT", 32767.0)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("LEFT", 65535.0)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("LEFT", "X")

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("LEFT", True)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("LEFT", False)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("LEFT", None)

        #   Tests invalid value data types - RIGHT
        with self.assertRaises(TypeError):
            xi.set_vibration_strength("RIGHT", 0.0)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("RIGHT", 32767.0)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("RIGHT", 65535.0)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("RIGHT", "X")

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("RIGHT", True)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("RIGHT", False)

        with self.assertRaises(TypeError):
            xi.set_vibration_strength("RIGHT", None)

        #   Tests invalid side args
        with self.assertRaises(ValueError):
            xi.set_vibration_strength(1, 255)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength(1.0, 255)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength("X", 255)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength(False, 255)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength(True, 255)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength(None, 255)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength("left", 255)

        with self.assertRaises(ValueError):
            xi.set_vibration_strength("right", 255)

    #   DO NOT TEST WITH CONTROLLER CONNECTED
    #
    #   test_toggle_vibration checks valid and invalid input for the
    #   vibration toggle function. Valid inputs may raise an exception regarding
    #   a disconnected controller, whereas invalid ones will raise a value error
    def test_toggle_vibration(self):

        #   Valid tests - done in control flow order of the tested function

        #   Left Branch
        #   L, R -> !L, R
        xi.motor_detail["left_active"] = True
        xi.motor_detail["right_active"] = True
        xi.toggle_vibration("LEFT")
        self.assertFalse(xi.motor_detail["left_active"])
        self.assertTrue(xi.motor_detail["right_active"])

        #   L, !R -> !L, !R
        xi.motor_detail["left_active"] = True
        xi.motor_detail["right_active"] = False
        xi.toggle_vibration("LEFT")
        self.assertFalse(xi.motor_detail["left_active"])
        self.assertFalse(xi.motor_detail["right_active"])

        #   !L, R -> L, R
        xi.motor_detail["left_active"] = False
        xi.motor_detail["right_active"] = True
        xi.toggle_vibration("LEFT")
        self.assertTrue(xi.motor_detail["left_active"])
        self.assertTrue(xi.motor_detail["right_active"])

        #   !L, !R -> L, !R
        xi.motor_detail["left_active"] = False
        xi.motor_detail["right_active"] = False
        xi.toggle_vibration("LEFT")
        self.assertTrue(xi.motor_detail["left_active"])
        self.assertFalse(xi.motor_detail["right_active"])

        #   Right Branch
        #   L, R -> L, !R
        xi.motor_detail["left_active"] = True
        xi.motor_detail["right_active"] = True
        xi.toggle_vibration("RIGHT")
        self.assertTrue(xi.motor_detail["left_active"])
        self.assertFalse(xi.motor_detail["right_active"])

        #   !L, R -> !L, !R
        xi.motor_detail["left_active"] = False
        xi.motor_detail["right_active"] = True
        xi.toggle_vibration("RIGHT")
        self.assertFalse(xi.motor_detail["left_active"])
        self.assertFalse(xi.motor_detail["right_active"])

        #   L, !R -> L, R
        xi.motor_detail["left_active"] = True
        xi.motor_detail["right_active"] = False
        xi.toggle_vibration("RIGHT")
        self.assertTrue(xi.motor_detail["left_active"])
        self.assertTrue(xi.motor_detail["right_active"])

        #   !L, !R -> !L, R
        xi.motor_detail["left_active"] = False
        xi.motor_detail["right_active"] = False
        xi.toggle_vibration("RIGHT")
        self.assertFalse(xi.motor_detail["left_active"])
        self.assertTrue(xi.motor_detail["right_active"])

        #   Tests invalid side args
        with self.assertRaises(ValueError):
            xi.toggle_vibration(1)

        with self.assertRaises(ValueError):
            xi.toggle_vibration(False)

        with self.assertRaises(ValueError):
            xi.toggle_vibration(True)

        with self.assertRaises(ValueError):
            xi.toggle_vibration(None)

        with self.assertRaises(ValueError):
            xi.toggle_vibration("left")

        with self.assertRaises(ValueError):
            xi.toggle_vibration("right")
