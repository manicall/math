import numpy as np
from m4.math4_1 import E, eps, normaC

A = np.array([
    [0.87, -0.04, 0.14],
    [0.13, 1.28, 0.04],
    [0.12, -0.17, 0.93]
])
C = E - A
D = np.array([2.41, 1.48, -2.65])
normaD = max(np.abs(D))

print()
print('Оценка сложности алгоритма', np.round(np.log(eps * (1 - normaC) / normaD) / np.log(normaC), 1))


