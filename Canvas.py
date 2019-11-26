from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import random
class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 70, test=False):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        
        self.setParent(parent)
        
        self.ax = self.figure.add_subplot(111)
        if not test:
            self.plot()
        else:
            self.myplot()
 
 
    def plot(self):
        self.ax.clear()
        data = [random.random() for i in range(25)]
        self.ax.plot(data, 'r-')
        self.ax.set_title("bla")

        self.ax.set(xlabel='testx', ylabel='texty')

    def myplot(self):
        self.ax.clear()
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        self.ax.plot(data)

    def clear(self):
        self.ax.clear()
 