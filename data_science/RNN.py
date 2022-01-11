# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:08:23 2020

@author: kevin
"""


from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Embedding
from tensorflow.keras.layers import LSTM
# lstm long sort memory cell

from tensorflow.keras.datasets import imdb

(x_train,y_train),(x_test,y_test)=imdb.load_data(num_words=20000)
# num_word=how many unique word loaded
# 20000 most popular words
#%%
# RNN网络容易出现反向传播过程中的梯度问题。主要原因是我们通常给RNN的参数为有限的序列。
# 为了实现的简便，keras只能接受长度相同的序列输入。因此如果目前序列长度参差不齐，这时需要使用pad_sequences()。该函数是将序列转化为经过填充以后的一个新序列。
x_train=sequence.pad_sequences(x_train,maxlen=80)
x_test=sequence.pad_sequences(x_test,maxlen=80)
# look at first 80 words

model=Sequential()
# converts the input data into dense vectors fo fixed size 
# that better suited for a neural network

model.add(Embedding(20000,128))
model.add(LSTM(128,dropout=0.2,recurrent_dropout=0.2))
model.add(Dense(1,activation='sigmoid'))

#%%
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=32,epochs=5,verbose=2,
          validation_data=(x_test,y_test)
          )
score,acc=model.evaluate(x_test,y_test,batch_size=32)
print("test score:",score)
print("test accuracy:",acc)