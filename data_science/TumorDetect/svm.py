# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:55:23 2020

@author: kevin
"""
import load_data 
load_data.load()
(X_train, X_test, Y_train, Y_test)=load_data.split()
#%%
from sklearn.svm import SVC
svm=SVC(probability=True,kernel='linear')
svm.fit(X_train,Y_train)

from sklearn import metrics
model_predicted=svm.predict(X_test)
accuracy = metrics.accuracy_score(Y_test,model_predicted)
print(svm.kernel,accuracy)
from sklearn.model_selection import cross_val_score
score=cross_val_score(svm,X_train,Y_train)
print(score.mean())
#%%


svm=SVC(probability=True)
svm.fit(X_train,Y_train)
from sklearn import metrics
model_predicted=svm.predict(X_test)
accuracy = metrics.accuracy_score(Y_test,model_predicted)
print(svm.kernel,accuracy)
score=cross_val_score(svm,X_train,Y_train)
print(score.mean())
#%%

from sklearn.svm import SVC
svm=SVC(probability=True,kernel='poly')
svm.fit(X_train,Y_train)

from sklearn import metrics
model_predicted=svm.predict(X_test)
accuracy = metrics.accuracy_score(Y_test,model_predicted)
print(svm.kernel,accuracy)
score=cross_val_score(svm,X_train,Y_train)
print(score.mean())

#%%

from sklearn.svm import SVC
svm=SVC(probability=True,kernel='sigmoid')
svm.fit(X_train,Y_train)

from sklearn import metrics
model_predicted=svm.predict(X_test)
accuracy = metrics.accuracy_score(Y_test,model_predicted)
print(svm.kernel,accuracy)
score=cross_val_score(svm,X_train,Y_train)
print(score.mean())
