import socket , time
import binascii
import config

g_ip=config.camera_ip #replace by the IP address of the UR robot
g_port=config.camera_port  #PORT used by robotiq gripper


v=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
v.connect((g_ip,g_port))

def get_info(v):
    v.send(b'get data')
    data = v.recv(30)
    info = str(data)[2:-1]
    angle, x, y = [float(num) for num in info.split(',')]
    return angle, x, y

while True:
    angle, x, y = get_info(v)
    print(angle)
