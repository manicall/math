'''Метод хорд'''
from PyQt5 import QtWidgets
import sys
from m3v1 import expandgraphic as eg
import numpy as np
import sympy as sp

x = sp.Symbol('x')
y = x ** 3 - 3 * x ** 2 + 6 * x - 3
dy = sp.diff(y)  # первая производная
d2y = sp.diff(dy)  # вторая производная
f = sp.lambdify(x, y)
df = sp.lambdify(x, dy)
d2f = sp.lambdify(x, d2y)

app = QtWidgets.QApplication(sys.argv)
window = eg.MainWindow()
window.setWindowTitle("Метод хорд")
window.get_funcs(f, lambda x: x * 0)
window.show()

def chord_analitic_resolve():
    a = float(window.grid2_lineEdit1.text())
    b = float(window.grid2_lineEdit2.text())  # отрезок
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
    window.grid1_label1.setText("Корень: " + str(xn1))
    window.grid1_label2.setText("Проверка: " + str(f(xn1)))

window.grid2_button2.clicked.connect(chord_analitic_resolve)
app.exec()

