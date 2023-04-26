import socket , time
import config

g_ip=config.camera_ip #replace by the IP address of the UR robot
g_port=config.camera_port  #PORT used by robotiq gripper

class Camera():
    def __init__(self, camera_ip = '10.10.1.10', camera_port = 2023):
        self.info = None
        self.angle = None
        self.x = None
        self.y = None
        self.camera_ip = camera_ip
        self.camera_port = camera_port
        self.camera = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.camera.connect((self.camera_ip, self.camera_port))
        print('Camera Activated')

    def get_camera_info(self):
        '''Get the camera detect information'''
        self.camera.send(b'get info')
        data = self.camera.recv(30)
        self.info = str(data)[2:-1]
        self.angle, self.x, self.y = [float(num) for num in self.info.split(',')]

    def main(self):
        while True:
            self.get_camera_info()
            print(f'Angle: {self.angle}, X: {self.x}, Y: {self.y}')
        
if __name__ == '__main__':
    camera = Camera()
    camera.main()
