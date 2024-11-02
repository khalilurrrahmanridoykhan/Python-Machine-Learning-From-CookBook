import numpy as np
from sklearn import linear_model, datasets
from sklearn.model_selection import GridSearchCV

iris = datasets.load_iris()
features = iris.data
target = iris.target

logistic = linear_model.LogisticRegression()

penalty = ['l1', 'l2']

C = np.logspace(0, 4, 10)

hyperparameters = dict(C=C, penalty=penalty)

gridsearch = GridSearchCV(logistic, hyperparameters, cv=5, verbose=0)

best_model = gridsearch.fit(features, target)

print('Best Penalty:', best_model.best_estimator_.get_params()['penalty'])
print('Best C:', best_model.best_estimator_.get_params()['C'])

best_model.predict(features)
# The best hyperparameters are stored in best_model.best_params_.
# The best estimator is stored in best_model.best_estimator_.
# The best score is stored in best_model.best_score_.
# The best index is stored in best_model.best_index_.
# The best parameter values are stored in best_model.best_estimator_.get_params().
# The best model is trained on the full dataset.
# The best model can be used to make predictions.

print(best_model.best_score_)