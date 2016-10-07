import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
matplotlib.use("TkAgg")


class Graph():
    figure = None
    datasets = []
    lines = []
    span = 0

    def __init__(self):
        plt.ion
        self.figure = Figure(dpi=100)
        self.figure.set_size_inches(7, 3.5)
        self.subplot = self.figure.add_subplot(111)
        self.subplot.set_xlim([0,100])
        self.subplot.set_ylim([-128,127])

    def update(self):
        for n, dataset in enumerate(self.datasets):
            self.lines[n].set_xdata(range(0,dataset.len()))
            self.lines[n].set_ydata(dataset.get())
            self.span = self.xSpan()

    def addChannel(self, IDatasource):
        self.datasets.append(IDatasource)
        line, = self.subplot.plot([])
        self.lines.append(line)
        self.lines[-1].set_xdata(range(0, IDatasource.len()))
        self.lines[-1].set_ydata(IDatasource.get())

    def xSpan(self):
        span = 0
        for dataset in self.datasets:
            x = dataset.len()
            if x > span:
                span = x
        return span-1

    def extents(self):
        xLimits = [0,0]
        yLimits = [0,0]
        for dataset in self.datasets:
            x = dataset.len()
            if x > 0:
                y = max(dataset.get())
            else:
                y = 0
            if x > xLimits[1]:
                xLimits[1] = x
            if y > yLimits[1]:
                yLimits[1] = y
            if y < yLimits[0]:
                yLimits[0] = y
        return [xLimits[0], xLimits[1]-1, yLimits[0], yLimits[1]]

    def setXLimits(self, min, max):
        self.subplot.set_xlim(min, max)

    def setYLimits(self, min, max):
        self.subplot.set_ylim(min, max)



