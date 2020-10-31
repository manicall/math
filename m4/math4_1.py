import numpy as np
import numpy.linalg as la
import copy
eps = 0.001
A = np.array([
    [0.87, -0.04, 0.14],
    [0.13, 1.28, 0.04],
    [0.12, -0.17, 0.93]
])
E = np.eye(A.shape[0])
D = np.array([2.41, 1.48, -2.65])
if la.det(A) != 0:
    C = E - A
    normaC = la.norm(C, ord=float('inf'))
    print(normaC)
    if normaC < 1:
        x0 = np.array([1, 1, 1])
        x1 = np.dot(C, x0) + D
        k = 0
        while not ((la.norm((x1 - x0), ord=float('inf')) <= (((1 - normaC) / normaC) * eps))):
            x0 = x1
            x1 = np.dot(C, x0) + D
            k += 1
        print('корень: ', x1, '\nколичество шагов: ', k)

def check(r):
    copyA = copy.copy(A)
    for i in range(copyA.shape[0]):
        for j in range(copyA.shape[1]):
            copyA[j][i] *= r[i]

    sums = np.array([sum(row) for row in copyA])
    print('проверка:', sums - D)

check(x1)



