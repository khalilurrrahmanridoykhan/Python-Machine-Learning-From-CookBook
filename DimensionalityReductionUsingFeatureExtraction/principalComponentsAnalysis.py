from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets

digits = datasets.load_digits()

features = StandardScaler().fit_transform(digits.data)
pca = PCA(n_components=0.99, whiten=True)
feactures_pca = pca.fit_transform(features)
print("Orignal Numbber of Feature: ", features.shape[1])
print("Reduced Number of Feature: ", feactures_pca.shape[1])