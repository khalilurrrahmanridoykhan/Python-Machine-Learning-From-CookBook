from sklearn.datasets import make_regression

features,target, coefficients = make_regression(
    n_samples=10, 
    n_features=3, 
    n_informative = 3,
    n_targets = 1,
    noise=0.0, 
    random_state=1, 
    coef = True
)

print(features[:])
print(target[:3])