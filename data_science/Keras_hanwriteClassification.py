# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:11:49 2020

@author: kevin
"""

from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
# Sequential => nunural network
# Dense Dropout ->add del cells form network

(mnist_train_images,mnist_train_labels),(mnist_test_images,mnist_test_labels)=mnist.load_data()

train_images=mnist_train_images.reshape(60000,784)
test_images=mnist_test_images.reshape(10000,784)
train_images=train_images.astype('float')
test_images=test_images.astype('float')

# / 255 becauese  turn the scale into 0-1
train_images /=  255
test_images /=  255

# turn the labels to one hot ex 1-3 and value =2 -> (0,1,0)
train_labels=keras.utils.to_categorical(mnist_train_labels,10)
test_labels=keras.utils.to_categorical(mnist_test_labels,10)


import matplotlib.pyplot as plt
def display_sample(num):
    # print in one hot 
    print(train_labels[num])
    #print the label and convert back to a num
    # np.argmax() 返回最大值索引號
    label=train_labels[num].argmax(axis=0)#get one hot code label
    image=train_images[num].reshape([28,28])
    plt.title('Sampke %d Label %d'%(num,label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()
display_sample(1234)    

model=Sequential()
model.add(Dense(512,activation='relu',input_shape=(784,)))
model.add(Dense(10,activation='softmax')  )  
model.summary()
# verbose = 0，在控制台没有任何输出
# verbose = 1 ：显示进度条
# verbose =2：为每个epoch输出一行记录
model.compile(loss='categorical_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])
#驗證
history=model.fit(train_images,train_labels,batch_size=100,epochs=10,verbose=1, validation_data=(test_images,test_labels))
score=model.evaluate(test_images,test_labels,verbose=0)
print('Test loss:',score[0])
print('Test accuracy',score[1])
#%%
#error one
for x in range(1000):
    test_image=test_images[x,:].reshape(1,784)
    predicted_cat=model.predict(test_image).argmax()
    label=test_labels[x].argmax()
    if(predicted_cat != label):
        plt.title('Prediction: %d Label %d'%(predicted_cat,label))
        plt.imshow(test_image.reshape([28,28]),cmap=plt.get_cmap('gray_r'))
        plt.show()
        
        
        