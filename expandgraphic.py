import numpy as np
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        super(MplCanvas, self).__init__(self.fig)
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.funcs = None
        self.sc = MplCanvas()
        self.old_sc = self.sc
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)
        #grid1===============================================
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.setAlignment(QtCore.Qt.AlignHCenter)
        self.grid1_label1 = QtWidgets.QLabel("")
        self.grid1_label2 = QtWidgets.QLabel("")
        self.grid1.addWidget(self.grid1_label1, 0, 0)
        self.grid1.addWidget(self.grid1_label2, 0, 1)
        #grid2=============================================
        self.grid2 = QtWidgets.QGridLayout()
        self.grid2.addWidget(QtWidgets.QLabel("Начало отрезка(a)"), 0 , 2)
        self.grid2.addWidget(QtWidgets.QLabel("Конец отрезка(b)"), 0, 3)
        self.grid2.addWidget(QtWidgets.QLabel("Количество точек на отрезке"), 0, 4)
        self.grid2_lineEdit1 = QtWidgets.QLineEdit("-5")
        self.grid2_lineEdit2 = QtWidgets.QLineEdit("5")
        self.grid2_lineEdit3 = QtWidgets.QLineEdit("100")
        grid2_button1 = QtWidgets.QPushButton("Построить график")
        grid2_button1.clicked.connect(self.create_graphic)
        self.grid2.addWidget(grid2_button1, 1, 0)
        self.grid2_button2 = QtWidgets.QPushButton("расчитать аналитически")
        self.grid2.addWidget(self.grid2_button2, 1, 1)
        self.grid2.addWidget(self.grid2_lineEdit1, 1, 2)
        self.grid2.addWidget(self.grid2_lineEdit2, 1, 3)
        self.grid2.addWidget(self.grid2_lineEdit3, 1, 4)
        #layout===============================================
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(toolbar)
        self.layout.addLayout(self.grid2)
        self.layout.addWidget(self.sc)
        self.layout.addLayout(self.grid1)
        #widget==============================================
        widget = QtWidgets.QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.show()

    def add_graphic(self, start, end, count):
        sc = MplCanvas()
        self.layout.removeWidget(self.old_sc)
        self.old_sc = sc
        self.layout.insertWidget(2,sc)

        x = np.linspace(start, end, count)
        for i in self.funcs:
            sc.axes.plot(x, i(x))
        self.hide()
        self.show()

    def create_graphic(self):
        self.add_graphic(float(self.grid2_lineEdit1.text()),
                         float(self.grid2_lineEdit2.text()),
                         int(self.grid2_lineEdit3.text()))

    def get_funcs(self, *args):
        self.funcs = args
