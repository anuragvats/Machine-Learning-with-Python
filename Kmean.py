import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

X=np.array([[1,2],
           [1,3],
           [2,4],
           [8,8],
           [9,9],
           [9,11]])

#plt.scatter(X[:,0],X[:,1],s=150)
#plt.show();

clr=KMeans(n_clusters=2)
clr.fit(X)

centroids = clr.cluster_centers_
lables = clr.labels_

colors = ["g.","r.","c."]

for i in range(len(X)):
    plt.plot(X[i][0],X[i][1],colors[lables[i]],markersize=25)

plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=25)
plt.show()
