import socket , time
import binascii
import config


g_ip = config.gripper_ip
g_port = config.gripper_port

    
      
def main():


   #Socket communication
   g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   g.connect((g_ip, g_port))
   g.send(b'GET ACT\n')
   g_recv = str(g.recv(10), 'UTF-8')
   if '1' in g_recv :
      print ('Gripper Activated')

   print ('get ACT  == ' + g_recv)
   g.send(b'GET POS\n')
   g_recv = str(g.recv(10), 'UTF-8')
   if g_recv :
      g.send(b'SET ACT 1\n')
      g_recv = str(g.recv(255), 'UTF-8')
      print (g_recv)
      time.sleep(3)
      g.send(b'SET GTO 1\n')
      g.send(b'SET SPE 255\n')
      g.send(b'SET FOR 255\n')

   while True:
      
      g.send(b'SET POS 255\n')
      g_recv = str(g.recv(255), 'UTF-8')
      print (g_recv)
      time.sleep(2)
      g.send(b'SET POS 0\n')
      g_recv = str(g.recv(255), 'UTF-8')
      print (g_recv)
      # g.send(b"get_actual_tcp_pose()\n")
      # print(f"pos= {str(g.recv(255))} " )
      time.sleep(2)

      




if __name__ == '__main__':
    import sys
    main()
