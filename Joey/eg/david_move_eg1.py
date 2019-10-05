"""
Move Test

This program is responsible for testing whether the robot arm can be moved when requested
to by our program.
"""

import socket
import time

#Specify what we want to connect to
HOST = "192.168.1.6"
PORT = 30002

#Create a TCP/IP socket to send and receive information
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#State a connection has been established
print("Connection Established...")
time.sleep(2)
print("Beginning movement...")
mess = "movej(p[0.5, 0.3, 0.4, 2.22, -2.22, 0.00], a=1.0, v=0.1)" + "\n"
s.send(mess.encode())
time.sleep(10)

#Close the socket
s.close()