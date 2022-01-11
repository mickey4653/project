
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import time
import load_data as load

MAX_NUMBER_OF_CLUSTERS = 50


def elbow_method_plot(X):

    sse = {}
    scores={}
    for k in range(1, MAX_NUMBER_OF_CLUSTERS):
        kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=1000).fit(X)

        labels = kmeans.labels_

        sse[k] = kmeans.inertia_  # Inertia: Sum of distances of samples to their closest cluster center
        if k > 1:

            sil_coeff = silhouette_score(X, labels, metric='euclidean')
            scores[k]=sil_coeff
            print("For n_clusters={}, The Silhouette Coefficient is {}".format(k, sil_coeff))

    plt.figure()

    plt.plot(list(sse.keys()), list(sse.values()))

    plt.xlabel("Number of cluster")

    plt.ylabel("SSE")

    plt.show()
    import operator
    k=max(scores.items(), key=operator.itemgetter(1))[0]
    return k
        

def perform_k_means_clustering(X, num_clusters):
    # Initialize KMeans
    km = KMeans(n_clusters=num_clusters,
                init='k-means++',
                n_init=40,
                max_iter=500,
                tol=1e-04,
                random_state=0)

    # Perform the clustering
    start_time = time.time()
    y_km = km.fit_predict(X)
    elapsed_time = time.time() - start_time
    print("Runtime: {} seconds".format(elapsed_time))

    # Plotting
    plt.figure()
    colors = cm.rainbow(np.linspace(0,1,num_clusters))
    for k, color in zip(range(num_clusters), colors):

        # plot points for cluster i
        plt.scatter(X[y_km == k, 0],
                    X[y_km == k, 1],
                    s=50,
                    c=color,
                    marker='o',
                    label="cluster {}".format(k+1))

    plt.scatter(km.cluster_centers_[:, 0],
                km.cluster_centers_[:,1],
                s=250,
                marker= '*',
                c='black',
                label='centroids')
    plt.xlim(-5,140)
    plt.ylim(-5,16)

    plt.legend(scatterpoints=1)
    plt.grid()
    plt.show()
    return km


def main():

    X,y=load.load()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
    model=perform_k_means_clustering(X_train,2)
    print('=========================================svm')
    pred_y = model.predict(X_test)
    from sklearn.metrics import zero_one_loss
    error = zero_one_loss(y_test, pred_y)

    print("Zero one loss error:{}".format(error))
    from sklearn.metrics import accuracy_score
    accuracy=accuracy_score(y_test,pred_y)
    print("accuracy",accuracy)
    

    


if __name__ == '__main__':
    main()


