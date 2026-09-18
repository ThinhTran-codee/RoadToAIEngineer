w = 2.0
b = 1.0
learning_rate = 0.1

for i in range(10):

    loss = w**2 + 3 * b**2

    dw = 2*w
    db = 6*b
    w = w - learning_rate * dw
    b = b - learning_rate * db

    print (i, loss, dw, db, w, b)