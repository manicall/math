import numpy as np
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.sc = MplCanvas()
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.setAlignment(QtCore.Qt.AlignHCenter)

        self.grid2 = QtWidgets.QGridLayout()
        self.grid2.addWidget(QtWidgets.QLabel("Начало отрезка(a)"), 0 , 1)
        self.grid2.addWidget(QtWidgets.QLabel("Конец отрезка(b)"), 0, 2)
        self.grid2.addWidget(QtWidgets.QLabel("Количество точек на отрезке", 0, 3))

        self.line_edit1 = QtWidgets.QLineEdit("-5")
        self.line_edit2 = QtWidgets.QLineEdit("-5")
        self.line_edit3 = QtWidgets.QLineEdit("-5")
        button = QtWidgets.QPushButton("Построить график")
        button.clicked.connect(self.create_graphic)
        self.grid2.addWidget(button, 1, 0)
        self.grid2.addWidget(self.line_edit1, 1, 1)
        self.grid2.addWidget(self.line_edit2, 1, 2)
        self.grid2.addWidget(self.line_edit2, 1, 3)
        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(toolbar)
        layout.addLayout(self.grid2)
        layout.addWidget(self.sc)
        layout.addLayout(self.grid1)
        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()
    def add_graphic(self, start, end, count, *args):
        x = np.linspace(start, end, count)
        for i in args:
            self.sc.axes.plot(x, i(x))
    def add_grid(self, str, x, y):
        self.grid1.addWidget(QtWidgets.QLabel(str), x, y)

    def create_graphic(self, *args):
        self.add_graphic(self.line_edit1, self.line_edit2, self.line_edit3, *args)

