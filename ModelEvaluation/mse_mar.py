import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + 2 + np.random.randn(100) * 0.5

data = pd.DataFrame({'feature': X.squeeze(), 'target': y})

X_train, X_test, y_train, y_test = train_test_split(data[['feature']], data['target'], test_size=0.2, random_state=42)

mean_value = y_train.mean()

y_pred_mean = np.full_like(y_test, mean_value, dtype=np.float64)

mse = mean_squared_error(y_test, y_pred_mean)
mae = mean_absolute_error(y_test, y_pred_mean)

print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')
