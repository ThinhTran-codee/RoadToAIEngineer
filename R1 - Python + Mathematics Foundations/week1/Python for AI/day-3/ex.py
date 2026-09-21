import numpy as np

#Traiining data

X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

#Parameters

w=0.0
b=0.0

learning_rate = 0.01
print("X:", X)
print("X shape:", X.shape)
print("y shape:", y.shape)

for i in range (1000):
 print("iteration:", i)
#Prediction

 y_pred = X * w + b

#Loss
loss  = np.mean((y_pred - y) ** 2)

#Gradient
dw = np.mean(2 * X * (y_pred - y))
db = np.mean(2 * (y_pred - y))

#Update
w = w - learning_rate * dw
b = b - learning_rate * db

if i % 100 == 0:
 print(i, loss, w, b)

print("Final: ")
print("w = ", w)
print("b = ", b)