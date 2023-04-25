import socket , time 

class Gripper:
    def __init__(self, gripper_ip='10.10.0.14', gripper_port=63352):
        self.gripper_ip = gripper_ip
        self.gripper_port = gripper_port
        self.gripper_recv = ""
        self.gripper = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gripper.connect((self.gripper_ip, self.gripper_port))
        self.g.send(b'GET ACT\n')
        self.gripper_recv = str(self.gripper.recv(10), 'UTF-8')
        if '1' in self.gripper_recv:
            print('Gripper Activated')
        else:
            print('Gripper is not Activated')

    def gripper_open(self):
        '''Open the gripper'''
        self.gripper.send(b'SET POS 0\n')
        self.gripper_recv = str(self.gripper.recv(255), 'UTF-8')
        print(self.gripper_recv)
        time.sleep(1)

    def close(self):
        '''Close the gripper'''
        self.gripper.send(b'SET POS 255\n')
        self.gripper_recv = str(self.gripper.recv(255), 'UTF-8')
        print(self.gripper_recv)
        time.sleep(1)

    def main(self):
        '''Main function'''
        # TEST
        self.gripper.send(b'GET POS\n')
        self.gripper_recv = str(self.gripper.recv(10), 'UTF-8')
        if self.gripper_recv:
            self.gripper.send(b'SET ACT 1\n')
            self.gripper_recv = str(self.gripper.recv(255), 'UTF-8')
            print(self.gripper_recv)
            time.sleep(3)
            self.gripper.send(b'SET GTO 1\n')
            self.gripper.send(b'SET SPE 255\n')
            self.gripper.send(b'SET FOR 255\n')
        
        while 1:
            self.gripper.send(b'SET POS 255\n')
            self.gripper_recv = str(self.gripper.recv(255), 'UTF-8')
            print(self.gripper_recv)
            time.sleep(2)
            self.gripper.send(b'SET POS 0\n')
            self.gripper_recv = str(self.gripper.recv(255), 'UTF-8')
            print(self.gripper_recv)
            time.sleep(2)

if __name__ == '__main__':
    gripper = Gripper()
    gripper.main()
