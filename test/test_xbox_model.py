from src import xbox_model as xm
import unittest


class TestXboxModel(unittest.TestCase):

    #   test_default_returns verifies that default variables have not been
    #   modified. As a rule, all default values will be either 'False' or 0.00
    def test_default_returns(self):

        #   Checks Button Defaults
        self.assertFalse(xm.is_button_depressed("A"))
        self.assertFalse(xm.is_button_depressed("B"))
        self.assertFalse(xm.is_button_depressed("X"))
        self.assertFalse(xm.is_button_depressed("Y"))

        #   Checks Shoulder Defaults
        self.assertFalse(xm.is_shoulder_depressed("LEFT"))
        self.assertFalse(xm.is_shoulder_depressed("RIGHT"))

        #   Checks DPAD Defaults
        self.assertFalse(xm.is_dpad_depressed("LEFT"))
        self.assertFalse(xm.is_dpad_depressed("RIGHT"))
        self.assertFalse(xm.is_dpad_depressed("TOP"))
        self.assertFalse(xm.is_dpad_depressed("BOTTOM"))

        #   Checks Option Defaults
        self.assertFalse(xm.is_option_depressed("BACK"))
        self.assertFalse(xm.is_option_depressed("START"))

        #   Checks Trigger Defaults
        self.assertFalse(xm.is_trigger_depressed("LEFT"))
        self.assertFalse(xm.is_trigger_depressed("RIGHT"))

        self.assertEqual(xm.get_depression_amount("LEFT"), 0.00)
        self.assertEqual(xm.get_depression_amount("RIGHT"), 0.00)

        #   Checks Stick Defaults
        self.assertEqual(xm.get_stick_position("LEFT", "X"), 0.00)
        self.assertEqual(xm.get_stick_position("LEFT", "Y"), 0.00)
        self.assertEqual(xm.get_stick_position("RIGHT", "X"), 0.00)
        self.assertEqual(xm.get_stick_position("RIGHT", "Y"), 0.00)

    #   test_normal_boundary validates that setter functions are performing
    #   as expected in normal circumstance. E.g. all relevant setters will
    #   toggle from False (prior test) to True, or that the trigger depressions
    #   can be toggled to 0.5, etc.
    def test_normal_boundary(self):

        #   Checks Button Setter Toggle
        xm.set_button_depressed("B", True)
        xm.set_button_depressed("X", True)
        xm.set_button_depressed("A", True)
        xm.set_button_depressed("Y", True)

        self.assertTrue(xm.is_button_depressed("A"))
        self.assertTrue(xm.is_button_depressed("B"))
        self.assertTrue(xm.is_button_depressed("X"))
        self.assertTrue(xm.is_button_depressed("Y"))


