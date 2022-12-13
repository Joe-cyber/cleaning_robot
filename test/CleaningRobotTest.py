import unittest
from unittest.mock import patch
from CleaningRobot import CleaningRobot
from CleaningRobotError import CleaningRobotError


class CleaningRobotTest(unittest.TestCase):
    """
    Your tests go here
    """
    def test_initialize_robot(self):
        robot = CleaningRobot(3, 3)
        robot.initialize_robot()
        self.assertEqual("(0,0,N)", robot.robot_status())

