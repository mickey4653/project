import os
import io
import numpy as np
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#%%
def readfiles(path):
    for root, dirnames,filenames in os.walk(path):#os walk recusive walk trough the path
        for filenames in filenames:
            path=os.path.join(root,filenames)
            
            inBody=False
            lines=[]
            f=io.open(path,'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line=="\n":
                    inBody=True
            f.close()
            message='\n'.join(lines)
            yield path,message
def dataFrameFromDirectory(path, classification):
    rows=[]
    index=[]
    for filename, message in readfiles(path):
        rows.append(    {'message':message,'class':classification}  )
        index.append(filename)
    return DataFrame(rows,index=index)
data =DataFrame(    {'message':[], 'class':[]})
data=data.append(dataFrameFromDirectory('D:\kevin\code\data_science\MLCourse\emails\spam','spam'))
data=data.append(dataFrameFromDirectory('D:\kevin\code\data_science\MLCourse\emails\ham','ham'))
#%%
#print(  data.head()     )
vectorizer=CountVectorizer()
counts=vectorizer.fit_transform( data['message'].values   )
print(counts)
"""fit(): Method calculates the parameters μ and σ and saves them as internal objects.
解释：简单来说，就是求得训练集X的均值，方差，最大值，最小值,这些训练集X固有的属性。

transform(): Method using these calculated parameters apply the transformation to a particular dataset.
解释：在fit的基础上，进行标准化，降维，归一化等操作（看具体用的是哪个工具，如PCA，StandardScaler等）。

fit_transform(): joins the fit() and transform() method for transformation of dataset.
解释：fit_transform是fit和transform的组合，既包括了训练又包含了转换。
"""
classifier=MultinomialNB()
targets=data['class'].values
classifier.fit(counts,targets)   

examples=['Free Viagra now!!!',"Hi Bob, how about a game of golf tomorrow?"]
example_counts=vectorizer.transform(examples)
prediction=classifier.predict(example_counts)
print(prediction)