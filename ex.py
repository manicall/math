import sys
import matplotlib as plt
plt.use('Qt5Agg')
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        #sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)
        grid = QtWidgets.QGridLayout()
        grid.addWidget(QtWidgets.QLabel("текст"),0,0)
        grid.addWidget(QtWidgets.QLabel("еще текст"),0,1)
        grid.setAlignment(QtCore.Qt.AlignHCenter)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        layout.addLayout(grid)
        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        y = sp.log(x, 10) - 7 / (2 * x + 6)  # функция

        f = sp.lambdify(x, y)
        self._show()

    def _show(self, func, start, end, count = 100):
        fig = self.subplots()
        x = self.linspace(start, end, count)
        self.plot(x, func(x))
        # X = 0
        l = lambda x: x * 0
        plt.plot(np.linspace(start, end, count), l(np.linspace(start, end, count)))
        plt.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()