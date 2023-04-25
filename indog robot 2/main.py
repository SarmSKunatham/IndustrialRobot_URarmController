from gripper import Gripper
from robot import Robot
import config

gripper = Gripper()
robot = Robot()

for i in range(2):
    gripper.open()

    for pos in config.back_to_start_path:
        robot.move_to_position(pos)

    end_pos = config.start_pos.copy()
    end_pos[2] -= 0.305
    end_pos[3] -= 0.7

    robot.move_to_end_position(end_pos)

    gripper.close()

    for pos in config.released_path:
        robot.move_to_position(pos)

    gripper.open()
