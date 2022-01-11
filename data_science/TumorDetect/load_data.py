# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:41:46 2020

@author: kevin
"""
       
def load():
        from sklearn import tree
        import pandas as pd
        from sklearn import preprocessing
        global doc,Severity 
        head=(['BI-RADS-Assessment','Age','Shape','Margin','Density','Severity'])
        doc=pd.read_csv('../MLCourse/mammographic_masses.data.txt',na_values='?',header=None)
        doc.columns=head
        # doc=doc.dropna()
        Severity=doc['Severity']
        doc.drop('Severity',axis=1, inplace=True)
        
        min_max_scaler = preprocessing.StandardScaler()
        doc_std = min_max_scaler.fit_transform(doc)
        doc= pd.DataFrame(doc_std,columns=head[:5])
        
def split():
        global doc,Severity    
        doc=doc.fillna(doc.mean())
        from sklearn.model_selection import train_test_split 
        X_train, X_test, Y_train, Y_test = train_test_split( doc, Severity, test_size=0.3)
        return X_train, X_test, Y_train, Y_test