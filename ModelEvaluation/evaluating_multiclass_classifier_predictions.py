from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import precision_score, recall_score, f1_score

features, target = make_classification(n_samples = 10000, n_features=3, n_informative=3, n_redundant=0, n_classes=3, random_state=1)

logit = LogisticRegression()

cross_val_score(logit, features, target, scoring='accuracy')
# print(cross_val_score(logit, features, target, scoring='accuracy'))
# Fit the model
logit.fit(features, target)
predictions = logit.predict(features)

# Calculate precision, recall, and f1 scores
precision_macro = precision_score(target, predictions, average='macro')
precision_weighted = precision_score(target, predictions, average='weighted')
precision_micro = precision_score(target, predictions, average='micro')

recall_macro = recall_score(target, predictions, average='macro')
recall_weighted = recall_score(target, predictions, average='weighted')
recall_micro = recall_score(target, predictions, average='micro')

f1_macro = f1_score(target, predictions, average='macro')
f1_weighted = f1_score(target, predictions, average='weighted')
f1_micro = f1_score(target, predictions, average='micro')

print(f"Precision (Macro): {precision_macro}")
print(f"Precision (Weighted): {precision_weighted}")
print(f"Precision (Micro): {precision_micro}")

print(f"Recall (Macro): {recall_macro}")
print(f"Recall (Weighted): {recall_weighted}")
print(f"Recall (Micro): {recall_micro}")

print(f"F1 Score (Macro): {f1_macro}")
print(f"F1 Score (Weighted): {f1_weighted}")
print(f"F1 Score (Micro): {f1_micro}")