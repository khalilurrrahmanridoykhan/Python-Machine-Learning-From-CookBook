from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

digits = datasets.load_digits()

# Create Features matrix
features = digits.data

# Create target vector
target = digits.target

# Create Logistic Regression Object
logis = LogisticRegression()

# Create Standardizer
standizer = StandardScaler()



# Create K-fold Cross-validation
kf = KFold(n_splits=10, shuffle=True, random_state=1)

# Crate Train tast set
features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.1, random_state=1
)

# Fit Standardizer to training set
standizer.fit(features_train)

# Apply to both training and test set
features_train_std = standizer.transform(features_train)
features_tast_std = standizer.transform(features_test)

# Create a pipeline that standardizes, then runs logistic regression
pipeline = make_pipeline(standizer, logis)

# Do K-fold cross-validation
cv_results = cross_val_score(
    pipeline,
    features,
    target,
    cv=kf,
    scoring="accuracy",
    n_jobs=-1
)

print(features.shape)