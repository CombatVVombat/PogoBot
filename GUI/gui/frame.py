import tkinter as tk


class Frame(tk.Frame):
    IGuiController = None

    def __init__(self, master, IGuiController, **kwargs):
        tk.Frame.__init__(self, master=master, **kwargs)
        self.IGuiController = IGuiController

