from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

features, target = iris.data, iris.target

featres_train, features_test, target_train, target_test = train_test_split(features, target, random_state=0)

dummy = DummyClassifier(strategy='uniform', random_state=1)
# dummy = DummyClassifier(strategy='stratified', random_state=1)


dummy.fit(featres_train, target_train)


dummy.score(features_test, target_test)


classifier = RandomForestClassifier()

classifier.fit(featres_train, target_train)
classifier.score(features_test, target_test)
print(dummy.score(features_test, target_test))
print(classifier.score(features_test, target_test))