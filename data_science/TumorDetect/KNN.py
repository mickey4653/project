# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:42:41 2020

@author: kevin
"""
import load_data as doc
from sklearn import neighbors
from sklearn import metrics
#%%
doc.load()
(X_train, X_test, Y_train, Y_test)=doc.split()

#%%
dic={}
for x in range(1,31):
    model=neighbors.KNeighborsClassifier(n_neighbors=x)
    model=model.fit(X_train,Y_train)
    
    model_predict=model.predict(X_test)
    accuracy=metrics.accuracy_score(Y_test, model_predict)
    dic[x]=accuracy
    print('K-',x,'accuracy=',accuracy)
import operator
best=max(dic.items(), key=operator.itemgetter(1))[0]
print('best k=',best,'accuracy=',dic[best])