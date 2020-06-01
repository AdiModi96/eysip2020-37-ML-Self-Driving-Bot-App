
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical
import random
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.models import load_model
np.random.seed(0)



(X_train,y_train),(X_test,y_test)=mnist.load_data()             #loads MNSIT Data

num_pixel=28*28
X_train=X_train.reshape(X_train.shape[0],28,28,1)
X_test=X_test.reshape(X_test.shape[0],28,28,1)
X_test.shape
X_train=X_train/255
X_test=X_test/255

y_test=to_categorical(y_test)
y_train=to_categorical(y_train)

model=load_model('model_digits.h5')



import cv2
import numpy as np

drawing=False # true if mouse is pressed
mode=True # if True, draw rectangle.

def interactive_drawing(event,x,y,flags,param):       #function to draw digit using mouse drag
    global ix,iy,drawing, mode

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.circle(img,(x,y),12,(255,255,255),-100)
                #print x,y
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.circle(img,(x,y),12,(255,255,255),-100)
            #print x,y
            #cv2.line(img,(x,y),(x,y),(0,0,255),10)
    return x,y




img = np.zeros((300,300,3), np.uint8)

cv2.namedWindow('output')
cv2.setMouseCallback('output',interactive_drawing)
while(1):
    cv2.imshow('output',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
cv2.imwrite('test.jpg',img)
cv2.destroyAllWindows()

img = cv2.imread("test.jpg")
plt.imshow(img, cmap=plt.get_cmap('gray'))




img=np.asarray(img)
img=cv2.resize(img,(28,28))
print(img.shape)
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img,cmap=plt.get_cmap('gray'))
img=img/255
img=img.reshape(1,28,28,1)
print('The number is :',str(model.predict_classes(img)[0]))
