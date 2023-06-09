gripper_ip = "10.10.0.14"
gripper_port = 63352  
camera_ip = "10.10.1.10"
camera_port = 2023
conveyor_port = 2002

# start_pos = b'movel(p[0.11527,-0.29319,0.18998,0.014,-3.126,0.06],1,0.25,0,0)\n'
start_pos = [0.11527,-0.29319,0.18998,0.014,-3.126,0.06]
end_pos = start_pos.copy()
end_pos[2] -= 0.3
released_pos = [0.008,-0.507,-0.18,0.014,-3.126,0.06]

released_path = [
    # Move z direction
    [pos if idx != 2 else end_pos[2]+0.1 for idx,pos in enumerate(released_pos) ],
    released_pos,
]

back_to_start_path = [
    # Move z direction
    [pos if idx != 2 else start_pos[2]-0.2 for idx,pos in enumerate(released_pos) ],
    start_pos,
]
