import tkinter as tk
from tkinter import filedialog
import gui.frame as myFrame


class FileLoadingFrame(myFrame.Frame):
    def __init__(self, master, IGuiController, **kwargs):
        myFrame.Frame.__init__(self, master, IGuiController, **kwargs)
        self.config(background='grey')
        self.config(relief=tk.GROOVE, borderwidth=5)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)

        self.openFileBtn = tk.Button(self, text="Open", command=self.openFile, width=10)
        self.openFileBtn.grid(row=0, column=0)
        self.saveFileBtn = tk.Button(self, text="Save", command=self.saveFile, width=10)
        self.saveFileBtn.grid(row=1, column=0)
        self.saveAsFileBtn = tk.Button(self, text="Save As...", command=self.saveAsFile, width=10)
        self.saveAsFileBtn.grid(row=2, column=0)

    def openFile(self):
        filename = filedialog.askopenfilename()
        self.IGuiController.runCommand("openfile", filename)

    def saveFile(self):
        pass

    def saveAsFile(self):
        self.filename = filedialog.asksaveasfile()

    def enable(self):
        for child in self.children.values():
            child.configure(state='active')

    def disable(self):
        for child in self.children.values():
            child.configure(state='disable')