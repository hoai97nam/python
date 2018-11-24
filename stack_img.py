import cv2
import numpy as np
img = cv2.imread('girl.jpg',cv2.IMREAD_COLOR)

img[55,55] = [255,255,255] # cho 1 vung mau trang
px = img[55,55] # gan bien px cho vung mau trang do


img[100:150,100:150] = [255,255,255] #cho 1 cung khac mau trang

face = img[37:111,107:194] #gan 1 vung cho bien face
img[0:74,0:87] = face   # and face va img voi nhau
#dieu kien la phaicung kich co

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




