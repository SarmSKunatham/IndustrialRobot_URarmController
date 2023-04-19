from robot import *
from gripper import *
import config
import time

g = connect_gripper()
r = connect_robot()

for i in range(2):
    gripper_open(g)

    for pos in config.back_to_start_path:
        command = "movej(p{}, 1, 0.25, 3, 0)\n".format(pos)
        r.send(bytes(command, "UTF-8"))
        time.sleep(4)
    
    end_pos = config.start_pos.copy()
    end_pos[2] -= 0.305
    end_pos[3] -= 0.7

    command = "movej(p{}, 1, 0.25, 3, 0)\n".format(end_pos)
    r.send(bytes(command, "UTF-8"))
    time.sleep(5)
    
    gripper_close(g)
    
    for pos in config.released_path:
        command = "movej(p{}, 1, 0.25, 3, 0 )\n".format(pos)
        r.send(bytes(command, "UTF-8"))
        time.sleep(4)

    gripper_open(g)

# # Reset to the original state.
# gripper_open(g)
# for pos in config.back_to_start_path:
#     command = "movej(p{}, 1, 0.25, 3, 0 )\n".format(pos)
#     r.send(bytes(command, "UTF-8"))
#     time.sleep(4)

