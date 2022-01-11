import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.svm import SVC
from sklearn.metrics import zero_one_loss
from AdalineSGD import AdalineSGD
import load_data as load
from sklearn.model_selection import train_test_split


def svm(X_train,y_train,X_test,y_test,k,c,g):
    
        
   
    print('=========================================\nsvm')
    svm = SVC(kernel=k, random_state=1, gamma=g, C=c)
    print('fit')
    svm.fit(X_train,y_train)
    print('plot')
    plot_decision_regions(X_train,y_train, classifier=svm)
   
    
    pred_y = svm.predict(X_test)
    
    error = zero_one_loss(y_test, pred_y)

    print("Zero one loss error:{}".format(error))
    from sklearn.metrics import accuracy_score
    accuracy=accuracy_score(y_test,pred_y)
    print("accuracy",accuracy)
    
    
    plt.legend(loc='upper left')
    title='kernel=%s,gamma=%s,c=%s, acc=%s'%(k,g,c,accuracy)
    plt.title(title)
    plt.show()
   

def adalineSGD(X_train,y_train,X_test,y_test):
    print('=========================================\nAdaline')
    adaline=AdalineSGD()
    adaline.fit(X_train,y_train)
    plot_decision_regions(X_train,y_train, classifier=adaline)
    # plt.title('adaline')
    pred_y=adaline.predict(X_test)
    error = zero_one_loss(y_test, pred_y)
    print("Zero one loss error:{}".format(error))
    from sklearn.metrics import accuracy_score
    accuracy=accuracy_score(y_test,pred_y)
    print("accuracy",accuracy)
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

    
if __name__ == '__main__':
    X,y=load.load()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
    #%%
    # adalineSGD(X_train,y_train,X_test,y_test)
    svm(X_train,y_train,X_test,y_test,'rbf',0.1,0.1)
    