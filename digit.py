import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('digit.jpg',0)
cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]


print(cells[0][0])
