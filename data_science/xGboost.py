# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:52:29 2020

@author: kevin
"""
from sklearn.datasets import load_iris
iris=load_iris()
numSample,numFeatures=iris.data.shape
# print(numSample)
# print(numFeatures)
# print(list(iris.target_names))
#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=0)
#random state->every time excecute get the same resualt
#%%
import xgboost as xgb

train=xgb.DMatrix(x_train,label=y_train)
test=xgb.DMatrix(x_test,label=y_test)

parm={
      'max_depth':4,
      'eta':0.3,
      'objective':'multi:softmax',
      'num_class':3
      }
epochs=10
model=xgb.train(parm,train,epochs)
predictions=model.predict(test)
#%%
from sklearn.metrics import accuracy_score

score=accuracy_score([1],[1])#(y_test , predictions)
print(score   )

