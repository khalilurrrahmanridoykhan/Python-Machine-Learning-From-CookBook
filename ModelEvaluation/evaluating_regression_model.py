from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

features, target = make_regression(n_samples=100, n_features=3, n_informative=3, n_targets=1, noise=50, coef=False, random_state=1)

ols = LinearRegression()

cross_val_score(ols, features, target, scoring="neg_mean_squared_error")
print(cross_val_score(ols, features, target, scoring="neg_mean_squared_error"))
cross_val_score(ols, features, target, scoring="r2")
print(cross_val_score(ols, features, target, scoring="r2"))

