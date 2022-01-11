# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:15:32 2020

@author: kevin
"""

import tensorflow
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Conv2D,MaxPooling2D,Flatten
from tensorflow.keras.optimizers import RMSprop


(mnist_train_images,mnist_train_labels),(mnist_test_images,mnist_test_labels)=mnist.load_data()

from tensorflow.keras import backend as K
# width*hight*color channel
if K.image_data_format()=='channels_first':
        train_images=mnist_train_images.reshape(mnsit_train_images.shape[0],1,28,28)
        test_images=mnist_test_images.reshape(mnist_test_images.shape[0],1,28,28)
        input_shape=(1,28,28)
else:
    train_images=mnist_train_images.reshape(mnist_train_images.shape[0],28,28,1)
    test_images=mnist_test_images.reshape(mnist_test_images.shape[0],28,28,1)
    input_shape=(28,28,1)
train_images=train_images.astype('float32')
test_images=test_images.astype('float32')
train_images/=255
test_images/=255

#%%
train_labels=tensorflow.keras.utils.to_categorical(mnist_train_labels,10)
test_labels=tensorflow.keras.utils.to_categorical(mnist_test_labels,10)

import matplotlib.pyplot as plt
def display_sample(num):
    print(train_labels[num])
    label=train_labels[num].argmax(axis=0)
    image=train_images[num].reshape(28,28)
    plt.title('Sample:%d Label:%d '%    (num,label))
    plt.imshow(image,cmap=plt.get_cmap('gray_r'))
    plt.show()
# display_sample(1234)    
#%%
model=Sequential()
# Param=(kernalsize-> 3*3 +1# bias)* neurals->32
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=input_shape))
# 64 3*3 kernels
model.add(Conv2D(64,(3,3),activation='relu'))

# reduce by taking the max of each 2*2 block
# diff from kernel size -> shrink the size
model.add(MaxPooling2D(pool_size=(2,2)))
#  fraction 0-1
model.add(Dropout(0.25))
# Flatten the results to one dimension to pass into final layer
# 2d-> 1D
model.add(Flatten())
# hidden layer
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
#%%
history=model.fit(train_images,train_labels,batch_size=32,
                  epochs=10,
                  verbose=2,
                  validation_data=(test_images,test_labels))
#%%
score=model.evaluate(test_images,test_labels,verbose=0)
print('Test loss:',score[0])
print('Test accuracy',score[1])
