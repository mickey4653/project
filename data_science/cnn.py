# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:03:48 2020

@author: kevin
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
(x_tain, y_train),(x_test,y_test)=mnist.load_data()
x_train=x_tain.reshape(60000,28,28,1)
x_test=x_test.reshape(10000,28,28,1)
#%
from keras.utils import np_utils
y_train=np_utils.to_categorical(y_train,10)
y_test=np_utils.to_categorical(y_test,10)
 #%%
from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten
from keras.layers import Conv2D,MaxPooling2D
from keras.optimizers import SGD
#%%
model=Sequential()
model.add(  Conv2D( 32, (3,3), padding='same', input_shape=(28,28,1)  ) )
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size= (2,2) ))


model.add(Conv2D(64, (3,3), padding="same" ) )#filter will be more & don't need input size
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size= (2,2) ))

model.add(Conv2D(128, (3,3), padding="same" ) )#filter will be more & don't need input size
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size= (2,2) ))
#%%
model.add(Flatten())

model.add(Dense(200))
model.add(Activation('relu'))

model.add(Dense(10))
model.add(Activation('softmax'))
#%%
model.compile(loss='mse',optimizer=SGD(lr=0.1), metrics=['accuracy'])
#%%
model.fit(x_train,y_train, batch_size=100, epochs=12)

#%%

model_json=model.to_json()

open("handwriting_model.jason", "w").write(model_json)

model.save_weights("handwritting_model_weights.h5")
#%%
predict=model.predict_classes(x_test)
pick=np.random.randint(1,999,5)
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(x_test[pick[i]].reshape(28,28),cmap='Greys')
    plt.title(predict[pick[i]])
    plt.axis("off")