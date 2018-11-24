import numpy as np
from sklearn.utils import shuffle
from skimage import exposure

def preprocess_dataset(X,y=None):
    #convert to grayscale, single y channel
    x=0.029*X[:,:,:,0]+0.587*X[:,:,:,1]+0.114*X[:,:,:,2]
    #scale feature to be in [0,1]
    X=(X/255.).astype(np.float32)

    #apply localize histogram localization
    for i in range(X.shape[0]):
        X[i]=exposure.equalize_adapthist(X[i])


    if y is not None:

        y= np.eye(43)[y]
        #shuffle the data
        X,y = shuffle(X,y)

    #add a single grayscale channel
    X=X.reshape(X.shape+(1,))
    return X,y

import cv2

img=cv2.imread('bb3.jpg',1)
preprocess_dataset(img)
