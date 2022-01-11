# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:32:01 2020

@author: kevin
"""
def createClusterData(N, k):
    np.random.seed(10)
    pointsPerCluster=float(N)/k
    X=[]
    for i in range(k):
        incomeCentroid=np.random.uniform(20000.0,200000.0)#均衡分布
        ageCentroid=np.random.uniform(20.0,70.0)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid,10000.0),np.random.normal(ageCentroid,20.0)])
    X=np.array(X)
    return X

import numpy as np
from sklearn.cluster import KMeans
import matplotlib .pyplot as plt
from sklearn.preprocessing import scale
data=createClusterData(100,7)
model=KMeans(n_clusters=5)
model=model.fit(scale(data))
print(len(data))
#print(model.labels_)
plt.figure(figsize=(8,6))
plt.scatter(data[:,0],data[:,1], c=model.labels_.astype(np.float) )
plt.show()