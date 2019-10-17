import numpy as np 
import cv2

def get_pixel(event,x,y,flags,param):
    global refPt1,refPt2,max_H,max_S,max_V,min_H,min_S,min_V
    #count = 0
    
    #print 'it worked'
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img,(x,y),100,(255,0,0),-1)
        refPt1 =[(x,y)]
        #print "x coord: " + str(mouseX)
        #print "y coord: " + str(mouseY)
        #print "hsv: " + str(HSV_img[mouseY,mouseX])
    elif event == cv2.EVENT_LBUTTONUP:
        refPt2 =[(x,y)]
        dist = int(np.sqrt((refPt2[0][0]-refPt1[0][0])**2+(refPt2[0][1]-refPt1[0][1])**2))
        print dist
        cv2.circle(img,refPt1[0],dist,(0,255,0),2)
        max_H = HSV_img[refPt1[0][1]][refPt1[0][0]][0]
        max_S = HSV_img[refPt1[0][1]][refPt1[0][0]][1]
        max_V = HSV_img[refPt1[0][1]][refPt1[0][0]][2]
        min_H = HSV_img[refPt1[0][1]][refPt1[0][0]][0]
        min_S = HSV_img[refPt1[0][1]][refPt1[0][0]][0]
        min_V = HSV_img[refPt1[0][1]][refPt1[0][0]][0]
        for i in range(-dist,dist):
            for j in range(-dist,dist):
                print "H: " + str(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][0]) + " S: " + str(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][1]) + " V: " + str(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][2])
                if HSV_img[refPt1[0][1]][refPt1[0][0]][0] - 10 < HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][0]:
                    min_H = min(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][0],min_H)
                    min_S = min(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][1],min_S)
                    min_V = min(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][2],min_V)
                    max_S = max(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][1],max_S)
                    max_V = max(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][2],max_V)

                if HSV_img[refPt1[0][1]][refPt1[0][0]][0] + 10 > HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][0]:
                    max_H = max(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][0],max_H)
                    min_S = min(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][1],min_S)
                    min_V = min(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][2],min_V)
                    max_S = max(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][1],max_S)
                    max_V = max(HSV_img[refPt1[0][1]+i][refPt1[0][0]+j][2],max_V)
        print "H: " + str(min_H) + ", " + str(max_H)
        print "S: " + str(min_S) + ", " + str(max_S)
        print "V: " + str(min_V) + ", " + str(max_V)
        
cv2.namedWindow('detect_HSV')
cv2.setMouseCallback('detect_HSV',get_pixel)
cv2.startWindowThread()
img = cv2.imread('image.jpg')

HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV image', HSV_img)
ret = 0
while(1):
    cv2.imshow('detect_HSV',img)
    k = cv2.waitKey(20) & 0xFF
#     if k == ord('a'):
#     print "x coord: " + str(mouseX)
#     print "y coord: " + str(mouseY)
#     print "hsv: " + str(HSV_img[mouseX,mouseY])
    if k == ord('q'):
        break
    elif ret == 1:
        break
cv2.destroyWindow('detect_HSV')
cv2.waitKey(1)

