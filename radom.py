import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
ketqua = np.random.randint(0,2,(25,1)).astype(np.float32)

red = trainData[ketqua.ravel()==1]
blue = trainData[ketqua.ravel()==0]
newmember = np.random.randint(0,2,(1,2)).astype(np.float32)

plt.scatter(red[:,0],red[:,1],100, 'r','*')
plt.scatter(blue[:,0],blue[:,1],100, 'b','X')
plt.scatter(newmember[:,0],newmember[:,1],100,'k','^')

knn = cv2.ml.KNearest_create()  #khoi tao
knn.train(trainData,0,ketqua)
temp, kq,hangxom,khoangcach = knn.findNearest(newmember,3)

print ("kq: {}\n".format(kq))
print ("hangxom: {}\n".format(hangxom))
print ("khoangcach: {}\n".format(khoangcach))

                
plt.show()
