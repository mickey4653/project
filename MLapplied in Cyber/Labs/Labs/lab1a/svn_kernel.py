import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from sklearn.metrics import zero_one_loss

from sklearn.svm import SVC


def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha=.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, c1 in enumerate(np.unique(y)):
        plt.scatter(x=X[y == c1, 0],
                    y=X[y == c1, 1],
                    alpha=.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=c1,
                    edgecolor='black'
                    )


np.random.seed(1)

X_xor = np.random.randn(200, 2)
y_xor = np.logical_xor(X_xor[:, 0] > 0,
                       X_xor[:, 1] > 0)

y_xor = np.where(y_xor, 1, -1)
kernels=['linear', 'poly', 'rbf', 'sigmoid']
# 'precomputed'
C=[0.1, 0.5, 1, 5, 10, 15, 20, 100]
gammas= [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 3, 4, 5]
# gammas=list( range(1,11))
# C=list(range(1,11))
best_loss=1
dict={'kernel':'','gamma':'','C':''}
for k in range(len(kernels)):
    for g in range(len(gammas)):
        for c in range(len(C)):
            # print(k,g,c)
            svm = SVC(kernel=kernels[k], random_state=1, gamma=gammas[g], C=C[c])
            svm.fit(X_xor, y_xor)
            pred_y = svm.predict(X_xor)
            error = zero_one_loss(y_xor, pred_y)
            if(error<best_loss and error>0):
                best_loss=error
                dict['kernel']=kernels[k]
                dict['gamma']=gammas[g]
                dict['C']=C[c]
            # print("Zero one loss error:{}".format(error))



#%%
print('kernel:', dict['kernel'],'\ngamma:', dict['gamma'],'\nC:',dict['C'])
svm = SVC(kernel=dict['kernel'], random_state=1, gamma=dict['gamma'], C=dict['C'])
svm.fit(X_xor, y_xor)
plot_decision_regions(X_xor, y_xor, classifier=svm)
plt.legend(loc='upper left')

pred_y = svm.predict(X_xor)

error = zero_one_loss(y_xor, pred_y)

print("Zero one loss error:{}".format(error))

# plt.show()
