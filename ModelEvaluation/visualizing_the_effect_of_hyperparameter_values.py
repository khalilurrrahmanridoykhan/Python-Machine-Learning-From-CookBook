# Hyperparameters are parameters whose values are set before the learning process begins.
# They control the behavior of the training algorithm and have a significant impact on the performance of the model.
# Examples include the learning rate, number of iterations, and regularization strength.

# This code evaluates the effect of varying the number of trees (n_estimators) in a RandomForestClassifier on the accuracy of the model using the digits dataset.
# It uses cross-validation to compute the training and test scores for different values of n_estimators, and then plots these scores along with their standard deviations to visualize the model's performance.



import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import validation_curve

digits = load_digits()

features, target = digits.data, digits.target

param_range = np.arange(1, 250, 2)

train_scores, test_scores = validation_curve(RandomForestClassifier(), features, target, param_name='n_estimators', param_range=param_range, cv=3, scoring='accuracy', n_jobs=-1)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(param_range, train_mean, '--', color='#111111', label='Training score')
plt.plot(param_range, test_mean, color='#111111', label='Cross-validation score')

plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, color='gray')
plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, color='gainsboro')

plt.title('Validation Curve With Random Forest')
plt.xlabel('Number Of Trees')
plt.ylabel('Accuracy Score')
plt.tight_layout()
plt.legend(loc='best')
plt.show()