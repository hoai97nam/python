import cv2
import numpy as np

img1 = cv2.imread('people.jpg',1)
img2 = cv2.imread('fuck.jpg',1)

img2 = img2[0:189,0:267]

mix = cv2.add(img1,img2)

cv2.imshow('f*ck',mix)
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
