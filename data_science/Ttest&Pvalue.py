# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:10:39 2020

@author: kevin
"""
import numpy as np
from scipy import stats
A=np.random.normal(25,5,1000)
B=np.random.normal(26,5,1000)

print(stats.ttest_ind(A,B))
#%%
B=np.random.normal(25,5,10000)
print(stats.ttest_ind(A,B))
#%%
A=np.random.normal(25,5,100000)
B=np.random.normal(25,5,100000)
print(stats.ttest_ind(A,B))
print(stats.ttest_ind(A,A))

