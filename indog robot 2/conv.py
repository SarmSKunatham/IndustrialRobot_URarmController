####### Command for control conveyor #################
#### activate tcp        = activate,tcp
#### power on servo      = pwr_on,conv,0
#### power off servo     = pwr_off,conv,0
#### set velocity x mm/s = set_vel,conv,x   # x = 0 to 200
#### jog forward         = jog_fwd,conv,0
#### jog backward        = jog_bwd,conv,0
#### stop conveyor       = jog_stop,conv,0
#########################################################


import socket,time
import config


host    = socket.gethostname()
c_port  = config.conveyor_port #PORT used by conveyor

      
def main():
   #Socket communication
   s = socket.socket()
   s.bind((host, c_port))
   s.listen()
   c, addr = s.accept()
   print("Connection from: " + str(addr))

   c.sendall(b'activate,tcp,0.0\n')
   # c_recv = c.recv(20)
   # print (c_recv)
   c.sendall(b'pwr_on,conv,0\n')
   # c_recv = c.recv(20)
   # print (c_recv)
   time.sleep(1)

   # c.sendall(b'set_vel,conv,10\n')
   # c_recv = c.recv(20)
   # print (c_recv)
   c.sendall(b'jog_fwd,conv,0\n')
   c_recv = c.recv(20)
   print (c_recv)
   



if __name__ == '__main__':
    import sys
    main()
