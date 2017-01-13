import gui as guiModule
import serialports as serialPortModule
import graph as graphModule
import datasource as dataSourceModule
import fileIO as fileIOModule
import encoding as encodingModule

# Create Base GUI Window
gui = guiModule.TopLevel("Pogo GUI")
gui.setSize((800,600))
gui.setPosition((500,300))


# Create GUI Controller (Handles exchange between GUI and objects which need to be controlled by the GUI)
guiController = guiModule.Controller()
guiController.debugPrint = False
portManager = serialPortModule.PortManager(guiController)


# Encoding/Decoding things
packetizer = encodingModule.Packetizer(guiController)


# Create Graph to handle data & data ranges
graph = graphModule.Graph(guiController)
plotDataChannel = []
for n in range(0,8):
    plotDataChannel.append(dataSourceModule.DatasourceList())
    graph.setChannelData(n, plotDataChannel[n])

fileIO = fileIOModule.FileIO(guiController)
#Sample Capture.txt = 4bytes, 4bytes, 2 bytes, 1 byte, 0 delimeter cobs encoded


# Create GUI Frames
gui.addFrame('portSelectFrame', guiModule.PortSelectFrame(gui, guiController))
gui.addFrame('graphFrame', guiModule.GraphFrame(gui, guiController, graph))
updateGraphFrame = gui.getFrame('graphFrame').update    #avoid looking up 'graphFrame' every frame
gui.addFrame('fileLoadingFrame', guiModule.FileLoadingFrame(gui, guiController))
gui.addFrame('encodingFrame', guiModule.EncodingFrame(gui, guiController))
gui.addFrame('channelFrame', guiModule.ChannelFrame(gui, guiController))


# Layout of GUI Frames
gui.getFrame('graphFrame').grid(row=0, column=0, sticky="N,S,E,W", columnspan=4)
gui.getFrame('portSelectFrame').grid(row=1, column=0, sticky="N,S,E", columnspan=1)
gui.getFrame('fileLoadingFrame').grid(row=1, column=1, sticky="N,S,W", columnspan=1)
gui.getFrame('encodingFrame').grid(row=1, column=2, sticky="N,S,W", columnspan=1)
gui.getFrame('channelFrame').grid(row=1, column=3, sticky="N,S,W", columnspan=1)


# Define repeated mainloop task
def task():
    updateGraphFrame()  # update the graph's canvas, view, & sliders
    graph.update()      # update the graph itself
    gui.after(10, task)


# Run mainloop
gui.after(10, task)
gui.mainloop()


