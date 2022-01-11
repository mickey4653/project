# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:18:52 2020

@author: OSA
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np 
r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv('../MLCourse/ml-100k/u.data',sep='\t', names=r_cols,usecols=range(3))
m_cols=['movie_id','title']
movies=pd.read_csv('../MLCourse/ml-100k/u.item',sep='|', names=m_cols,usecols=range(2))
ratings=pd.merge(movies,ratings)
# print(ratings.head())
#%%
userRatings=ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
# print(userRatings.head())
corrMatrix=userRatings.corr(method='pearson',min_periods=100)
# print(corrMatrix.head())
myRatings=userRatings.loc[0].dropna()
#.loc-> select value
#dropna-> deal with missing value
# print(type(myRatings)   )
simCandidates=pd.Series()
for i in range(0,len(myRatings.index)):
    # print("Adding sims for",myRatings.index[i],".....")
    sims=corrMatrix[ myRatings.index[i].dorpna() ]
    sims=sims.map(lambda x:x*myRatings[i])
    #lambda：它允许你快速定义单行的最小函数  simCandidates=simCandidates.append(sims)
simCandidates.sort_values(inplace=True,ascending=False)
# print(simCandidates.head(10))
simCandidates=simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace=True,ascending=False)
# print(simCandidates.head(10))
filterSims=simCandidates.drop(myRatings.index)
#drop seen movie
print(filterSims.head(10))