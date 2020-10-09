import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
import sys
def create_graphic(func, start, end, count=100):
    fig = plt.subplots()
    x = np.linspace(start, end, count)
    plt.plot(x, func(x))
    # X = 0
    l = lambda x: x * 0
    plt.plot(np.linspace(start, end, count), l(np.linspace(start, end, count)))
    plt.show()

def show_result(root_value, check_value):
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMessageBox(0, "результат",
                                   "корень: " + str(root_value) + "\nпроверка: " + str(check_value))
    dialog.exec_()

