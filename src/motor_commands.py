#!/usr/bin/env python2
import socket
import rospy
from std_msgs.msg import Int16
s = socket.socket()
host = socket.gethostname()  #IP Address of the Raspberry pi
port = 9999            #Must be same as that in server.py
#In client.py we use another way to bind host and port together by using connect function()
s.connect((host, port))
print('connected to the host')
mode = 0;   #0-> Propulsion
forwardBackwardSpeed = 0;
leftRightSpeed = 0;
linear_velocity=2;
angular_velocity=3;
width_chassi=4;
radius_wheel=2;
def sendDatatoRaspi():
    global forwardBackwardSpeed, leftRightSpeed;
    print(forwardBackwardSpeed)
    print(leftRightSpeed)
    stringData = str(mode) + ',' + str(forwardBackwardSpeed*10) + ',' + str(leftRightSpeed*10)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def printSpeeds():
    global forwardBackwardSpeed, leftRightSpeed;

    stringData = str(mode) + ',' + str(forwardBackwardSpeed) + ',' + str(leftRightSpeed)
    print("MODE 0 DATA :",stringData)

def generate_commands():
    global forwardBackwardSpeed,linear_velocity,angular_velocity,leftRightSpeed,width_chassi,radius_wheel;
    forwardBackwardSpeed = linear_velocity/radius_wheel
    leftRightSpeed = (angular_velocity*width_chassi)/(2*radius_wheel)
    print("generated forwardBackwardSpeed and leftRightSpeed")
def initialize():
    rospy.init_node('motor_socket',anonymous = True)
def listener():
    global linear_velocity,angular_velocity;
    msg = rospy.wait_for_message("/test",Int16)
    print(msg)

initialize()
while(1):
 listener()
 generate_commands()
 printSpeeds()
 sendDatatoRaspi()
