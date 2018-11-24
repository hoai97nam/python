import cv2
import numpy as np

img = cv2.imread('girl.jpg',1)

px = img[55,55]
print(px)
