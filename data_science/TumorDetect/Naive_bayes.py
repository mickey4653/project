# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:36:28 2020

@author: kevin
"""

import load_data as load_doc
load_doc.load()
(X_train, X_test, Y_train, Y_test)=load_doc.split()
#%%
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
model = GaussianNB()
model.fit(X_train, Y_train)
model_Y=model.predict(X_test)
accuarcy=metrics.accuracy_score(Y_test,model_Y)
print(accuarcy)