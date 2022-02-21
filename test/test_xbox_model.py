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
        self.assertFalse(xm.is_button_offset("A"))
        self.assertFalse(xm.is_button_offset("B"))
        self.assertFalse(xm.is_button_offset("X"))
        self.assertFalse(xm.is_button_offset("Y"))

        #   Checks Shoulder Defaults
        self.assertFalse(xm.is_shoulder_offset("LEFT"))
        self.assertFalse(xm.is_shoulder_offset("RIGHT"))

        #   Checks DPAD Defaults
        self.assertFalse(xm.is_dpad_offset("LEFT"))
        self.assertFalse(xm.is_dpad_offset("RIGHT"))
        self.assertFalse(xm.is_dpad_offset("TOP"))
        self.assertFalse(xm.is_dpad_offset("BOTTOM"))

        #   Checks Option Defaults
        self.assertFalse(xm.is_option_offset("BACK"))
        self.assertFalse(xm.is_option_offset("START"))

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

        #   Checks Button Setter Toggle
        xm.set_button_offset("A", True)
        xm.set_button_offset("B", True)
        xm.set_button_offset("X", True)
        xm.set_button_offset("Y", True)

        self.assertTrue(xm.is_button_offset("A"))
        self.assertTrue(xm.is_button_offset("B"))
        self.assertTrue(xm.is_button_offset("X"))
        self.assertTrue(xm.is_button_offset("Y"))

        #   Check Shoulder Setter Toggle
        xm.set_shoulder_offset("LEFT", True)
        xm.set_shoulder_offset("RIGHT", True)

        self.assertTrue(xm.is_shoulder_offset("LEFT"))
        self.assertTrue(xm.is_shoulder_offset("RIGHT"))

        #   Check DPAD Setter Toggle
        xm.set_dpad_offset("LEFT", True)
        xm.set_dpad_offset("RIGHT", True)
        xm.set_dpad_offset("TOP", True)
        xm.set_dpad_offset("BOTTOM", True)

        self.assertTrue(xm.is_dpad_offset("LEFT"))
        self.assertTrue(xm.is_dpad_offset("RIGHT"))
        self.assertTrue(xm.is_dpad_offset("TOP"))
        self.assertTrue(xm.is_dpad_offset("BOTTOM"))

        #   Check Option Setter Toggle
        xm.set_option_offset("START", True)
        xm.set_option_offset("BACK", True)

        self.assertTrue(xm.is_option_offset("START"))
        self.assertTrue(xm.is_option_offset("BACK"))

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

        #   Type checks for set_button_offset
        try:
            xm.set_button_offset("A", False)
        except TypeError:
            self.fail("Unexpected failure occurred during button offset dType test")

        with self.assertRaises(TypeError):
            xm.set_button_offset("A", 1)

        with self.assertRaises(TypeError):
            xm.set_button_offset("A", "X")

        with self.assertRaises(TypeError):
            xm.set_button_offset("A", 1.0)

        with self.assertRaises(TypeError):
            xm.set_button_offset("A", None)

        #   Type checks for set_shoulder_offset
        try:
            xm.set_shoulder_offset("LEFT", True)
        except TypeError:
            self.fail("Unexpected failure occurred during shoulder offset dType test")

        with self.assertRaises(TypeError):
            xm.set_shoulder_offset("LEFT", 1)

        with self.assertRaises(TypeError):
            xm.set_shoulder_offset("LEFT", "X")

        with self.assertRaises(TypeError):
            xm.set_shoulder_offset("LEFT", 1.0)

        with self.assertRaises(TypeError):
            xm.set_shoulder_offset("LEFT", None)

        #   Type checks for set_dpad_offset
        try:
            xm.set_dpad_offset("LEFT", True)
        except TypeError:
            self.fail("Unexpected failure occurred during dpad offset dType test")

        with self.assertRaises(TypeError):
            xm.set_dpad_offset("LEFT", 1)

        with self.assertRaises(TypeError):
            xm.set_dpad_offset("LEFT", "X")

        with self.assertRaises(TypeError):
            xm.set_dpad_offset("LEFT", 1.0)

        with self.assertRaises(TypeError):
            xm.set_dpad_offset("LEFT", None)

        #   Type checks for set_option_offset
        try:
            xm.set_option_offset("START", True)
        except TypeError:
            self.fail("Unexpected failure occurred during option offset dType test")

        with self.assertRaises(TypeError):
            xm.set_option_offset("START", 1)

        with self.assertRaises(TypeError):
            xm.set_option_offset("START", "X")

        with self.assertRaises(TypeError):
            xm.set_option_offset("START", 1.0)

        with self.assertRaises(TypeError):
            xm.set_option_offset("START", None)

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
            xm.set_trigger_offset("LEFT", 1)

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
            xm.set_stick_position("LEFT", "X", 1)

        with self.assertRaises(TypeError):
            xm.set_stick_position("LEFT", "X", "X")

        with self.assertRaises(TypeError):
            xm.set_stick_position("LEFT", "X", None)