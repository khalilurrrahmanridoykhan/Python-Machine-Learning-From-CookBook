from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
features, target = make_blobs(
    n_samples = 100,
    n_features = 2,
    centers = 3,
    cluster_std = 0.5,
    shuffle = True,
    random_state = 1
)

# View Scatterplot of Make_blods = The Number of Clusters Grnerated 
plt.scatter(features[:,0], features[:,1], c=target)
plt.show()

print(features[:,0])
print(target)