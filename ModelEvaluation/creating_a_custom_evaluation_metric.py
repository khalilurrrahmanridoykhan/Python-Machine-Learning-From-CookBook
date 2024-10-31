from sklearn.metrics import make_scorer, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression

features, target = make_regression(n_samples=100, n_features=3, random_state=1)

features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.10, random_state=1)

def custom_metric(target_test, target_predicted):
    r2 = r2_score(target_test, target_predicted)
    return r2

score = make_scorer(custom_metric, greater_is_better=True)

classifier = Ridge()
model = classifier.fit(features_train, target_train)

score(model, features_test, target_test)
print(score(model, features_test, target_test))

target_predicted = model.predict(features_test)
r2_score(target_test, target_predicted)
print(r2_score(target_test, target_predicted))