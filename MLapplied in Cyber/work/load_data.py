# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:41:30 2021

@author: kevin
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from imblearn.over_sampling import KMeansSMOTE

def load():
    df = pd.read_csv("creditcard.csv", header=0)
    # df = pd.read_csv("small_creditcard.csv", header=0)
    y = df.iloc[:,-1].values
    X = df.iloc[:, 1:-2].values
    
    
    #%%
    # # We need to normalize the the dataset
    standard_scaler = StandardScaler()
    X= standard_scaler.fit_transform(X)
    # ratio=(y[y==1]).sum()/(y[y==0]).sum()
    km = KMeansSMOTE(k_neighbors=2,random_state=0,n_jobs=-1,cluster_balance_threshold=0.0017304750013189597)
    X,y = km.fit_resample(X, y)
    X = PCA(n_components=2).fit_transform(X)
   
   
        
    plt.title('class 0')
    plt.xlim(X.min(),X.max())
    plt.ylim(y.min(),y.max())
    plt.scatter(X[y==0][:,0],X[y==0][:,1])
    plt.show()
    
    plt.xlim(X.min(),X.max())
    plt.ylim(y.min(),y.max())
    plt.scatter(X[y==1][:,0],X[y==1][:,1])
    plt.title('class 1')
    plt.show()
    
    return X,y
if __name__=="__main__":
    X,y=load()