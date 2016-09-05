import tkinter as tk

class TopLevel(tk.Tk):
    def __init__(self, title, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(title)

    def setSize(self, size):
        self.geometry('%dx%d' % (size[0],size[1]))
        self.update()

    def setPosition(self, position):
        size = ( self.winfo_width(), self.winfo_height() )
        self.geometry("%dx%d+%d+%d" % (size[0], size[1], position[0], position[1]))
        self.update()


