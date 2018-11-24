import cv2
import numpy as np

# thay doi gia tri 1 diem anh
#img = np.uint8([[[232,162,0]]])
#hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#print(hsv_img)


# convert an image
img = cv2.imread('color.jpg',1)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# tao mat na
min_mau = np.array([50,192,122])
max_mau = np.array([55,192,122])
mask = cv2.inRange(hsv_img,min_mau,max_mau)
final = cv2.bitwise_or(img,img,mask=mask)
cv2.imshow('mask',final)

cv2.waitKey(0)
