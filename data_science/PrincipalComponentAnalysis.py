# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:14:24 2020

@author: kevin
"""
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

iris=load_iris()
numSamples,numFeatures=iris.data.shape
X=iris.data
pca=PCA(n_components=2,whiten=True).fit(X)
#n_components-->2 dimensions
#whiten=true-->normalized
X_pca=pca.transform(X)
#transform data
print(pca.components_)
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
colors=cycle('rgb')
target_ids=range(len(iris.target_names))
#range(3)-->1,2,3
pl.figure()
for i, c ,label in zip(target_ids, colors ,iris.target_names):
    #iterate i index of target_ids
    pl.scatter(X_pca[iris.target==i,0],X_pca[iris.target==i,1],
               c=c,label=label)
pl.legend()
#The elements to be added to the legend are automatically determined,
pl.show()