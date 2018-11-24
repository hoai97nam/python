import cv2
import numpy as np

img = cv2.imread('horse.jpg',1)
px = img[0][0]

print(px)

for i in range(640):
    for j in range (640):
        if img[i,j,0]>30:
            img[i,j]=100
cv2.imshow('pixel',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
