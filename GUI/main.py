import gui as guiModule
import serialports as serialPortModule

# Create Base GUI Window
gui = guiModule.TopLevel("Pogo GUI")
gui.setSize((800,600))
gui.setPosition((500,300))

# Create GUI Controller (Handles exchange between GUI and objects which need to be controlled by the GUI)
guiController = guiModule.Controller()
portManager = serialPortModule.PortManager(guiController)

# Create GUI Frames
gui.addFrame('portSelectFrame', guiModule.PortSelectFrame(gui, guiController))



### Fix this shit
print(guiController.variables['portList'])
portManager.refreshPortList()
print(guiController.variables['portList'])


gui.mainloop()
