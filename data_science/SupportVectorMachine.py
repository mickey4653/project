# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:57:37 2020

@author: kevin
"""
import numpy as np
def createClusterData(N,k):
    np.random.seed(10)
    pointPerCluster=float(N)/k
    X=[]
    y=[]
    for i in range(k):
        incomeCentroid=np.random.uniform(20000.0,200000.0)
        ageCentroid=np.random.uniform(20.0,70.0)
        for j in range(int(pointPerCluster)):
            X.append([  np.random.normal(incomeCentroid,10000.0),np.random.normal(ageCentroid,2.0) ])
            #loc, scale
            y.append(i)
    X=np.array(X)
    y=np.array(y)
    return X,y
#%%
from matplotlib import *
from sklearn.preprocessing import MinMaxScaler
(X,y)=createClusterData(100,5)
plt=pyplot
# plt.figure(figsize=(8,6))
# plt.scatter(X[:,0],X[:,1],c=y.astype(np.float))
# plt.show()
scaling=MinMaxScaler(feature_range=(-1,1)).fit(X)
#scale between -1 1
X=scaling.transform(X)
# plt.figure(figsize=(8,6))
# plt.scatter(X[:,0],X[:,1],c=y.astype(np.float))
# plt.show()
#%%
from sklearn import svm,datasets
C=1.0
svc=svm.SVC(kernel='linear',C=C).fit(X,y)
def plotPredictions(clf):
    xx,yy=np.meshgrid(  np.arange(-1,1,.001),np.arange(-1,1,.001))
    #convert to np array
    npx=xx.ravel()
    npy=yy.ravel()
    #convert a lit of 2D
    samplePoints=np.c_[npx,npy]
    
    Z=clf.predict(np.array(samplePoints)    )
    plt.figure(figsize=(8,6))
    Z=Z.reshape(xx.shape)
    plt.contour(xx,yy,Z,cmap=plt.cm.Paired,alpha=0.8)
    plt.scatter(X[:,0],X[:,1],c=y.astype(np.float))
    plt.show()
plotPredictions(svc)
print(svc.predict(scaling.transform([[200000,40]])))
    