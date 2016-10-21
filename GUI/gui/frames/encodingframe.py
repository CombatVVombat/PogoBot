import tkinter as tk
import gui.frame as myFrame
import gui.combobox as myComboBox


class EncodingFrame(myFrame.Frame):
    def __init__(self, master, IGuiController, **kwargs):
        myFrame.Frame.__init__(self, master, IGuiController, **kwargs)
        self.config(background='grey')
        self.config(relief=tk.GROOVE, borderwidth=5)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)

        self.sourceSelectLabel = tk.Label(self, text="Source: ", width=7)
        self.sourceSelectCombo = myComboBox.Combobox(self, width=8, value=['File', 'Stream'])
        self.sourceSelectCombo.current(0)
        self.encodeCheckBox = tk.Checkbutton(self, text="COBS Encoded", width=16, anchor="w")
        self.checksumCheckBox = tk.Checkbutton(self, text="Checksum", width=16, anchor="w")
        self.sourceSelectLabel.grid(row=0, column=0, stick="W")
        self.sourceSelectCombo.grid(row=0, column=1, sticky="W")
        self.encodeCheckBox.grid(row=1, column=0, sticky="W", columnspan=2)
        self.checksumCheckBox.grid(row=2, column=0, sticky="W", columnspan=2)
        self.encodeCheckBox.select()

        self.sourceSelectCombo.onSelect(lambda x: self.IGuiController.runCommand('setDataSource', self.sourceSelectCombo.current()))
