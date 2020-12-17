import numpy as np
import sympy as sp
import copy

h = 0.1
dy = '0.2 * x + y ** 2'
f = sp.lambdify(['x', 'y'], dy)
x = np.linspace(0, 1, 11)
y = [0.1]

for i in range(0, 3):
    k = [0, 0, 0, 0]
    k[0] = h * f(x[i], y[i])
    k[1] = h * f(x[i] + h / 2, y[i] + k[0] / 2)
    k[2] = h * f(x[i] + h / 2, y[i] + k[1] / 2)
    k[3] = h * f(x[i] + h, y[i] + k[2])

    y.append(round
             (y[i] + float(1 / 6) *
              (k[0] + 2 * k[1] + 2 * k[2] + k[3]), 4)
             )
y1 = copy.copy(y)
y2 = copy.copy(y)
print(y)
for i in range(3, 10):
    y1.append(y[i - 4] + (4 * h / 3) * (2 * f(x[i - 3], y[i - 3])
                                        - f(x[i - 2], y[i - 2])
                                        + f(x[i - 1], y[i - 1])))
    y2.append(y[i - 2] + h / 3 * (f(x[i - 2], y[i - 2]) + 4 * f(x[i - 1], y[i - 1]) + f(x[i], y1[i])))
    y.append(round(y2[i],4))

print(y)
