import numpy as np

def predict(X, w, b):
    return X * w + b

def train(X, y, w, b, learning_rate, epochs):
    for _ in range(epochs):
        y_pred = predict(X, w, b)
        loss = np.mean((y_pred - y) ** 2)
        dw = np.mean(2 * X * (y_pred - y))
        db = np.mean(2 * (y_pred - y))
        w = w - learning_rate * dw
        b = b - learning_rate * db
    return w, b

X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

w = 0.0
b = 0.0

w, b = train(X, y, w, b, learning_rate=0.01, epochs=1000)

print("w = ", w)
print("b = ", b)