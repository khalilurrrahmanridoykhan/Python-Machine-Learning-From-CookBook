from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

digits = datasets.load_digits()
# Create Features Matrix
features = digits.data
# Create Target Vector
target = digits.target
# Create Standardizer
standardizer = StandardScaler()
# Create The Logistic Regression Object
logit = LogisticRegression()
# Create a pipeline that standardizes, then runs logistic regression
pipline = make_pipeline(standardizer, logit)
# create k-Fold cross-validation
kf = KFold(n_splits=10, shuffle=True, random_state=1)
# Create k-fold cross-validation
cv_results = cross_val_score(pipline, features, target, cv=kf, scoring="accuracy", n_jobs=-1)
# Calculate Mean
print(features.shape)