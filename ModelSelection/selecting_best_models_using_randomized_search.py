from scipy.stats import uniform
from sklearn import linear_model, datasets
from sklearn.model_selection import RandomizedSearchCV

iris = datasets.load_iris()
features = iris.data
target = iris.target

logistic = linear_model.LogisticRegression()
penalty = ['l1', 'l2']
C = uniform(loc=0, scale=4)
hyperparameters = dict(C=C, penalty=penalty)

randomsearch = RandomizedSearchCV(logistic, hyperparameters, cv=5, verbose=0, n_iter=100, n_jobs=-1, random_state=1)

best_model = randomsearch.fit(features, target)
print('Best Penalty:', best_model.best_estimator_.get_params()['penalty'])