import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import os
"""
Система уравнений согласно варианту:
     --
    | sin(x + 0.5) - y = 2
    | cos(y + 2.0) + x = 0
     --
     --
    | x = cos(y + 2)
    | y = sin(x + 0.5) - 2
     --
"""

eps = 0.001
range = np.linspace(-5, 5, 100)
fig = plt.figure()
plt.subplot(111)
plt.subplot(111).spines['left'].set_position('center')
plt.subplot(111).spines['bottom'].set_position('center')
plt.xlabel('x', labelpad=-30, loc='right')
plt.ylabel('y', labelpad=-30, loc='top')
#x = -cos(y + 2)
plt.plot(-np.cos(range + 2), range)  # orange
#y = sin(x + 0.5) - 2
plt.plot(range, np.sin(range + 0.5) - 2)  # blue

"""
Область D = {-1<=x<=0, -3<=y<=-2}
"""

# МЕТОД НЬЮТОНА
os.system('cls')
print('Медот Ньютона')
f1 = 'x + cos(y + 2)'
f2 = 'sin(x + 0.5) - 2 - y'

# матрица якоби
J = np.array([
    [sp.diff(f1, 'x'), sp.diff(f1, 'y')],
    [sp.diff(f2, 'x'), sp.diff(f2, 'y')]
])
lJ = np.array([
    [sp.diff(f1, 'x'), sp.lambdify('y', sp.diff(f1, 'y'))],
    [sp.lambdify('x', sp.diff(f2, 'x')), sp.diff(f2, 'y')]
])

# det(J) = -1 - cos(x+0.5)*sin(y+2), докажем что cos(x+0.5)*-sin(y+2) != -1
if all(lJ[0][1](np.linspace(-1, 0, 10)) * lJ[1][0](np.linspace(-3, -2, 10)) != -1):
    def b1(x, y):
        return - (x + np.cos(y + 2)) + xk - np.sin(yk + 2) * yk

    def b2(x, y):
        return - (np.sin(x + 0.5) - 2 - y) + np.cos(xk + 0.5) * xk - yk
    xk = -1
    yk = -3
    def solve():
        A = np.array([
            [1, -np.sin(yk + 2)],
            [np.cos(xk + 0.5), -1]
        ])
        b = np.array([b1(xk, yk), b2(xk, yk)])
        return np.linalg.solve(A, b)
    xk1, yk1 = solve()
    i = 0
    while not (max(np.abs(xk1 - xk), np.abs(yk1 - yk)) <= eps):
        xk = xk1
        yk = yk1
        xk1, yk1 = solve()
        i += 1
    print('корни:', xk1, yk1)
    print('проверка:', np.sin(xk1 + 0.5) - yk1 - 2, np.cos(yk1 + 2) + xk1)
    print('количество шагов:', i)

#  МЕТОД ИТЕРАЦИЙ
print('Медот итераций')
f1 = '-cos(y + 2)'
f2 = 'sin(x + 0.5) - 2'
M = np.array([
    [sp.diff(f1, 'x'), sp.diff(f1, 'y')],
    [sp.diff(f2, 'x'), sp.diff(f2, 'y')]
])
lM = np.array([
    [sp.diff(f1, 'x'), sp.lambdify('y', sp.diff(f1, 'y'))],
    [sp.lambdify('x', sp.diff(f2, 'x')), sp.diff(f2, 'y')]
])

#print(M)
normaM1 = (max(lM[0][1](np.linspace(-1, -0.85, 10))))
normaM2 = (max(lM[1][0](np.linspace(-3, -2, 10))))
M = np.array([
    [0, normaM1],
    [normaM2, 0]
])
normaM = np.linalg.norm(M, ord=float('inf'))

x = np.array([-1, -3])
xk1 = -np.cos(x[1] + 2)
yk1 = np.sin(x[0] + 0.5) - 2

i = 0
while not ((np.linalg.norm((np.array([xk1, yk1]) - x), ord=float('inf'))
            <= (((1 - normaM) / normaM) * eps))):
    x = [xk1, yk1]
    xk1 = -np.cos(x[1] + 2)
    yk1 = np.sin(x[0] + 0.5) - 2
    i += 1
print('корни:', xk1, yk1)
print('проверка:', np.sin(xk1 + 0.5) - yk1 - 2, np.cos(yk1 + 2) + xk1)
print('количество шагов:',i)
plt.show()
