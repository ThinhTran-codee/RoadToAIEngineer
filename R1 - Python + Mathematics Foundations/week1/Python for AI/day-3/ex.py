import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

w = 0.0
b = 0.0

learning_rate = 0.01

for i in range(1000):
    y_pred = X * w + b

    loss = np.mean((y_pred - y) ** 2)

    dw = np.mean(2 * X * (y_pred - y))
    db = np.mean(2 * (y_pred - y))

    w = w - learning_rate * dw
    b = b - learning_rate * db

    if i % 100 == 0:
        print(i, loss, w, b)

print("Final:")
print("w =", w)
print("b =", b)