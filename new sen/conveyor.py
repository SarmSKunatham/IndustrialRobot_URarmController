####### Command for control conveyor #################
#### activate tcp        = activate,tcp
#### power on servo      = pwr_on,conv,0
#### power off servo     = pwr_off,conv,0
#### set velocity x mm/s = set_vel,conv,x   # x = 0 to 200
#### jog forward         = jog_fwd,conv,0
#### jog backward        = jog_bwd,conv,0
#### stop conveyor       = jog_stop,conv,0
#########################################################

#พังนะน้อง


import socket,time
import config


host    = '10.10.0.98'
c_port  = config.conveyor_port #PORT used by conveyor


def connect_conveyor():
   print(host)
   s = socket.socket()
   s.bind((host, c_port))
   print("bind")
   s.listen()
   print("Listen")
   c, addr = s.accept()
   print('accept')
   print("Connection from: " + str(addr))

   c.sendall(b'activate,tcp,0.0\n')
   # c_recv = c.recv(20)
   # print (c_recv)
   c.sendall(b'pwr_on,conv,0\n')
   # c_recv = c.recv(20)
   # print (c_recv)
   return c
def run_conveyour(c, speed=10):
   command = f'set_vel,conv,{speed}\n'
   c.sendall(bytes(command, "UTF-8"))
   c_recv = c.recv(20)
   print (c_recv)
   c.sendall(b'jog_fwd,conv,0\n')
   c_recv = c.recv(20)
   print (c_recv)

def stop_conveyour(c):
   c.sendall(b'jog_stop,conv,0\n')
   c_recv = c.recv(20)
   print (c_recv)


def main():
   #Socket communication
   s = socket.socket()
   s.bind((host, c_port))
   s.listen()
   c, addr = s.accept()
   print("step1")
   print("Connection from: " + str(addr))

   c.sendall(b'activate,tcp,0.0\n')
   c_recv = c.recv(20)
   print("step2")
   print (c_recv)

   c.sendall(b'pwr_on,conv,0\n')
   time.sleep(1)

   c.sendall(b'set_vel,conv,10\n')
   c_recv = c.recv(20)
   print (c_recv)
   c.sendall(b'jog_fwd,conv,0\n')
   c_recv = c.recv(20)
   print (c_recv)
   



if __name__ == '__main__':
    import sys
    c = connect_conveyor()
    run_conveyour(c, speed=20)
    time.sleep(10)
    stop_conveyour(c)
