import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
matplotlib.use("TkAgg")


class Graph():
    figure = None
    datasets = []
    lines = []
    span = 0

    def __init__(self, IGuiController):
        plt.ion
        self.figure = Figure(dpi=100)
        self.figure.set_size_inches(7, 3.5)
        self.subplot = self.figure.add_subplot(111)
        self.subplot.set_xlim([0,100])
        self.subplot.set_ylim([-128,127])
        self.IDataSources = []
        self.activeDataSource = 0
        self.IGuiController = IGuiController
        self.IGuiController.bindCommand('setDataSource', self.setDataSource)
        self.IGuiController.bindCommand('toggleChannel', self.toggleChannel)
        self.channelState = [0, 0, 0, 0, 0, 0, 0, 0]
        self.lines = self.subplot.plot([],[],'r',[],[],'g',[],[],'b',[],[],'c',[],[],'k',[],[],'m',[],[],'y',[],[],'g')

    def update(self):
        self.span = self.xSpan()
        for n, line in enumerate(self.lines):
            if self.channelState[n] == 1:
                line.set_xdata(range(-10,10))
                line.set_ydata(range(-10,10))
            else:
                line.set_xdata(0)
                line.set_ydata(0)

    def toggleChannel(self, channel, state):
        print('Graph::toggleChannel ' + str(channel) + ' ' + str(state))
        self.channelState[channel] = state

    def addDataSource(self, IDataSource):
        self.IDataSources.append(IDataSource)

    def setDataSource(self, index):
        if index >= 0 and index < len(self.IDataSources):
            print("Graph::setDataSource: " + str(index))
            self.activeDataSource = index
            self.datasets.clear()
            self.datasets.append(self.IDataSources[index])
        else:
            print("Graph::setDataSource index out of bounds.")

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



