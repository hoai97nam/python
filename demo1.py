import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame =  cap.read()

    #convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # threshold the HSV image to get only the blue color
    mask = cv2.inRange(hsv, lower_blue,upper_blue)

    #Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k ==27:
        break

cv2.destroyAllWindows()
