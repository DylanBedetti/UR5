"""
Move Test

This program is responsible for testing whether the robot arm can be moved when requested
to by our program.
"""

import socket
import time
import cv2
import requests
import shutil

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

# This is the image url.
# image_url = "http://192.168.1.6:4242/current.jpg?annotations=off"
# # Open the url image, set stream to True, this will return the stream content.
# count = 0
# count1 = 0
# while(1):
#     resp = requests.get(image_url, stream=True)
#     # Open a local file with wb ( write binary ) permission.
#     img_string = 'local_image_' + str(count) + '.jpg'
#     local_file = open(img_string, 'wb')
#     # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
#     resp.raw.decode_content = True
#     # Copy the response stream raw data to local image file.
#     shutil.copyfileobj(resp.raw, local_file)
#     # Remove the image url response object.
#     del resp

#     img = cv2.imread(img_string,cv2.COLOR_BGR2RGB)
#     cv2.imshow('image',img)
#     #count+=1
#     #if count == 10:
#     #    break
#     #cv2.waitKey(0)
#     if(cv2.waitKey(0)):
#        count+=1
#        if(count==50):
#            break
# cv2.destroyAllWindows()
s.close()
