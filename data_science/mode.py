# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:37:47 2020

@author: kevin
"""
import numpy as np
ages=np.random.randint(18, high=90,size=500)
from scipy import stats
print(stats.mode(ages)    )
