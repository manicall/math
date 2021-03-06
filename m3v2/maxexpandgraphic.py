import numpy as np
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sympy as sp


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.funcs = None
        sc = MplCanvas()
        self.old_sc = sc
        toolbar = NavigationToolbar(sc, self)

        # menubar============================================
        menuBar = self.menuBar()
        action = menuBar.addAction("Метод касательных", self.set_tangent_resolve_method)
        action.setStatusTip("Выбрать решение уравнения методом касательных")
        action = menuBar.addAction("Метод хорд", self.set_chord_resolve_method)
        action.setStatusTip("Выбрать решение уравнения методом хорд")

        # grid1===============================================
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.setAlignment(QtCore.Qt.AlignHCenter)
        self.grid1_label1 = QtWidgets.QLabel("")
        self.grid1_label2 = QtWidgets.QLabel("")
        self.grid1.addWidget(self.grid1_label1, 0, 0)
        self.grid1.addWidget(self.grid1_label2, 0, 1)

        # grid2=============================================
        self.grid2 = QtWidgets.QGridLayout()
        self.grid2.addWidget(QtWidgets.QLabel("Начало отрезка(a)"), 0, 2)
        self.grid2.addWidget(QtWidgets.QLabel("Конец отрезка(b)"), 0, 3)
        self.grid2.addWidget(QtWidgets.QLabel("Количество точек на отрезке"), 0, 4)
        self.grid2.addWidget(QtWidgets.QLabel("Точность"), 0, 5)
        self.grid2.addWidget(QtWidgets.QLabel("Уравнение"), 0, 6)
        self.grid2_lineEdit1 = QtWidgets.QLineEdit("1")
        self.grid2_lineEdit2 = QtWidgets.QLineEdit("5")
        self.grid2_lineEdit3 = QtWidgets.QLineEdit("100")
        self.grid2_lineEdit4 = QtWidgets.QLineEdit("0.001")
        self.grid2_lineEdit4.textChanged.connect(self.set_accurate)
        #===================================================================
        self.grid2_comboBox = QtWidgets.QComboBox()
        self.grid2_comboBox.addItem('log(x, 10) - 7 / (2 * x + 6)')
        self.grid2_comboBox.addItem('x ** 3 - 3 * x ** 2 + 6 * x - 3')
        self.grid2_comboBox.setEditable(True)
        self.grid2_comboBox.currentIndexChanged.connect(self.change_equation)
        #====================================================================
        grid2_button1 = QtWidgets.QPushButton("Построить график")
        grid2_button1.clicked.connect(self.create_graphic)
        self.grid2.addWidget(grid2_button1, 1, 0)
        self.grid2_button2 = QtWidgets.QPushButton("Рассчитать аналитически")
        self.grid2_button2.clicked.connect(self.tangent_analitical_resolve)
        self.grid2.addWidget(self.grid2_button2, 1, 1)
        self.grid2.addWidget(self.grid2_lineEdit1, 1, 2)
        self.grid2.addWidget(self.grid2_lineEdit2, 1, 3)
        self.grid2.addWidget(self.grid2_lineEdit3, 1, 4)
        self.grid2.addWidget(self.grid2_lineEdit4, 1, 5)
        self.grid2.addWidget(self.grid2_comboBox, 1, 6)

        # function============================================
        self.E = float(self.grid2_lineEdit4.text())
        x = sp.Symbol('x')
        self.y = self.grid2_comboBox.currentText()  # функция
        self.dy = sp.diff(self.y)  # первая производная
        self.d2y = sp.diff(self.dy)  # вторая производная
        self.f = sp.lambdify(x, self.y)
        self.df = sp.lambdify(x, self.dy)
        self.d2f = sp.lambdify(x, self.d2y)
        self.get_funcs(self.f, lambda x: x * 0)

        # child_layout===============================================
        self.child_layout = QtWidgets.QVBoxLayout()
        self.child_layout.addWidget(toolbar)
        self.child_layout.addWidget(sc)

        # parent_layout===============================================
        self.parent_layout = QtWidgets.QVBoxLayout()
        self.parent_layout.addLayout(self.grid2)
        self.parent_layout.addLayout(self.child_layout)
        self.parent_layout.addLayout(self.grid1)

        # widget==============================================
        widget = QtWidgets.QWidget()
        widget.setLayout(self.parent_layout)
        self.setCentralWidget(widget)

        # statusbar===========================================
        self.label1 = QtWidgets.QLabel("выбран метод касательных")
        self.label2 = QtWidgets.QLabel("текущее уравнение: " + self.grid2_comboBox.currentText())
        status_bar = self.statusBar()
        status_bar.setSizeGripEnabled(False)
        status_bar.addPermanentWidget(self.label1)
        status_bar.addPermanentWidget(self.label2)
        self.show()

    def add_graphic(self, start, end, count):
        sc = MplCanvas()
        toolbar = NavigationToolbar(sc, self)
        for i in range(self.child_layout.count()):
            self.child_layout.takeAt(0).widget().deleteLater()
        self.child_layout.addWidget(toolbar)
        self.child_layout.addWidget(sc)
        x = np.linspace(start, end, count)
        for i in self.funcs:
            sc.axes.plot(x, i(x))

    def create_graphic(self):
        try:
            self.add_graphic(float(self.grid2_lineEdit1.text()),
                         float(self.grid2_lineEdit2.text()),
                         int(self.grid2_lineEdit3.text()))
        except:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "В поля ввода введены некорректные данные")

    def get_funcs(self, *args):
        self.funcs = args

    def set_accurate(self):
        try: self.E = float(self.grid2_lineEdit4.text())
        except: pass

    def change_equation(self):
        x = sp.Symbol('x')
        try:
            self.y = self.grid2_comboBox.currentText()  # функция
            self.dy = sp.diff(self.y)  # первая производная
            self.d2y = sp.diff(self.dy)  # вторая производная
            self.f = sp.lambdify(x, self.y); self.f(1)
            self.df = sp.lambdify(x, self.dy)
            self.d2f = sp.lambdify(x, self.d2y)
        except:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Невозможно построить функцию уравнения")
            self.grid2_comboBox.removeItem(self.grid2_comboBox.count() - 1)
            self.y = self.grid2_comboBox.currentText()
        self.get_funcs(self.f, lambda x: x * 0)
        self.label2.setText("текущее уравнение: " + self.y)

    def set_tangent_resolve_method(self):
        self.label1.setText("выбран метод касательных")
        self.grid2_button2.clicked.disconnect()
        self.grid2_button2.clicked.connect(self.tangent_analitical_resolve)

    def set_chord_resolve_method(self):
        self.label1.setText("выбран метод хорд")
        self.grid2_button2.clicked.disconnect()
        self.grid2_button2.clicked.connect(self.chord_analitical_resolve)

    def analitical_resolve(self):
        a = float(self.grid2_lineEdit1.text())
        b = float(self.grid2_lineEdit2.text())  # отрезок
        print('f(a)*f(b): ', np.round(self.f(a) * self.f(b), 4))  # < 0
        if self.f(a) * self.f(b) >= 0 or self.df(a) == 0 or self.d2f(a) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Невозможно вычислить корень уравнения")
            self.grid1_labels_clear()
            return
        print('f(a)*f\'\'(x): ', np.round(self.f(a) * self.d2f(np.linspace(a, b, 10)), 4))  # > 0 => x0 = a
        return a, b


    def tangent_analitical_resolve(self):
        try: a, b = self.analitical_resolve()
        except: return
        check = self.f(a) * self.d2f(np.linspace(a, b, 10)) >= 0
        not_check = self.f(a) * self.d2f(np.linspace(a, b, 10)) < 0
        m = min(self.df(np.linspace(a, b, 10)))  # min|f'(x)|
        if (all(check)):
            xn = a
        elif (all(not_check)):
            xn = b
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Невозможно вычислить корень уравнения")
            self.grid1_labels_clear()
            return

        xn1 = xn - self.f(xn) / self.df(xn)
        n = 0
        while (not (np.abs(self.f(xn1)) <= self.E * m and np.abs(xn1 - xn) <= self.E)):
            xn = xn1
            xn1 = xn - self.f(xn) / self.df(xn)
            n += 1
        self.grid1_label1.setText("Корень: " + str(xn1))
        self.grid1_label2.setText("Проверка: " + str(self.f(xn1)))

    def chord_analitical_resolve(self):
        try: a, b = self.analitical_resolve()
        except: return
        check = self.f(a) * self.d2f(np.linspace(a, b, 10)) >= 0
        not_check = self.f(a) * self.d2f(np.linspace(a, b, 10)) < 0
        if (all(check)):
            xn = b
            d = a
        elif (all(not_check)):
            xn = a
            d = b
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Невозможно вычислить корень уравнения")
            self.grid1_labels_clear()
            return

        m = min(self.df(np.linspace(a, b, 10)))  # min|f'(x)|
        n = 0
        xn1 = xn - self.f(xn) * (xn - d) / (self.f(xn) - self.f(d))
        while (not (np.abs(self.f(xn1)) <= self.E * m and np.abs(xn1 - xn) <= self.E)):
            xn = xn1
            xn1 = xn - self.f(xn) * (xn - d) / (self.f(xn) - self.f(d))
            n += 1
        self.grid1_label1.setText("Корень: " + str(xn1))
        self.grid1_label2.setText("Проверка: " + str(self.f(xn1)))

    def grid1_labels_clear(self):
        self.grid1_label1.setText("")
        self.grid1_label2.setText("")
