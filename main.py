from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Robot:
    def __init__(self, facing=Direction.NORTH):
        self.facing = facing

    def turn_left(self):
        target_direction = self.facing.value - 1
        if target_direction < Direction.NORTH.value:
            target_direction = Direction.WEST.value

        self.facing = Direction(target_direction)

    def turn_right(self):
        target_direction = self.facing.value + 1
        if target_direction > Direction.WEST.value:
            target_direction = Direction.NORTH.value

        self.facing = Direction(target_direction)

    def report(self):
        print(f'I\'m facing {self.facing}')


class TableTop:
    def __init__(self, dimensions=(5, 5)):
        self.dimensions = dimensions


def main(name):
    robot = Robot()

    while True:
        foo = input('turn left or right')

        if foo == 'left':
            robot.turn_left()
        if foo == 'right':
            robot.turn_right()

        robot.report()


if __name__ == '__main__':
    main('PyCharm')
