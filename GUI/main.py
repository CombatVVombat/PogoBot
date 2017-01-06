import gui as guiModule
import serialports as serialPortModule
import graph as graphModule
import datasource as dataSourceModule
import fileIO as fileIOModule

# Create Base GUI Window
gui = guiModule.TopLevel("Pogo GUI")
gui.setSize((800,600))
gui.setPosition((500,300))


# Create GUI Controller (Handles exchange between GUI and objects which need to be controlled by the GUI)
guiController = guiModule.Controller()
guiController.debugPrint = False
portManager = serialPortModule.PortManager(guiController)


# Create Graph to handle data & data ranges
# TODO Graph should be supplied with a data source for each channel.  It should not need to know how to decode data.
graph = graphModule.Graph(guiController)
dataFromFile = dataSourceModule.DatasourceList()
dataFromStream = dataSourceModule.DatasourceList()  # TODO make bytestream datasource type
#graph.addDataSource(dataFromFile)
#graph.addDataSource(dataFromStream)
fileIO = fileIOModule.FileIO(guiController, dataFromFile)


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


def task():
    updateGraphFrame()  # update the graph's canvas, view, & sliders
    graph.update()      # update the graph itself
    gui.after(10, task)

# Run mainloop
gui.after(10, task)
gui.mainloop()


