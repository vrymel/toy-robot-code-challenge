from Direction import Direction


class Robot:
    def __init__(self, move_range=(5, 5)):
        self.location = None
        self.facing = None
        self.move_range = move_range

    def is_ready(self):
        return (self.location is not None) and (self.facing is not None)

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

    def move(self):
        x, y = self.location
        if self.facing == Direction.NORTH:
            y = y + 1
        elif self.facing == Direction.SOUTH:
            y = y - 1
        elif self.facing == Direction.WEST:
            x = x - 1
        elif self.facing == Direction.EAST:
            x = x + 1

        if self.is_out_of_bounds(x, y):
            print('Robot can\'t move beyond range')
            return

        self.location = (x, y)

    def __repr__(self):
        return f'Robot is at location {self.location} and facing {self.facing}'
