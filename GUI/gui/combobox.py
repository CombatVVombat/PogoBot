from tkinter import ttk


class Combobox(ttk.Combobox):
    def __init__(self, master, **kwargs):
        ttk.Combobox.__init__(self, master=master, **kwargs)

    def updateList(self, list):
        self.configure(values=list)

    def onDropdown(self, func):
        self.configure(postcommand=func)

    def onSelect(self, func):
        self.bind("<<ComboboxSelected>>", func)