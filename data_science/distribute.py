# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:19:41 2020

@author: kevin
"""
import numpy as np
#random number(num,standard deviation,datapoints )
income=np.random.normal(27000,15000,1000)
print("mean=",np.mean(income)   )
print( "median=",np.median(income))
import matplotlib.pyplot as plt
plt.hist(income,50)
plt.show()

#extreme value
income=np.append(income,100000000000)

print("mean=",np.mean(income)   )
print( "median=",np.median(income))