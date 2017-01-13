import tkinter as tk
from tkinter import ttk
import gui.frame as myFrame
import gui.combobox as myComboBox


class PortSelectFrame(myFrame.Frame):
    def __init__(self, master, IGuiController, **kwargs):
        myFrame.Frame.__init__(self, master, IGuiController, **kwargs)
        self.config(background='grey')
        self.config(relief=tk.GROOVE, borderwidth=5)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)

        self.refreshBtn = tk.Button(self, text="Scan Ports")
        self.refreshBtn.configure(command=lambda: self.IGuiController.runCommand('refreshPortList'))
        self.refreshBtn.grid(row=0, column=0, sticky="N,S,E,W")
        self.refreshBtn.rowconfigure(0, weight=1)

        self.portComboBox = myComboBox.Combobox(self, width=20)
        self.portComboBox.grid(row=0, column=1, sticky="N,E,W")
        self.portComboBox.onDropdown(lambda: self.portComboBox.updateList(self.IGuiController.get('portList')))
        self.portComboBox.onSelect(lambda e: self.IGuiController.runCommand('setSelectedPort', self.portComboBox.get()))

        self.portSettingsFrame = ttk.LabelFrame(self)
        self.portSettingsFrame.grid(row=1, column=0, columnspan=2, sticky="N,S,E,W")
        self.portSettingsFrame.rowconfigure(0, weight=1)

        self.togglePortBtn = tk.Button(self, text="Open Port")
        self.togglePortBtn.grid(row=2, column=0, columnspan=2, pady=1, sticky="N,S,E,W")
        self.togglePortBtn.configure(command=lambda: self.IGuiController.runCommand('togglePort'))
        self.togglePortBtn.rowconfigure(0, weight=1)

        # Create combo boxes for port configuration
        self.portConfigLabels = []
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Baudrate"))
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Byte Size"))
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Parity"))
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Stop Bits"))
        self.portConfigLabels.append(tk.Label(self.portSettingsFrame, text="Timeout"))
        self.portConfigCombos = {}
        for n, label in enumerate(self.portConfigLabels):
            label.grid(row=n, column=0, sticky="N,S")
            labelText = label.cget("text")
            self.portConfigCombos[labelText] = myComboBox.Combobox(self.portSettingsFrame)
            self.portConfigCombos[labelText].grid(row=n, column=1, sticky="N,S")
            self.IGuiController.createVariable(labelText)
            self.portConfigCombos[labelText].onSelect(lambda x, y=labelText:self.IGuiController.set(y, self.portConfigCombos[y].get()))

        # Set combo box default values & default current value
        self.portConfigCombos["Baudrate"].configure(value=[4800,9600,19200,38400,57600,115200,230400,460800,500000])
        self.portConfigCombos["Baudrate"].current(1)
        self.portConfigCombos["Byte Size"].configure(value=[5,6,7,8])
        self.portConfigCombos["Byte Size"].current(3)
        self.portConfigCombos["Parity"].configure(value=["None", "Even", "Odd", "Mark", "Space"])
        self.portConfigCombos["Parity"].current(0)
        self.portConfigCombos["Stop Bits"].configure(values=["1", "2"])
        self.portConfigCombos["Stop Bits"].current(0)
        self.portConfigCombos["Timeout"].configure(values=["None", "Non-Blocking", "1 second", "2 seconds", "5 seconds"])
        self.portConfigCombos["Timeout"].current(0)

        # Update GUI values to combos box default values
        for label in self.portConfigCombos:
            self.IGuiController.set(label, self.portConfigCombos[label].get())

        # Bind disable/enable of the port config combos
        self.IGuiController.bindCommand("disablePortConfig", self.disablePortConfig)
        self.IGuiController.bindCommand("enablePortConfig", self.enablePortConfig)

    def disablePortConfig(self):
        self.togglePortBtn.configure(text="Close Port")
        for child in self.portSettingsFrame.children.values():
            child.configure(state='disable')

    def enablePortConfig(self):
        self.togglePortBtn.configure(text="Open Port")
        for child in self.portSettingsFrame.children.values():
            child.configure(state='active')


