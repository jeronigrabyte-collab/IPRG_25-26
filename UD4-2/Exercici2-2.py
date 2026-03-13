#EXERCICI 2 PRÀCTICA 2
import numpy as np

temperatures = np.array([
    [18, 20, 17],
    [19, 21, 18],
    [17, 19, 16],
    [22, 24, 20],
    [21, 23, 19],
    [15, 22, 18],
    [18, 20, 17]
])

print(temperatures[:, 2])
print(temperatures[0, :])
print(temperatures[:2, :])
print(temperatures[2:5, 0])