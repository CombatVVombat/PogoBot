

class Channel:
    active = 0
    color = 'r'
    dataHandle = None
    line = None

    def __init__(self, parentSubplot, color):
        self.color = color
        self.line = parentSubplot.plot([],[],self.color)[0] #Take zeroeth index because subplot returns a tuple

    def setData(self, dataHandle):
        self.dataHandle = dataHandle

    def update(self):
        if self.active and self.dataHandle:
                xdata = list(range(0, len(self.dataHandle)))
                self.line.set_xdata(xdata)
                self.line.set_ydata(self.dataHandle.get())
        else:
            self.line.set_xdata(0)
            self.line.set_ydata(0)

    def xMin(self):
        return 0

    def xMax(self):
        if self.dataHandle:
            return len(self.dataHandle)
        else:
            return 0

    def yMin(self):
        if self.dataHandle:
            return min(self.dataHandle)
        else:
            return 0

    def yMax(self):
        if self.dataHandle:
            return max(self.dataHandle)
        else:
            return 0


