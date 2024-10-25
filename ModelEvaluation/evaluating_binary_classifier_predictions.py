from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
X, y = make_classification(n_samples=1000, n_features=3,n_redundant=0, n_classes=2, random_state=42)

logit = LogisticRegression()

cross_val_score(logit, X, y, scoring='accuracy')
# print(cross_val_score(logit, X, y, scoring='accuracy'))

cross_val_score(logit, X, y, scoring='precision')
# print(cross_val_score(logit, X, y, scoring='precision'))

cross_val_score(logit, X, y, scoring='recall')
# print(cross_val_score(logit, X, y, scoring='recall'))

cross_val_score(logit, X, y, scoring='f1')
# print(cross_val_score(logit, X, y, scoring='f1'))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

y_hat = logit.fit(X_train, y_train).predict(X_test)

accuracy_score(y_test, y_hat)
print(accuracy_score(y_test, y_hat))


