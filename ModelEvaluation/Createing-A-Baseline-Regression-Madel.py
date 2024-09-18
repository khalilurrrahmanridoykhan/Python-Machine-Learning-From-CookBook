from sklearn.datasets import load_boston
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split

# Load Data
boston = load_boston()

# Create Features
features, target = boston.data, boston.target

# Make tast and training sliit
features_train, features_tast, target_train, target_tast = train_test_split(features, target, random_state=0)
# Create a dummy Regression
dummy = DummyRegressor(strategy='mean')
# Train Dummy Regration
dummy.fit(features_train, target_train)
# Get R-square of Dummy
# dummyrsquare = print(boston)
print(boston)