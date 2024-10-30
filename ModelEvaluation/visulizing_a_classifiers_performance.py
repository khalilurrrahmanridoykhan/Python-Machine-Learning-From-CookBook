import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

iris = datasets.load_iris()

features = iris.data
target = iris.target

class_names = iris.target_names

features_train, features_test, target_train, target_test = train_test_split(features, target, random_state=1)

classifier = LogisticRegression()

target_predicted = classifier.fit(features_train, target_train).predict(features_test)

matrix = confusion_matrix(target_test, target_predicted)

dataframe = pd.DataFrame(matrix, index=class_names, columns=class_names)

sns.heatmap(dataframe, annot=True, cbar=None, cmap="Blues")
plt.title("Cofusipn Matrix"), plt.tight_layout()
plt.ylabel("True Class"), plt.xlabel("Predicted Class")
plt.show()

print(dataframe)