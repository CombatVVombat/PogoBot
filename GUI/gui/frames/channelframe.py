import tkinter as tk
import gui.frame as myFrame


class ChannelFrame(myFrame.Frame):
    def __init__(self, master, IGuiController, **kwargs):
        myFrame.Frame.__init__(self, master, IGuiController, **kwargs)
        self.config(background='grey')
        self.config(relief=tk.GROOVE, borderwidth=5)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)

        self.enableLabel = tk.Label(self, text="Enable/Disable")
        self.enableLabel.grid(row=0, column=0, sticky="E,W")
        self.numBytesLabel = tk.Label(self, text="Bytes")
        self.numBytesLabel.grid(row=0, column=1, sticky="E,W")
        self.signedLabel = tk.Label(self, text="Signed")
        self.signedLabel.grid(row=0, column=2, sticky="E,W")
        self.numBytesSpinners = []
        self.enableCheckVars = []
        self.enableCheckBoxes = []
        self.signedCheckBoxes = []
        color = ['blue', 'green', 'red', 'cyan', 'magenta', 'orange', 'black', 'chartreuse']
        for i in range(0,8):
            label = "Channel " + str(i+1)
            self.enableCheckVars.append(tk.IntVar())
            self.enableCheckBoxes.append(tk.Checkbutton(self, text=label, fg=color[i],
                                                        width=10, variable=self.enableCheckVars[-1]))
            self.numBytesSpinners.append(tk.Spinbox(self, values=[1,2,3,4,5,6,7,8], width=4))
            self.signedCheckBoxes.append(tk.Checkbutton(self, width=4))
            self.enableCheckBoxes[-1].grid(row=i+1, column=0)
            self.numBytesSpinners[-1].grid(row=i+1, column=1, sticky="N,S")
            self.signedCheckBoxes[-1].grid(row=i+1, column=2, sticky="N,S,E,W")
            self.enableCheckBoxes[-1].configure(command=
                                                lambda i=i, s=self.enableCheckVars[-1]:
                                                self.IGuiController.runCommand('setChannelState', i, s.get()))
        self.enableCheckBoxes[0].select()
        self.IGuiController.runCommand('setChannelState', 0, 1)

