import numpy as np
from sklearn.metrics import silhouette_score
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

features, _ = make_blobs(n_samples=50, n_features=10, centers=2, random_state=1, cluster_std=0.5, shuffle=True)

model = KMeans(n_clusters=2, random_state=1).fit(features)

target_predicted = model.labels_

silhouette_score(features, target_predicted)
print(silhouette_score(features, target_predicted))