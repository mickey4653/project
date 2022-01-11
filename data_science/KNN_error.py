# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:19:42 2020

@author: OSA
"""


import pandas as pd
import numpy as np 
r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv('./MLCourse/ml-100k/u.data',sep='\t', names=r_cols,usecols=range(3))
movieProperties=ratings.groupby('movie_id').agg({'rating':[np.size,np.mean]})
# print(movieProperties.head())
movieNumRatings=pd.DataFrame(movieProperties['rating']['size'])
#lambda like a small function
movieNormalizedNumRatings=movieNumRatings.apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x)))
# print(movieNormalizedNumRatings.head())

#%%
movieDict={}
with open(r'./MLCourse/ml-100k/u.item',encoding='UTF-8')as f:
    temp=''
    for line in f :
        fields=line.rstrip('\n').split("|")
        movieID=int(fields[0])
        name=fields[1]
        genres=fields[5:25]
        genres=map(int,genres)
        movieDict[movieID]=(name, genres,movieNormalizedNumRatings.loc[movieID].get('size')
                            ,movieProperties.loc[movieID].rating)
from scipy import spatial
def ComputeDistance(a,b):#a movieID b Movie
    try:
        genreA=list(a[1])
        genreB=list(b[1])
        genreDistance=spatial.distance.cosine(genreA,genreB)
        #compute the cosine(余璇) distance
    except ValueError:
        genreDistance=0
        print(len(genreA),len(genreB)   )
    popularityA=a[2]
    popularityB=b[2]
    X=a[2]
    Y=b[2]
    
    print("Y",Y)#,len(Y),Y)
    print("X",X)#len(X),X)
    popularityDistance=abs(popularityA-popularityB)
    #abs絕對值
    return genreDistance+popularityDistance
# print(ComputeDistance(movieDict[2],movieDict[4])    )
#%%
import operator
def getNeighbors(movieID,K):
    distances=[]
    for movie in movieDict:
        if(movie!=movieID):
            X=movieDict[movieID]
            Y=movieDict[movie]
            dist=ComputeDistance(X,Y)
            distances.append((movie,dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(K):
        neighbors.append(distances[x][0])
        return neighbors
K=10
avgRating=0
neighbors=getNeighbors(1,K)
for neighbor in neighbors:
    avgRating+=movieDict[neighbor][3]
    print(movieDict[neighbor[0]]+""+str(movieDict[neighbor][3]))
avgRating/=float(K)