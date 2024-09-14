from sklearn.datasets import make_classification

features, target = make_classification(
    n_samples = 100, 
    n_features = 3,
    n_informative = 3,
    n_redundant = 0,
    n_classes = 2,
    weights = [.25, 0.75],
    random_state = 1
)

print(features[:3])
print(target[:3])