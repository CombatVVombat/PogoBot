from gui import *
from ports.ports import *


gui = TopLevel("Pogo GUI")
gui.setSize((800,600))
gui.setPosition((500,300))

portList = refreshPorts()
portSelectFrame = PortSelectFrame(gui)
portSelectFrame.grid()


#c = tk.Canvas(gui, width=200, height=100)
#c.config(background='black')
#c.grid()

gui.mainloop()
