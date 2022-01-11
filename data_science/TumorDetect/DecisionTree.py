# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:49:40 2020

@author: kevin
"""
from sklearn import tree
import pandas as pd
head=(['BI-RADS-Assessment','Age','Shape','Margin','Density','Severity'])
doc=pd.read_csv('../MLCourse/mammographic_masses.data.txt',na_values='?',header=None)
doc.columns=head
# doc=doc.dropna()
Severity=doc['Severity']
doc.drop('Severity',axis=1, inplace=True)

# doc.drop('column_name',axis=1, inplace=True)
# check doc.std()/doc.mean()

doc=doc.fillna(doc.std())


#%%
from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split( doc, Severity, test_size=0.3)

Dtree = tree.DecisionTreeClassifier(max_depth=5)
Dtree = Dtree.fit(X_train,Y_train)
#%%
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydot
import matplotlib.pyplot as plt
# An in-memory stream for unicode text. It inherits TextIOWrapper.
# StringIO, that reads and writes a string buffer 
document=StringIO()
tree.export_graphviz(Dtree,out_file=document,feature_names=head[:5])
(graph,)=pydot.graph_from_dot_data(document.getvalue())
graph.write_pdf("./Tumor.pdf") 
#%%
from sklearn import metrics
tree_predicted=Dtree.predict(X_test)
accuracy = metrics.accuracy_score(Y_test, tree_predicted)
print(accuracy)

#%%
from sklearn.model_selection import cross_val_score
score=cross_val_score(Dtree,X_train,Y_train)
print(score.mean())