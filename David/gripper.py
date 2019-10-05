import socket
import time

#Specify what we want to connect to
HOST = "192.168.1.6"
PORT = 30002

#Create a TCP/IP socket to send and receive information
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


f = open ("gripper_tutorial2.script", "rb")  #Robotiq FT sensor

l = f.read(1024)
while (l):
   s.send(l)
   l = f.read(1024)
s.close()
