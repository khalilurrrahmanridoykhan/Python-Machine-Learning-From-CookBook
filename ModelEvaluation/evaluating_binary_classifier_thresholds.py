import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score

features, target = make_classification(n_samples=1000, n_features=10, n_classes=2, n_informative=3, random_state=3)

features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.1, random_state=1)

logit = LogisticRegression()

logit.fit(features_train, target_train)

target_probabilities = logit.predict_proba(features_test)[:,1]

folse_positive_rate, true_positive_rate, threshold = roc_curve(target_test, target_probabilities)

plt.title("Receiver Operating Characteristic")
plt.plot(folse_positive_rate, true_positive_rate)
plt.plot([0,1], ls="--")
plt.plot([0,0], [1,0], c=".7"), plt.plot([1,1], c=".7")
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.show()