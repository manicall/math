'''Метод хорд'''

from PyQt5 import QtWidgets
import sys
import expandgraphic as eg
import numpy as np
import sympy as sp
app = QtWidgets.QApplication(sys.argv)
x = sp.Symbol('x')
y = x ** 3 - 3 * x ** 2 + 6 * x - 3
dy = sp.diff(y)  # первая производная
d2y = sp.diff(dy)  # вторая производная
f = sp.lambdify(x, y)
df = sp.lambdify(x, dy)
d2f = sp.lambdify(x, d2y)
a = 0;
b = 1  # отрезок
print('f(a)*f(b): ', f(a) * f(b))  # < 0
print('f\'(a): ', df(a))  # <> 0
print('f\'\'(a): ', d2f(a))  # <> 0
print('f(a)*f\'\'(x): ', f(a) * d2f(np.linspace(a, b, 10)))  # > 0 => d = a, x0 = b
m = min(df(np.linspace(a, b, 10)))  # min|f'(x)|
d = a
E = 0.001
n = 0

xn = b
xn1 = xn - f(xn) * (xn - d) / (f(xn) - f(d))
while (not (np.abs(f(xn1)) <= E * m and np.abs(xn1 - xn) <= E)):
    xn = xn1
    xn1 = xn - f(xn) * (xn - d) / (f(xn) - f(d))
    n += 1
window = eg.MainWindow()
window.add_grid("Корень: " + str(xn1), 0, 0)
window.add_grid("Проверка: " + str(f(xn1)), 0, 1)
window.add_graphic(a, b, 100, f, lambda x: x * 0)
window.show()
app.exec()

