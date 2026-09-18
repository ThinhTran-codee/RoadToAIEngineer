import numpy as np

y_true = np.array([10, 15, 20])
y_pred = np.array([8, 13, 23])

mse = np.mean((y_true - y_pred) ** 2)
print(mse)