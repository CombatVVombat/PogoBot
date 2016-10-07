import tkinter as tk
import gui.frame as myFrame


class EncodingFrame(myFrame.Frame):
    def __init__(self, master, IGuiController, **kwargs):
        myFrame.Frame.__init__(self, master, IGuiController, **kwargs)
        self.config(background='grey')
        self.config(relief=tk.GROOVE, borderwidth=5)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)

        self.encodeCheckBox = tk.Checkbutton(self, text="COBS Encoded", width=12, anchor="w")
        self.checksumCheckBox = tk.Checkbutton(self, text="Checksum", width=12, anchor="w")
        self.encodeCheckBox.grid(row=0, column=0, sticky="W")
        self.checksumCheckBox.grid(row=1, column=0, sticky="W")

        self.encodeCheckBox.select()

