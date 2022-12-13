import unittest
from unittest.mock import patch
from CleaningRobot import CleaningRobot
from CleaningRobotError import CleaningRobotError
from mock import GPIO


class CleaningRobotTest(unittest.TestCase):
    """
    Your tests go here
    """
    def test_initialize_robot(self):
        robot = CleaningRobot(3, 3)
        robot.initialize_robot()
        self.assertEqual("(0,0,N)", robot.robot_status())

    @patch.object(GPIO, 'input')
    def test_battery_is_under_10_percent(self, mock_input):
        mock_input.return_value = 5
        robot = CleaningRobot(3, 3)
        robot.initialize_robot()
        self.assertTrue(robot.battery_led_on)
