import tkinter as tk
import gui.frame as myFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphFrame(myFrame.Frame):
    def __init__(self, master, IGuiController, graph, **kwargs):
        myFrame.Frame.__init__(self, master, IGuiController, **kwargs)
        self.graph = graph
        self.config(background='black')
        self.config(relief=tk.GROOVE, borderwidth=5)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.canvasFrame = tk.Frame(master=self, relief=tk.GROOVE, borderwidth=2)
        self.canvasFrame.rowconfigure(0, weight=1)
        self.canvasFrame.columnconfigure(0, weight=1)
        self.canvasFrame.grid(row=0, column=0, sticky="E,W,N,S")
        self.canvas = FigureCanvasTkAgg(figure=self.graph.figure, master=self.canvasFrame)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES)

        self.viewLocked = True
        self.viewTarget = self.graph.extents()[1]
        self.viewOffset = 1
        self.viewWidth = 10

        self.xScrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.scroll)
        self.xScrollbar.grid(row=1, column=0, sticky="E,W", columnspan=1)
        self.xScrollbar.bind("<MouseWheel>", lambda event: self.setViewWidth(event))
        view = self.calcView(self.viewTarget, self.viewOffset, self.viewWidth)
        self.setScrollbar(view[0], view[1], self.graph.span)

        self.update()

    def setScrollbar(self, min, max, span):
        if span <= 0:
            span = 1
        self.xScrollbar.set(str(min/span), str(max/span))

    def update(self):
        self.graph.update()
        if self.viewLocked:
            self.viewTarget = self.graph.extents()[1]
        view = self.calcView(self.viewTarget, self.viewOffset, self.viewWidth)
        self.setScrollbar(view[0], view[1], self.graph.span)
        self.graph.setXLimits(view[0], view[1])
        self.canvas.draw()
        self.after(100, self.update)

    def calcView(self, target, offset, width):
        viewMax = int(target * offset)
        viewMin = viewMax - width
        return viewMin, viewMax

    def scroll(self, *args):
        if args[0] == "scroll":
            self.viewOffset += float(args[1]) * 0.02
        if args[0] == "moveto":
            self.viewOffset = float(args[1]) + self.viewWidth/self.graph.span
        if self.viewOffset > 1.0:
            self.viewOffset = 1.0
        if self.viewOffset < 0:
            self.viewOffset = 0

    def setViewWidth(self, event):
        if event.delta > 0:
            self.viewWidth -= int(event.delta * 0.0001 * self.graph.span)
        else:
            self.viewWidth -= int(event.delta * 0.0001 * self.graph.span)
        if self.viewWidth < 10:
            self.viewWidth = 10
        if self.viewWidth > self.graph.span:
            self.viewWidth = self.graph.span
