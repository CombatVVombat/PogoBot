import tkinter as tk
from tkinter import ttk
import gui.frame as myFrame


class PortSelectFrame(myFrame.Frame):
    def __init__(self, master, IGuiController, **kwargs):
        myFrame.Frame.__init__(self, master, IGuiController, **kwargs)
        self.config(background='grey')
        self.config(width=200, height=100)
        self.config(relief=tk.GROOVE, borderwidth=5)

        self.refreshBtn = tk.Button(self, text="Scan Ports")
        self.refreshBtn.grid(row=0, column=0)
        self.refreshBtn.configure(command=lambda: self.IGuiController.runCommand('refreshPortList'))

        self.portComboBox = ttk.Combobox(self, width = 20)
        self.portComboBox.grid(row=0, column=1)

        ####
        self.portComboBox.configure(values=list(self.IGuiController.variables['portList']))
        ### How to update variables?  Who does it?

        self.portSettingsFrame = ttk.LabelFrame(self)
        self.portSettingsFrame.grid(row=1, column=0, columnspan=2, sticky="N,S,E,W")

        self.togglePortBtn = tk.Button(self, text="Open Port")
        self.togglePortBtn.grid(row=2, column=0, columnspan=2, sticky="E,W")
        self.togglePortBtn.configure(command=lambda: self.IGuiController.runCommand('togglePort'))

        self.portConfigLabels = []
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Buadrate"))
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="ByteSize"))
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Parity"))
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Stop Bits"))
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Timeout"))

        self.portConfigEntrys = []

        for n, label in enumerate(self.portConfigLabels):
            self.portConfigEntrys.append(tk.Entry(self.portSettingsFrame, text=""))
            label.grid(row=n, column=0)

        for n, entry in enumerate(self.portConfigEntrys):
            entry.grid(row=n, column=1)

    def disablePortConfig(self):
        for child in self.portSettingsFrame.children.values():
            child.configure(state='disable')

    def enablePortConfig(self):
        for child in self.portSettingsFrame.children.values():
            child.configure(state='enable')


