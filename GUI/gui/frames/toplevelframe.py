import tkinter as tk


class TopLevel(tk.Tk):
    def __init__(self, title, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(title)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    frames = {}

    def setSize(self, size):
        self.geometry('%dx%d' % (size[0],size[1]))
        self.update()

    def setPosition(self, position):
        size = ( self.winfo_width(), self.winfo_height() )
        self.geometry("%dx%d+%d+%d" % (size[0], size[1], position[0], position[1]))
        self.update()

    def addFrame(self, title, frame):
        self.frames[title] = frame

    def getFrame(self, title):
        frame = self.frames.get(title)
        if frame is not None:
            return frame
        else:
            print("TopLevel:GetFrame: '" + title + "' not found.")
