import numpy as np

theta = np.array([10.0, 5.0])
gradient = np.array([2.0, 4.0])
learning_rate = 0.5

theta = theta - learning_rate * gradient

print(theta)