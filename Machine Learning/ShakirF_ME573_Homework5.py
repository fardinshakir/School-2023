import numpy as np
import matplotlib.pyplot as plt
import copy
import csv


datapath = 'C:/Users/Fardin Shakir/Desktop/ml/'
# Data set I will use
data = np.loadtxt(datapath + 'shakirf_kmeans_cluster_data.csv',delimiter = ',')
cluster = 5
iterations = 10


# Update cluster value for each data
def update_cluster_value(data,centroids):
    P = np.shape(data)[1]
    # Storage
    cluster_value = []
    for p in range(P):

        x_p = data[:,p][:,np.newaxis]
    # Distance between
        diffs = np.sum((x_p - centroids)**2,axis = 0)
        # Nearest centroid
        ind = np.argmin(diffs)
        cluster_value.append(ind)
    return np.array(cluster_value)

# Updated centroid location
def update_centroids(data,old_centroids,cluster_value):
    K = old_centroids.shape[1]
    # Storage
    centroids = []
    for k in range(K):
        # Index
        S_k = np.argwhere(cluster_value == k)

        c_k = 0
        # Determine the new centroid, else use the previous one
        if np.size(S_k) > 0:
            c_k = np.mean(data[:,S_k],axis = 1)
        else:
            c_k = copy.deepcopy(old_centroids[:,k])[:,np.newaxis]
        centroids.append(c_k)
    centroids = np.array(centroids)[:,:,0]
    return centroids.T

# K means
def my_kmeans(data,centroids,iterations):
    for j in range(iterations):
    # Update the cluster values
        cluster_value = update_cluster_value(data,centroids)

    # Update the actual value of centroid
        centroids = update_centroids(data,centroids,cluster_value)

    # Our final container
    cluster_value = update_cluster_value(data,centroids)
    return centroids,cluster_value

def analysis(data, cluster, iterations):
    # Points and centroid initialization
    points = np.random.permutation(np.arange(np.shape(data)[1]))[:cluster]
    centroids_0 = data[:,points]
    centroids,cluster_value = my_kmeans(data,centroids_0,iterations)
    print(centroids)

    plt.scatter(data[0,:],data[1,:],c = 'k', s = 10)
    plt.plot(centroids[0], centroids[1], 'r*')
    plt.show()

analysis(data, cluster, iterations)
