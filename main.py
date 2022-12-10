import re

from Direction import Direction
from Robot import Robot


def main():
    robot = Robot()

    direction_map = {
        'north': Direction.NORTH,
        'south': Direction.SOUTH,
        'east': Direction.EAST,
        'west': Direction.WEST,
    }

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
        elif cmd == 'right':
            robot.turn_right()
        elif cmd == 'move':
            robot.move()
        elif cmd == 'report':
            print(robot)
        else:
            # only show invalid message if the robot is ready.
            if robot.is_ready():
                print('Invalid command. Only the following commands are allowed:')
                print('PLACE X,Y,F')
                print('MOVE')
                print('LEFT')
                print('RIGHT')
                print('REPORT')


if __name__ == '__main__':
    main()
