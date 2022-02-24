from src import xbox_model as xm
import unittest


class TestXboxModel(unittest.TestCase):

    #   test_default_returns verifies that default variables have not been
    #   modified. As a rule, all default values will be either 'False' or 0.00
    def test_default_returns(self):

        print("Running test_xbox_model -> test_default_returns...")

        #   Resets all values to defaults - seems to be essential to avoiding
        #   out of order script runs causing problems.
        xm.reset_model()

        #   Checks Button Defaults
        self.assertFalse(xm.get_button_status("A"))
        self.assertFalse(xm.get_button_status("B"))
        self.assertFalse(xm.get_button_status("X"))
        self.assertFalse(xm.get_button_status("Y"))

        #   Checks Shoulder Defaults
        self.assertFalse(xm.get_button_status("LEFT_SHOULDER"))
        self.assertFalse(xm.get_button_status("RIGHT_SHOULDER"))

        #   Checks DPAD Defaults
        self.assertFalse(xm.get_button_status("DPAD_LEFT"))
        self.assertFalse(xm.get_button_status("DPAD_RIGHT"))
        self.assertFalse(xm.get_button_status("DPAD_UP"))
        self.assertFalse(xm.get_button_status("DPAD_DOWN"))

        #   Checks Option Defaults
        self.assertFalse(xm.get_button_status("BACK"))
        self.assertFalse(xm.get_button_status("START"))

        #   Checks Stick-Click Defaults
        self.assertFalse(xm.get_button_status("LEFT_THUMB"))
        self.assertFalse(xm.get_button_status("RIGHT_THUMB"))

        #   Checks Trigger Defaults
        self.assertFalse(xm.is_trigger_offset("LEFT"))
        self.assertFalse(xm.is_trigger_offset("RIGHT"))

        self.assertEqual(xm.get_offset_amount("LEFT"), 0.00)
        self.assertEqual(xm.get_offset_amount("RIGHT"), 0.00)

        #   Checks Stick Defaults
        self.assertEqual(xm.get_stick_position("LEFT", "X"), 0.00)
        self.assertEqual(xm.get_stick_position("LEFT", "Y"), 0.00)
        self.assertEqual(xm.get_stick_position("RIGHT", "X"), 0.00)
        self.assertEqual(xm.get_stick_position("RIGHT", "Y"), 0.00)

        print("Finished test_xbox_model -> test_default_returns!")

    #   test_normal validates that setter functions are performing
    #   as expected in normal circumstance. E.g. all relevant setters will
    #   toggle from False (prior test) to True, or that the trigger offsets
    #   can be toggled to 0.5, etc.
    def test_normal(self):

        print("Running test_xbox_model -> test_normal_boundary...")

        #   Checks Primary Buttons
        xm.set_button_status("A", True)
        xm.set_button_status("B", True)
        xm.set_button_status("X", True)
        xm.set_button_status("Y", True)

        self.assertTrue(xm.get_button_status("A"))
        self.assertTrue(xm.get_button_status("B"))
        self.assertTrue(xm.get_button_status("X"))
        self.assertTrue(xm.get_button_status("Y"))

        #   Check Shoulders
        xm.set_button_status("LEFT_SHOULDER", True)
        xm.set_button_status("RIGHT_SHOULDER", True)

        self.assertTrue(xm.get_button_status("LEFT_SHOULDER"))
        self.assertTrue(xm.get_button_status("RIGHT_SHOULDER"))

        #   Check DPAD
        xm.set_button_status("DPAD_LEFT", True)
        xm.set_button_status("DPAD_RIGHT", True)
        xm.set_button_status("DPAD_UP", True)
        xm.set_button_status("DPAD_DOWN", True)

        self.assertTrue(xm.get_button_status("DPAD_LEFT"))
        self.assertTrue(xm.get_button_status("DPAD_RIGHT"))
        self.assertTrue(xm.get_button_status("DPAD_UP"))
        self.assertTrue(xm.get_button_status("DPAD_DOWN"))

        #   Check Options
        xm.set_button_status("START", True)
        xm.set_button_status("BACK", True)

        self.assertTrue(xm.get_button_status("START"))
        self.assertTrue(xm.get_button_status("BACK"))

        #   Check Stick Click
        xm.set_button_status("LEFT_THUMB", True)
        xm.set_button_status("RIGHT_THUMB", True)

        self.assertTrue(xm.get_button_status("LEFT_THUMB"))
        self.assertTrue(xm.get_button_status("RIGHT_THUMB"))

        #   Check Trigger Setter Toggle
        xm.set_trigger_status("LEFT", True)
        xm.set_trigger_status("RIGHT", True)
        xm.set_trigger_offset("LEFT", 1.0)
        xm.set_trigger_offset("RIGHT", 1.0)

        self.assertTrue(xm.is_trigger_offset("LEFT"))
        self.assertTrue(xm.is_trigger_offset("RIGHT"))
        self.assertEqual(xm.get_offset_amount("LEFT"), 1.0)
        self.assertEqual(xm.get_offset_amount("RIGHT"), 1.0)

        #   Checks Stick Setter
        xm.set_stick_position("LEFT", "X", 1.0)
        xm.set_stick_position("LEFT", "Y", 1.0)
        xm.set_stick_position("RIGHT", "X", 1.0)
        xm.set_stick_position("RIGHT", "Y", 1.0)

        self.assertEqual(xm.get_stick_position("LEFT", "X"), 1.0)
        self.assertEqual(xm.get_stick_position("LEFT", "Y"), 1.0)
        self.assertEqual(xm.get_stick_position("RIGHT", "X"), 1.0)
        self.assertEqual(xm.get_stick_position("RIGHT", "Y"), 1.0)

        print("Finished test_xbox_model -> test_normal_boundary!")

    #   test_invalid_boundary_numerics checks that invalid numeric values can't
    #   be applied to the trigger offset fields or the stick axis fields.
    #   This does not test for invalid data types, however.
    def test_invalid_boundary_numerics(self):

        print("Running test_xbox_model -> test_invalid_boundary_numerics...")

        #   Checks for 'underflow' values of trigger offset
        with self.assertRaises(ValueError):
            xm.set_trigger_offset("LEFT", -0.1)

        with self.assertRaises(ValueError):
            xm.set_trigger_offset("LEFT", -0.01)

        with self.assertRaises(ValueError):
            xm.set_trigger_offset("RIGHT", -0.1)

        with self.assertRaises(ValueError):
            xm.set_trigger_offset("RIGHT", -0.01)

        #   Checks for 'overflow' values of trigger offset
        with self.assertRaises(ValueError):
            xm.set_trigger_offset("LEFT", 1.1)

        with self.assertRaises(ValueError):
            xm.set_trigger_offset("LEFT", 1.01)

        with self.assertRaises(ValueError):
            xm.set_trigger_offset("RIGHT", 1.1)

        with self.assertRaises(ValueError):
            xm.set_trigger_offset("RIGHT", 1.01)

        #   Checks for 'underflow' values of stick offset
        with self.assertRaises(ValueError):
            xm.set_stick_position("LEFT", "X", -1.1)

        with self.assertRaises(ValueError):
            xm.set_stick_position("LEFT", "Y", -1.1)

        with self.assertRaises(ValueError):
            xm.set_stick_position("RIGHT", "X", -1.1)

        with self.assertRaises(ValueError):
            xm.set_stick_position("RIGHT", "Y", -1.1)

        with self.assertRaises(ValueError):
            xm.set_stick_position("LEFT", "X", -1.01)

        with self.assertRaises(ValueError):
            xm.set_stick_position("LEFT", "Y", -1.01)

        with self.assertRaises(ValueError):
            xm.set_stick_position("RIGHT", "X", -1.01)

        with self.assertRaises(ValueError):
            xm.set_stick_position("RIGHT", "Y", -1.01)

        #   Checks for 'overflow' values of stick offset

        with self.assertRaises(ValueError):
            xm.set_stick_position("LEFT", "X", 1.1)

        with self.assertRaises(ValueError):
            xm.set_stick_position("LEFT", "Y", 1.1)

        with self.assertRaises(ValueError):
            xm.set_stick_position("RIGHT", "X", 1.1)

        with self.assertRaises(ValueError):
            xm.set_stick_position("RIGHT", "Y", 1.1)

        with self.assertRaises(ValueError):
            xm.set_stick_position("LEFT", "X", 1.01)

        with self.assertRaises(ValueError):
            xm.set_stick_position("LEFT", "Y", 1.01)

        with self.assertRaises(ValueError):
            xm.set_stick_position("RIGHT", "X", 1.01)

        with self.assertRaises(ValueError):
            xm.set_stick_position("RIGHT", "Y", 1.01)

        print("Finished test_xbox_model -> test_invalid_boundary_numerics!")

    #   test_valid_boundary_numerics ensures that numbers close to boundaries will
    #   not cause exceptions to be raised.
    def test_valid_boundary_numerics(self):

        print("Running test_xbox_model -> test_valid_boundary_numerics...")

        try:
            #   Checks upper bounds of trigger offset
            xm.set_trigger_offset("LEFT", 0.9)
            xm.set_trigger_offset("LEFT", 0.99)
            xm.set_trigger_offset("LEFT", 1.0)
            xm.set_trigger_offset("RIGHT", 0.9)
            xm.set_trigger_offset("RIGHT", 0.99)
            xm.set_trigger_offset("RIGHT", 1.0)

            #   Checks lower bounds of trigger offset
            xm.set_trigger_offset("LEFT", 0.1)
            xm.set_trigger_offset("LEFT", 0.01)
            xm.set_trigger_offset("LEFT", 0.0)
            xm.set_trigger_offset("RIGHT", 0.1)
            xm.set_trigger_offset("RIGHT", 0.01)
            xm.set_trigger_offset("RIGHT", 0.0)

        except ValueError:
            self.fail("Failure occurred during trigger offset setting")

        try:
            #   Checks upper bounds of stick offset
            xm.set_stick_position("LEFT", "X", 0.9)
            xm.set_stick_position("LEFT", "X", 0.99)
            xm.set_stick_position("LEFT", "X", 1.0)

            xm.set_stick_position("LEFT", "Y", 0.9)
            xm.set_stick_position("LEFT", "Y", 0.99)
            xm.set_stick_position("LEFT", "Y", 1.0)

            xm.set_stick_position("RIGHT", "X", 0.9)
            xm.set_stick_position("RIGHT", "X", 0.99)
            xm.set_stick_position("RIGHT", "X", 1.0)

            xm.set_stick_position("RIGHT", "Y", 0.9)
            xm.set_stick_position("RIGHT", "Y", 0.99)
            xm.set_stick_position("RIGHT", "Y", 1.0)

            #   Checks lower bounds of stick offset
            xm.set_stick_position("LEFT", "X", -0.9)
            xm.set_stick_position("LEFT", "X", -0.99)
            xm.set_stick_position("LEFT", "X", -1.0)

            xm.set_stick_position("LEFT", "Y", -0.9)
            xm.set_stick_position("LEFT", "Y", -0.99)
            xm.set_stick_position("LEFT", "Y", -1.0)

            xm.set_stick_position("RIGHT", "X", -0.9)
            xm.set_stick_position("RIGHT", "X", -0.99)
            xm.set_stick_position("RIGHT", "X", -1.0)

            xm.set_stick_position("RIGHT", "Y", -0.9)
            xm.set_stick_position("RIGHT", "Y", -0.99)
            xm.set_stick_position("RIGHT", "Y", -1.0)

        except ValueError:
            self.fail("Failure occurred during stick position setting")

        print("Finished test_xbox_model -> test_valid_boundary_numerics!")

    #   test_data_types ensures that only valid type data arguments are being
    #   parsed. This only validates data that would otherwise be registered to
    #   a field - it does not check values that are flags for switches.
    def test_data_types(self):

        print("Running test_xbox_model -> test_data_types...")

        #   Type check for button group - dpad, primaries, etc.
        try:
            xm.set_button_status("A", False)
        except TypeError:
            self.fail("Unexpected failure occurred during button offset dType test")

        with self.assertRaises(TypeError):
            xm.set_button_status("A", 1)

        with self.assertRaises(TypeError):
            xm.set_button_status("A", "X")

        with self.assertRaises(TypeError):
            xm.set_button_status("A", 1.0)

        with self.assertRaises(TypeError):
            xm.set_button_status("A", None)

        #   Type checks for set_trigger_status
        try:
            xm.set_trigger_status("LEFT", True)
        except TypeError:
            self.fail("Unexpected failure occurred during trigger status dType test")

        with self.assertRaises(TypeError):
            xm.set_trigger_status("LEFT", 1)

        with self.assertRaises(TypeError):
            xm.set_trigger_status("LEFT", "X")

        with self.assertRaises(TypeError):
            xm.set_trigger_status("LEFT", 1.0)

        with self.assertRaises(TypeError):
            xm.set_trigger_status("LEFT", None)

        print("Finished test_xbox_model -> test_data_types!")

        #   Type checks for set_trigger_offset
        try:
            xm.set_trigger_offset("LEFT", 1.0)
        except TypeError:
            self.fail("Unexpected failure occurred during trigger offset dType test")

        with self.assertRaises(TypeError):
            xm.set_trigger_offset("LEFT", "X")

        with self.assertRaises(TypeError):
            xm.set_trigger_offset("LEFT", None)

        #   Type checks for stick position
        try:
            xm.set_stick_position("LEFT", "X", 1.0)
        except TypeError:
            self.fail("Unexpected failure occurred during stick position dType test")

        with self.assertRaises(TypeError):
            xm.set_stick_position("LEFT", "X", "X")

        with self.assertRaises(TypeError):
            xm.set_stick_position("LEFT", "X", None)
