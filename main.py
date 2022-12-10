from enum import Enum
import re


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Dimension:
    def __init__(self, dimensions=(5, 5)):
        self.dimensions = dimensions


class Robot:
    def __init__(self, move_range=(5, 5)):
        self.location = None
        self.facing = None
        self.move_range = move_range

    def is_ready(self):
        return self.location is not None

    def place(self, x, y, facing):
        if self.is_out_of_bounds(x, y):
            return False, 'The specified location is out of bounds.'

        self.location = (x, y)
        self.facing = facing

        return True, None

    def is_out_of_bounds(self, x, y):
        if x < 0 or x > self.move_range[0]:
            return True
        if y < 0 or y > self.move_range[1]:
            return True

        return False

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


def main():
    robot = Robot()

    direction_map = {
        'north': Direction.NORTH,
        'south': Direction.SOUTH,
        'east': Direction.EAST,
        'west': Direction.WEST,
    }

    # todo: discard all commands in the sequence until a valid PLACE command has been executed

    while True:
        cmd = input('robot command: ').lower().strip()

        place_tokens = re.search(r"place\s+([0-5]),([0-5]),([north|south|east|west]+)", cmd)
        if place_tokens:
            x = int(place_tokens[1])
            y = int(place_tokens[2])
            facing = place_tokens[3]

            placed, message = robot.place(x, y, direction_map[facing])
            if not placed:
                print(message)
                continue

        if not robot.is_ready():
            print('Robot not placed. Do a PLACE X,Y,F command first.')
            continue

        if cmd == 'left':
            robot.turn_left()
        if cmd == 'right':
            robot.turn_right()
        if cmd == 'move':
            pass
        if cmd == 'report':
            robot.report()


if __name__ == '__main__':
    main()
