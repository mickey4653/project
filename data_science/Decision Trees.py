# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:26:25 2020

@author: kevin
"""

import numpy as np
import pandas as pd
from sklearn import tree
input_file="C:/Users\kevin\Desktop\code\data_science\MLCourse\PastHires.csv"
df=pd.read_csv(input_file,header=0)
#print(  df.head()   )
#%%
d={'Y':1,'N':0}
df['Hired']=df['Hired'].map(d)
df['Employed?']=df['Employed?'].map(d)
df['Top-tier school']=df['Top-tier school'].map(d)
df['Interned']=df['Interned'].map(d)
d={'BS':0,'MS':1,'PhD':2}
df['Level of Education']=df['Level of Education'].map(d)
#print(df.head())
#%%
features=list(df.columns[:6])
y=df["Hired"]
X=df[features]
clf=tree.DecisionTreeClassifier()
clf.fit(X,y)
#%%
#display
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydot
import matplotlib.pyplot as plt
dot_data=StringIO()
tree.export_graphviz(clf,out_file=dot_data,feature_names=features)
(graph,)=pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("Enployed.pdf") 
#gini point-> entropy-> variency of data
#sample-> numbers remaining(excluded)
#values[0. 5.] -> left 0 right 5
#%%
#Random Forest
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=10)
clf=clf.fit(X,y)
print(clf.predict(  [[10,1,4,0,0,0]]    ))
print(clf.predict(  [[10,0,4,0,0,0]] ))
