import numpy as np

arr = np.random.randint(1, 100, 10)
max_val = np.max(arr)
max_idx = np.argmax(arr)

print(arr)
print(max_val)
print(max_idx)
