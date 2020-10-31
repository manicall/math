import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
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

E = 0.001
range = np.linspace(-2, 2, 100)
fig = plt.figure()
plt.subplot(111)
plt.subplot(111).spines['left'].set_position('center')
plt.subplot(111).spines['bottom'].set_position('center')
plt.xlabel('x', labelpad=-30, loc='right')
plt.ylabel('y', labelpad=-30, loc='top')

#y = sin(x + 0.5) - 2
plt.plot(range, np.sin(range + 0.5) - 2)  # blue
#x = cos(y + 2)
plt.plot(np.cos(range + 2), range)  # orange
plt.show()
"""
Область D = {0<=x<=1, -1<=y<=-2}
"""
# МЕТОД НЬЮТОНА
f1 = 'x - cos(y + 2)'
f2 = 'sin(x + 0.5) - 2 - y'


if sp.diff(f2, 'x', 'x') != '0' and sp.diff(f1, 'y', 'y') != '0':
    # матрица якоби
    J = np.array([
        [sp.diff(f1, 'x'), sp.diff(f1, 'y')],
        [sp.diff(f2, 'x'), sp.diff(f2, 'y')]
    ])
    print(J)
    lJ = np.array([
        [sp.diff(f1, 'x'), sp.lambdify('y', sp.diff(f1, 'y'))],
        [sp.lambdify('x', sp.diff(f2, 'x')), sp.diff(f2, 'y')]
    ])

    # det(J) = -1 - cos(x+0.5)*sin(y+2), докажем что cos(x+0.5)*sin(y+2) != -1
    if all(lJ[0][1](np.linspace(0, 1, 10)) > 0) and all(lJ[1][0](np.linspace(-1, -2, 10)) > 0):

        def b1(x, y):
            return xk + np.sin(yk + 1) * yk - (xk - np.cos(yk + 1))

        def b2(x, y):
            return - (np.sin(xk) - yk) + np.cos(xk) * xk - yk
        xk = -1
        yk = -1
        i = 0

        while i < 10:
            A = np.array([[1, np.sin(yk+1)],
                          [np.cos(xk), -1]])

            b = np.array([b1(xk, yk), b2(xk, yk)])

            xk1, yk1 = np.linalg.solve(A, b)
            print(xk1 - np.cos(yk1+1), np.sin(xk1) - yk1)
            xk = xk1
            yk = yk1
            i+=1

    #| sin(x + 0.5) - y = 2
    #| cos(y + 2.0) + x = 0




#xk1 - xk + sin(yk+2)*yk1 - sin(yk+2)*yk = - (xk - cos(yk+1))
#cos(xk)*(xk1-xk) - (yk1-yk) =  - (sin(xk)-yk)

#xk1 + sin(yk+1)*yk1 = xk + sin(yk+1) * yk - (xk - cos(yk+1))
#cos(xk)*xk1 - yk1 =  - (sin(xk) - yk) + cos(xk) * xk - yk
