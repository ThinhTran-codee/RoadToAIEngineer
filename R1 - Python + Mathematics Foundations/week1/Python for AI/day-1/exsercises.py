import numpy as np

## 2: Vector Operations

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print(a + b)

print(a - b)

print(3 * a)

## Broadcast: 

numbers1 = np.array([[1,2,3], [4, 5, 6]])
numbers2 = np.array([10, 20, 30])
print(numbers1 + numbers2)

//Vì dimension cuối của numbers1 có kích thước là 3 và B cũng vậy nên numpy có thể broadcast B cho từng row A


## Dot product: