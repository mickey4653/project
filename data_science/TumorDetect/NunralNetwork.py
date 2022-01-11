
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import pandas as pd
import numpy as np
from sklearn import preprocessing
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
# normalized

min_max_scaler = preprocessing.StandardScaler()
doc_std = min_max_scaler.fit_transform(doc)
doc= pd.DataFrame(doc_std,columns=head[:5])
#%%
#train test split
from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split( doc, Severity, test_size=0.3)
def model(optimizer):
    model=Sequential()

    model.add(Dense(128,input_shape=(5,  ),activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(16,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(8,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer=optimizer,metrics=['accuracy'])
    #驗證
    history=model.fit(X_train,Y_train,batch_size=5,epochs=10,verbose=0, validation_data=(X_test,Y_test))
    score=model.evaluate(X_test,Y_test,verbose=0)
    print(optimizer)
    print('Test loss:',score[0])
    print('Test accuracy',score[1])
    print('-------------')
#%%
model('SGD')
model('RMSprop')
model('Adam')

def showResult(num):
    x=np.array(X_test)[num]
    x=np.reshape(x,(1,5))
    print('content---',x)
    print('predicted---',model.predict_classes(x )    )
# showResult(1)   

    
