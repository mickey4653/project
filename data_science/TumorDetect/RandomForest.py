# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:22:23 2020

@author: kevin
"""
import load_data as load_doc
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

load_doc.load()
(X_train, X_test, Y_train, Y_test)=load_doc.split()
#%%

from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import  preprocessing, metrics
model = RandomForestClassifier(n_estimators=100, random_state=0)
# 　1) n_estimators: 也就是最大的弱学习器的个数。一般来说n_estimators太小，容易欠拟合，n_estimators太大，计算量会太大，并且n_estimators到一定的数量后，再增大n_estimators获得的模型提升会很小，所以一般选择一个适中的数值。默认是100。
model_fit=model.fit(X_train,Y_train)
model_predicted=model_fit.predict(X_test)
accuracy = metrics.accuracy_score(Y_test,model_predicted)
print(accuracy)
#%%
from sklearn.model_selection import cross_val_score
score=cross_val_score(model,X_train,Y_train)
print(score.mean())
