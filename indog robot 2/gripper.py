import socket
import time

gripper_ip = "10.10.0.14"
gripper_port = 63352


class Gripper:
    def __init__(self):
        self.g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.g.connect((gripper_ip, gripper_port))
        self.g.send(b'GET ACT\n')
        g_recv = str(self.g.recv(10), 'UTF-8')
        if '1' in g_recv:
            print('Gripper Activated')

    def open(self):
        self.g.send(b'SET POS 0\n')
        g_recv = str(self.g.recv(255), 'UTF-8')
        print(g_recv)
        time.sleep(1)

    def close(self):
        self.g.send(b'SET POS 255\n')
        g_recv = str(self.g.recv(255), 'UTF-8')
        print(g_recv)
        time.sleep(1)
