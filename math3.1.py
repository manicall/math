'''Метод касательных'''
from PyQt5 import QtWidgets
import sys
import expandgraphic as eg
import numpy as np
import sympy as sp
app = QtWidgets.QApplication(sys.argv)

x = sp.Symbol('x')
y = sp.log(x, 10) - 7 / (2 * x + 6)  # функция
dy = sp.diff(y)  # первая производная
d2y = sp.diff(dy)  # вторая производная
f = sp.lambdify(x, y)
df = sp.lambdify(x, dy)
d2f = sp.lambdify(x, d2y)

a = 3;
b = 4  # отрезок
print('f(a)*f(b): ', np.round(f(a) * f(b), 4))  # < 0
print('f\'(a): ', np.round(df(a), 4))  # <> 0
print('f\'\'(a): ', np.round(d2f(a), 4))  # <> 0
print('f(a)*f\'\'(x): ', np.round(f(a) * d2f(np.linspace(a, b, 10)), 4))  # > 0 => x0 = a

a = 3; b = 4  # отрезок
print('f(a)*f(b): ', np.round(f(a)*f(b),4))  # < 0
print('f\'(a): ', np.round(df(a),4))  # <> 0
print('f\'\'(a): ', np.round(d2f(a),4))  # <> 0
print('f(3)*f\'\'(x): ', np.round(f(a)*d2f(np.linspace(a, b, 10)), 4))  # > 0 => x0 = a

m = min(df(np.linspace(a, b, 10)))  # min|f'(x)|
xn = a
xn1 = xn - f(xn) / df(xn)
n = 0
E = 0.001

while (not (np.abs(f(xn1)) <= E * m and np.abs(xn1 - xn) <= E)):
    xn = xn1
    xn1 = xn - f(xn) / df(xn)
    n += 1

window = eg.MainWindow()
print(window.line_edit1.text())
window.add_grid("Корень: " + str(xn1), 0, 0)
window.add_grid("Проверка: " + str(f(xn1)), 0, 1)
window.add_graphic(a, b, 100, f, lambda x: x * 0)
window.show()
app.exec()

while(not(np.abs(f(xn1))<=E*m and np.abs(xn1 - xn) <= E)):
    xn = xn1
    xn1 = xn - f(xn) / df(xn)
    n += 1
print('\n')
print("корень: ", xn1)
print("проверка: ", f(xn1))


