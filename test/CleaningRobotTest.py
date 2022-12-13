import unittest
from unittest.mock import patch
from CleaningRobot import CleaningRobot
from CleaningRobotError import CleaningRobotError
from mock import GPIO


class CleaningRobotTest(unittest.TestCase):
    """
    Your tests go here
    """

    def setUp(self) -> None:
        self.robot = CleaningRobot(3, 3)
        self.robot.initialize_robot()

    def test_initialize_robot(self):
        self.assertEqual("(0,0,N)", self.robot.robot_status())

    @patch.object(GPIO, 'input')
    def test_battery_is_under_10_percent(self, mock_input):
        mock_input.return_value = 5
        self.robot.manage_battery()
        self.assertTrue(self.robot.battery_led_on)

    @patch.object(GPIO, 'input')
    def test_battery_is_up_10_percent(self, mock_input):
        mock_input.return_value = 15
        self.robot.manage_battery()
        self.assertTrue(self.robot.cleaning_system_on)

    def test_implement_execute_command_forward(self):
        new_pos = self.robot.execute_command('f')
        self.assertEqual("(0,1,N)", new_pos)

    def test_implement_execute_command_left(self):
        new_pos = self.robot.execute_command('l')
        self.assertEqual("(0,0,W)", new_pos)

    def test_implement_execute_command_right(self):
        self.assertRaises(CleaningRobotError, self.robot.execute_command, 'a')

    @patch.object(GPIO, 'input')
    def test_obstacle_found_true(self, mock_input):
        mock_input.return_value = 100
        obstacle = self.robot.obstacle_found()
        self.assertTrue(obstacle)

    @patch.object(GPIO, 'input')
    def test_obstacle_found_false(self, mock_input):
        mock_input.return_value = 0
        obstacle = self.robot.obstacle_found()
        self.assertFalse(obstacle)

    @patch.object(GPIO, 'input')
    def test_obstacle_found_state(self, mock_input):
        mock_input.return_value = 50
        self.assertEqual("(0,0,N)(0,1)", self.robot.robot_status())

    @patch.object(GPIO, 'input')
    def test_implement_execute_command_forward_status_update(self, mock_input):
        mock_input.return_value = 50
        new_pos = self.robot.execute_command('f')
        self.assertEqual("(0,1,N)(0,2)", new_pos)
