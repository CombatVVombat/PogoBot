from Serial.ports import *
from GUI.gui import *
from GUI.buildGUI import *
from GUI.canvas import *
from matplotlib.figure import Figure

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")



serial = serial.Serial(port=                None,
                       baudrate=            9600,
                       bytesize=            serial.EIGHTBITS,
                       parity=              serial.PARITY_NONE,
                       stopbits=            serial.STOPBITS_ONE,
                       timeout=             None,
                       xonxoff=             False,
                       rtscts=              False,
                       dsrdtr=              False)

def task():
    canvas.draw()


window = Window("Pogo GUI", task)
buildGUI(window)

figure = Figure(figsize=(5,4), dpi=100)
graph = figure.add_subplot(111)
window.addCanvas(buildCanvas(figure, window.root))


window.update()













