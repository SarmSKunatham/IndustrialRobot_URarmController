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
import Config

class Conveyor():
   def __init__(self, host='10.10.0.98', conveyor_port = 2002):
      self.host = host
      self.conveyor_port = conveyor_port
      self.conveyor_recv = None
      print("Conveyor init")
      socket_server = socket.socket()
      socket_server.bind((self.host, self.conveyor_port))
      print('Conveyor bind')
      socket_server.listen()
      print('Conveyor listen on port ', self.conveyor_port)
      self.conveyor, addr = socket_server.accept()
      time.sleep(2)
      print("Conveyor accept")
      print("Connection from: " + str(addr))
      # Activate tcp
      self.conveyor.sendall(b'activate,tcp,0.0\n')
      print("Conveyor activate")
      # Power on servo
      self.conveyor.sendall(b'pwr_on,conv,0\n')
      print("Conveyor power on")

   def run_conveyor(self, speed=10):
      self.conveyor.sendall(b'jog_stop\n')
      command = f'set_vel,conv,{speed}\n'
      self.conveyor.sendall(bytes(command, "UTF-8"))
      # self.conveyor_recv = self.conveyor.recv(20)
      # print (self.conveyor_recv)``
      self.conveyor.sendall(b'jog_fwd,conv,0\n')
      # self.conveyor_recv = self.conveyor.recv(20)
      # print (self.conveyor_recv)
   
   def stop_conveyor(self):
      self.conveyor.sendall(b'jog_stop,conv,0\n')
      # self.conveyor_recv = self.conveyor.recv(20)
      # print (self.conveyor_recv)

   def main(self):
      # Move conveyor
      self.run_conveyor()
      time.sleep(10)
      self.stop_conveyor()


if __name__ == '__main__':
      conveyor = Conveyor()
      conveyor.main()
