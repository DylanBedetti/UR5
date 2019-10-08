import cv2
import requests
import shutil
import time
import urx

#This is the image url.
image_url = "http://192.168.1.6:4242/current.jpg?annotations=off"
# Open the url image, set stream to True, this will return the stream content.
count = 0
count1 = 0

    #rob.set_freedrive(1,timeout = 60)
    #time.sleep(10);

while(1):
    resp = requests.get(image_url, stream=True)
    # Open a local file with wb ( write binary ) permission.
    img_string = 'local_image_v2_' + str(count) + '.jpg'
    local_file = open(img_string, 'wb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    # Remove the image url response object.
    del resp

    img = cv2.imread(img_string,cv2.COLOR_BGR2RGB)
    cv2.imshow('image',img)
    #count+=1
    #if count == 10:
    #    break
    #cv2.waitKey(0)
    if(cv2.waitKey(0)):
       count+=1
       if(count==50):
           break
cv2.destroyAllWindows()