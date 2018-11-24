import cv2
import numpy as np

img = cv2.imread('horse.jpg',1)
px = img[0][0]

print(px)

for i in range(100):
    img[i][i] = [1,1,1]
    img[i+1][i] = [1,1,1]
cv2.imshow('pixel',img)

cv2.waitKey(0)
v2.destroyAllWindows()
