import cv2
import numpy as np
img = cv2.imread('fuck.jpg', 1)

subimg = img[200:300,200:1000]

cv2.imshow('anhcat',subimg)
subimg = subimg[:,:,2]

# thong so anh
print(subimg.shape) # kich co anh
print(subimg.size) # dung luong anh
print(subimg.dtype) # loai anh

cv2.waitKey(0)
cv2.destroyAllWindows()


 
