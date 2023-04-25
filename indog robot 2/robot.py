import socket
import struct
import time
import config

robot_ip = '10.10.0.14'
robot_port = 30003


class Robot:
    def __init__(self):
        self.r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.r.connect((robot_ip, robot_port))

    def send_command(self, command):
        self.r.send(bytes(command, "UTF-8"))

    def move_to_position(self, position, speed=1, acceleration=0.25):
        command = "movej(p{}, {}, {}, 3, 0)\n".format(position, speed, acceleration)
        self.send_command(command)
        time.sleep(4)

    def move_to_end_position(self, end_pos):
        command = "movej(p{}, 1, 0.25, 3, 0)\n".format(end_pos)
        self.send_command(command)
        time.sleep(5)
