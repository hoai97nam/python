import cv2
import numpy as np

img = cv2.imread('girl.jpg',-1)
cv2.line(img, (0,0) , (200,190), (25,100,90),2);
#truyen thong so buc anh
#ve tu toa do nao den toa do nao
#mau RGB
#do rong - tinh bang pixel
cv2.imwrite('dave.jpg', img);

cv2.destroyAllWindows()
