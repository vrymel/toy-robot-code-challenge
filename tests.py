import unittest

from Robot import Robot


class TestRobot(unittest.TestCase):
    def test_not_ready(self):
        r = Robot()
        self.assertFalse(r.is_ready(), 'the robot should not be ready if not placed yet')


if __name__ == '__main__':
    unittest.main()