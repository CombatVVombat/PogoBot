import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from .channel import Channel
import random
matplotlib.use("TkAgg")


class Graph():
    figure = None
    channels = []
    span = 1

    def __init__(self, IGuiController):
        # Setup Plotting Figure & Subplot
        plt.ion
        self.figure = Figure(dpi=100)
        self.figure.set_size_inches(7, 3.5)
        self.subplot = self.figure.add_subplot(111)
        self.setXLimits(0,100)
        self.setYLimits(-128,127)

        # Create channels.  Channels handle their own lines (so they need the subplot)
        colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'orange', 'black', 'chartreuse']
        for n in range(0,8):
            self.channels.append(Channel(self.subplot, colors[n]))

        self.IGuiController = IGuiController
        self.IGuiController.bindCommand('setChannelState', self.setChannelState)

        ### TEMPORARY ###
        self.tempData = list(range(-10, 10))
        for n, channel in enumerate(self.channels):
            channel.setData(self.tempData)
        #################

    def update(self):
        ### Temporary ####
        self.tempData.append(random.randrange(-10,10))

        self.span = self.updateSpan()
        for channel in self.channels:
            channel.update()

    def setChannelState(self, channel, state):
        #print('Graph::toggleChannel ' + str(channel) + ' ' + str(state))
        if 0 <= channel < len(self.channels):
            self.channels[channel].active = state
        else:
            print("Graph::setChannelState channel doesn't exist.")

    def updateSpan(self):
        span = self.xMax()
        return span

    def xMin(self):
        xMin = 0
        for channel in self.channels:
            x = channel.xMin()
            if x < xMin:
                xMin = x
        return xMin

    def xMax(self):
        xMax = 1
        for channel in self.channels:
            if channel.active:
                x = channel.xMax()
                if x > xMax:
                    xMax = x
        return xMax

    def yMin(self):
        yMin = 0
        for channel in self.channels:
            y = channel.yMin()
            if y < yMin:
                yMin = y
        return yMin

    def yMax(self):
        yMax = 1
        for channel in self.channels:
            y = channel.yMax()
            if y > yMax:
                yMax = y
        return yMax

    def setXLimits(self, min, max):
        self.subplot.set_xlim(min, max)

    def setYLimits(self, min, max):
        self.subplot.set_ylim(min, max)



