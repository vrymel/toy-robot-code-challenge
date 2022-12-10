# toy-robot-code-challenge

## setup
The solution does not have any 3rd-party libraries so it should run on at least Python 3.4

## example
```
python main.py

# output
robot command: PLACE 1,2,NORTH
robot command: MOVE
robot command: MOVE
robot command: RIGHT
robot command: MOVE
robot command: REPORT
Robot is at location (2, 4) and facing Direction.EAST
robot command:
```

## testing
a simple `tests.py` is created to test the integrity of the robot.

```bash
python tests.py
```