import time
from conveyor import Conveyor
from gripper import Gripper
from arm import Arm
import config

def pickup_box():
    conveyor = Conveyor()
    arm = Arm()
    gripper = Gripper()

    # Start conveyor
    conveyor.run_conveyor()
    print("Start conveyor!")

    # Open the gripper
    gripper.gripper_open()
    time.sleep(3)

    # Move arm to start pos
    arm.movej_to_position(config.start_pos)
    print("move to start pos")
    time.sleep(3)

    # # Move to box pos
    arm.movej_to_position(config.box_pos)
    print("move to box pos")
    time.sleep(3)

    # Close gripper
    gripper.gripper_close()
    time.sleep(3)

    # Move to start
    arm.movej_to_position(config.start_pos)
    print("move to start")
    time.sleep(3)

    # Stop conv
    conveyor.stop_conveyor()

    # Place box
    arm.movej_to_position(config.released_pos)
    time.sleep(3)
    print("move to end pos")
    time.sleep(3)
    gripper.gripper_open()
    time.sleep(3)
    arm.movej_to_position(config.start_pos)
    print("move to start pos")
    time.sleep(3)

if __name__ == '__main__':
    pickup_box()

    


