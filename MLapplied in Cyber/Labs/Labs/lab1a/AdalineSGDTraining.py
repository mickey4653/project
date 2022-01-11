import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from AdalineSGD import AdalineSGD
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split

def plot_decision_regions(X_train,y_train,X_test,y_test,classifier, resolution=0.02):

    # setup marker generator and color map
    markers = ('s','x','o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    labels=['Iris-setosa','Iris-versicolor',' Iris-virginica']
    cmap = ListedColormap(colors[:len(np.unique(y_test))])

    # plot the decision surface
    x1_min, x1_max =  X_train[:,0].min() - 1, X_train[:, 0].max() +1
    x2_min, x2_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                            np.arange(x2_min, x2_max, resolution))

    Z = classifier.predict(   np.array([xx1.ravel(), xx2.ravel()]).T   )
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha=.7, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
 
    #plot class samples
    for idx, c1 in enumerate(np.unique(y_test)):
        plt.scatter(
                    # x=X[y == c1, 0],
                    # y=X[y == c1, 1],
                    # X[x pos,y pos]
                    x=X_test[y_test == c1,0],
                    y=X_test[y_test == c1,1],                    
                    alpha=.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=labels[c1],
                    edgecolor='black'
                    )
  
df = pd.read_csv("iris.data", header=None)


# df.tail()

# print(df.tail())

# select setosa and versicolor
y = df.iloc[:, 4].values
y[y == 'Iris-setosa'] = 0
y[y == 'Iris-versicolor'] = 1
y[y == 'Iris-virginica'] = 2

# extract the four iris features for each of the samples to build the sample set X
X = df.iloc[:, [0, 2]].values




# extract sepal length and petal length
# extract features
# X = df.iloc[0:len(df), [0, 2]].values

X_train, X_test ,y_train, y_test= train_test_split(X, y,test_size=0.3, random_state = 20, shuffle=True)       




# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,4))
#
# ada1 = AdalineGD(n_iter=10, eta= 0.01).fit(X,y)
#
# ax[0].plot(range(1,len (ada1._cost)+1),
#            np.log10(ada1._cost),
#            marker='o')
#
# ax[0].set_xlabel('Epochs')
# ax[0].set_ylabel('log(Sum-squared-error)')
#
# ax[0].set_title('Adaline = Learning rate 0.01')
#
# ada2 = AdalineGD(n_iter=15, eta= 0.01).fit(X,y)
#
# ax[1].plot(range(1,len (ada2._cost)+1),
#            np.log10(ada2._cost),
#            marker='o')
#
# ax[1].set_xlabel('Epochs')
# ax[1].set_ylabel('log(Sum-squared-error)')
#
# ax[1].set_title('Adaline = Normalized with Learning rate 0.01')
#
#
#
# plt.show()
#
# pass
#
# plt.close()


#=================Standardized data ######################

X_std = np.copy(X_train)

X_std[:,0] = (X_std[:,0] - X_std[:,0].mean()) / (X_std[:,0].std())
X_std[:,1] = (X_std[:,1] - X_std[:,1].mean()) / (X_std[:,1].std())
# testing
X_test[:,0] = (X_test[:,0] - X_test[:,0].mean()) / (X_test[:,0].std())
X_test[:,1] = (X_test[:,1] - X_test[:,1].mean()) / (X_test[:,1].std())

ada = AdalineSGD(n_iter=35, eta= 0.01, random_state=1).fit(X_std,y_train)
# eta learning rate


plot_decision_regions(X_std,y_train,X_test,y_test,classifier=ada)
plt.title('Adaline - Stochastic Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()


#%%
# Gradience plot
plt.plot(range(1,len(ada._cost)+1), ada._cost, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Average Cost')
plt.show()





pass

plt.close()







