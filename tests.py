import unittest

from Direction import Direction
from Robot import Robot


class TestRobot(unittest.TestCase):
    def test_not_ready(self):
        r = Robot()
        self.assertFalse(r.is_ready(), 'the robot should not be ready if not placed yet')

    def test_place(self):
        r = Robot()
        placed, _msg = r.place(4, 3, Direction.NORTH)

        self.assertTrue(placed, 'the robot should be placed')
        self.assertEqual(r.location, (4, 3), 'the robot should be placed at location (4,3)')
        self.assertEqual(r.facing, Direction.NORTH, 'the robot should be facing NORTH')

    def test_invalid_place(self):
        r = Robot()
        placed, _msg = r.place(6, 3, Direction.NORTH)

        self.assertFalse(placed, 'the robot should not be placed because the location is out of bounds')

    def test_is_out_of_bounds(self):
        r = Robot()

        self.assertFalse(r.is_out_of_bounds(0, 0))
        self.assertFalse(r.is_out_of_bounds(5, 5))
        self.assertTrue(r.is_out_of_bounds(-1, -1))
        self.assertTrue(r.is_out_of_bounds(6, 6))

    def test_turn_left(self):
        r = Robot()
        r.place(0, 0, Direction.NORTH)
        r.turn_left()

        self.assertEqual(r.facing, Direction.WEST, 'the robot should be facing WEST when turned left from NORTH')
        self.assertEqual(r.location, (0, 0), 'the robot should not have moved')

    def test_turn_right(self):
        r = Robot()
        r.place(0, 0, Direction.NORTH)
        r.turn_right()

        self.assertEqual(r.facing, Direction.EAST, 'the robot should be facing EAST when turned right from NORTH')
        self.assertEqual(r.location, (0, 0), 'the robot should not have moved')

    def test_move(self):
        r = Robot()
        r.place(0, 0, Direction.NORTH)
        r.move()

        self.assertEqual(r.facing, Direction.NORTH, 'the robot should still be facing NORTH')
        self.assertEqual(r.location, (0, 1), 'the robot should move at the positive y-direction')

    def test_rotate_right(self):
        r = Robot()
        r.place(0, 0, Direction.NORTH)
        r.move()

        self.assertEqual(r.facing, Direction.NORTH, 'the robot should still be facing NORTH')
        self.assertEqual(r.location, (0, 1), 'the robot should move at the positive y-direction')

        r.turn_right()
        r.move()

        self.assertEqual(r.facing, Direction.EAST, 'the robot should be facing EAST by now')
        self.assertEqual(r.location, (1, 1), 'the robot should move at the positive x-direction')

        r.turn_right()
        r.move()

        self.assertEqual(r.facing, Direction.SOUTH, 'the robot should be facing SOUTH by now')
        self.assertEqual(r.location, (1, 0), 'the robot should move at the negative y-direction')

        r.turn_right()
        r.move()

        self.assertEqual(r.facing, Direction.WEST, 'the robot should be facing WEST by now')
        self.assertEqual(r.location, (0, 0), 'the robot should move at the negative x-direction')

    def test_rotate_left(self):
        r = Robot()
        r.place(1, 1, Direction.NORTH)
        r.move()

        self.assertEqual(r.facing, Direction.NORTH, 'the robot should still be facing NORTH')
        self.assertEqual(r.location, (1, 2), 'the robot should move at the positive y-direction')

        r.turn_left()
        r.move()

        self.assertEqual(r.facing, Direction.WEST, 'the robot should be facing WEST by now')
        self.assertEqual(r.location, (0, 2), 'the robot should move at the negative x-direction')

        r.turn_left()
        r.move()

        self.assertEqual(r.facing, Direction.SOUTH, 'the robot should be facing SOUTH by now')
        self.assertEqual(r.location, (0, 1), 'the robot should move at the negative y-direction')

        r.turn_left()
        r.move()

        self.assertEqual(r.facing, Direction.EAST, 'the robot should be facing EAST by now')
        self.assertEqual(r.location, (1, 1), 'the robot should move at the positive x-direction')


if __name__ == '__main__':
    unittest.main()
