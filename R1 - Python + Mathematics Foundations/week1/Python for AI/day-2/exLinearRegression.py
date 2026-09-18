import numpy as np

X = np.array([[1,2], [3,4], [5,6]])

w = np.array([10, 20])
b = 5

prediction = X @ w + b

print(prediction)