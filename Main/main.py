import time
from conveyor import Conveyor
from gripper import Gripper
from arm import Arm
import config
from camera import Camera
import math

# Initialize
conveyor = Conveyor()
arm = Arm()
gripper = Gripper()
camera = Camera()

# Move arm to start position and open gripper
start_position = [0.116,-0.3,0.2,0,-3.143,0]
arm.movel_to_position(start_position)
gripper.gripper_open()
start_time = time.time()

# Start conveyor
conveyor.run_conveyor()

# Detect object
while True:
    camera.get_camera_info()
    # print(f'Angle: {camera.angle}, X: {camera.x}, Y: {camera.y}, numberObj: {camera.numberObj}')
    # print(type(camera.numberObj), camera.numberObj)
    if camera.numberObj == '1':
        print(f'Latest Angle: {camera.angle}, X: {camera.x}, Y: {camera.y}, numberObj: {camera.numberObj}')
        break

print(f'Final Angle: {camera.angle}, X: {camera.x}, Y: {camera.y}, numberObj: {camera.numberObj}')
        

# Calculate position of the box
# if float(camera.angle) >= 270.0 and float(camera.angle) <= 360.0:
#     camera.angle = 360.0 - float(camera.angle) 

new_x = start_position[0] + ((540 - float(camera.x)) * -0.00019) + 0.18 - 0.05
new_y = start_position[1] + ((550 - float(camera.y)) * -0.00019)
 
new_pos = start_position.copy()
new_pos[0] = new_x
new_pos[1] = new_y
new_pos[2] = 0.04
if not(float(camera.angle) >= 270.0 and float(camera.angle)<= 360.0):
    new_rx = start_position[3] + math.radians(float(camera.angle))
    new_pos[3] = new_rx
arm.movel_to_position(new_pos)

# move down to grab
new_pos[2] = -0.1
arm.movel_to_position(new_pos)
time.sleep(2.5)
gripper.gripper_close()

# Move up
new_pos[2] = 0.2
arm.movel_to_position(start_position)
stop_time = time.time()

print('Congratultation!!!')
print(f'Time : {stop_time - start_time}')

