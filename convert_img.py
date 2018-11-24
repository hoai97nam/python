import cv2
import numpy as np

img =cv2.imread('people.jpg',1)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('hsv',hsv)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
