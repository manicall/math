import numpy as np
import matplotlib.pyplot as plt
def create_graphic(func, start, end, count=100):
    fig = plt.subplots()
    x = np.linspace(start, end, count)
    plt.plot(x, func(x))
    # X = 0
    l = lambda x: x * 0
    plt.plot(np.linspace(start, end, count), l(np.linspace(start, end, count)))
    plt.show()


