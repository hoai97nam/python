import cv2
import numpy as np

img = cv2.imread('fuck.jpg',1)
res = cv2.resize(img,None,fx=2,fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow('resize',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


        
