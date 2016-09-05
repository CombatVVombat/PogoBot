from tkinter import *
from tkinter import ttk

class Window():
    root = None
    canvas = []
    widgets = []
    def __init__(self, title, task):
        self.root = Tk()
        self.root.title(title)

    def addWidget(self, widget):
        self.widgets.append(widget)

    def addCanvas(self, canvas):
        self.canvas.append(canvas)

    def update(self):
        for c in self.canvas:
            c.draw()
        self.root.mainloop()
        
        


