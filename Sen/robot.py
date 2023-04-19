#!/usr/bin/env python
# encoding: utf=8

""" 
#UR Controller Primary Client Interface Reader
# For software version 3.0
#
# Overview of client interface      : https://www.universal-robots.com/articles/ur/interface-communication/overview-of-client-interfaces/
# Datastream info found             : https://www.universal-robots.com/articles/ur/interface-communication/remote-control-via-tcpip/
# Script command for control robot  : https://s3-eu-west-1.amazonaws.com/ur-support-site/124999/scriptManual_3.15.4.pdf
"""

import socket, struct , time ,os
import array
import pickle
import config

robot_ip   = '10.10.0.14'
robot_port = 30003    ####RTDE

buffer_size = 140
get_pos_buffer_size=1116
joint_deg = [0.0,0.0,0.0,0.0,0.0,0.0]
joint_tcp = [0.0,0.0,0.0,0.0,0.0,0.0]    ####Base Ref

joint_speed = 0.1


def connect_robot() :

        global r
        
        ####Establish connection to controller
        r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r.connect((robot_ip, robot_port))
        #r_recv = r.recv(buffer_size)
        #if r_recv :
                #print('Connected to Primary interfaces....SUCCESSFULLY!')
                #print (r_recv)
        #else :
                #print('Connected to Primary interfaces...FAILED!')
        return r


def robot_status():
        
        global robot_mode
        r_recv = r.recv(buffer_size)
        robot_data = struct.unpack('!i142d',r_recv)
        robot_mode = robot_data[95]
        for i in range (0,6) :
                joint_tcp[i] = round(robot_data[56+i],3)
                joint_deg[i] = round((robot_data[32+i])/0.01745,2)
             
                
        print ('Robot mode    : ' + str(robot_mode))
        #print (robot_data)    
        print ('Robot Joint Pos    : ' + str(joint_tcp))
        print ('Robot Joint Deg    : ' + str(joint_deg))
        

def main():
        connect_robot()              
        #robot_status()
        print('Robot start moving')
        end_pos = config.start_pos.copy()
        end_pos[2] =  end_pos[2]-0.1
        print(end_pos)
        command = "movel(p{}, 1, 0.25, 0, 0 )\n".format(end_pos)
        r.send(bytes(command, "UTF-8"))
        r_recv = str(r.recv(255))
        print(r_recv)
        time.sleep(2)

        command = "movel(p{}, 1, 0.25, 0, 0 )\n".format(config.start_pos)
        print(config.start_pos)
        r.send(bytes(command, "UTF-8"))
        #r.send(b"get_actual_tcp_pose()\n")



        #data = r.recv(24)
        #print(data)
        # data = array.array("ffffff", data)
        # data.tolist()
        # data.byteswap()
        #print( struct.unpack("5hk0tf", data) )
 
        


if __name__ == '__main__':
    import sys
    main()

