from numpy import arange, sin
from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
from timeit import default_timer as timer
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Serial.ports import *


root = Tk()
root.title("POGOBOT GUI")

ser = serial.Serial()
ser.timeout = 0
portList = []
portOpen = BooleanVar()
portOpen.set(0)
selectedPort = StringVar()
selectedPort.set("None")
bytesRead = StringVar()
bytesRead.set("Bytes Read: ")
bpsValue = StringVar()
window = IntVar()
window.set(1000)
bpsValue.set("bps: ")
timeValue = StringVar()
timeValue.set("Frame Time (ms): ")
lastTime = 0
baud = IntVar()
baud.set(57600)

XaxisMin = 0
XaxisMax = 100

rawByteStream = bytearray()
channel = [ [], [], [] ]


plt.ion()                                   #interactive mode
f = Figure(figsize=(5,4), dpi=100)          
graph = f.add_subplot(111)
graph.axis([0, 1000, 0, 65000])
line0, = graph.plot(channel[0])
line1, = graph.plot(channel[1])
line2, = graph.plot(channel[2])



def buildPacket(frameLength):
    #frameLength = number of data bytes in frame, not counting zero delimeter
    global rawByteStream
    packet = bytearray()
    if len(rawByteStream) > frameLength:    # need enough bytes to build a packet
        for i in rawByteStream:
            if(i == 0):
                break
            else:
                packet.append(i)
        if len(packet) != frameLength:      # started in the middle of a frame, discard
            del rawByteStream[0:len(packet)+1]
        else:
            del rawByteStream[0:len(packet)+1]
            return packet

def checkEncoding(packet):
    i = 0
    count = 0
    n = 0
    while n < len(packet):
        i = i + 1
        count = count + packet[n]
        n = n + packet[n]
    if count == len(packet):
        return True
    else:
        print("Bad Packet")
        return False

def printPacket(packet):
    packetString = ""
    for i in range(0, len(packet)):
        packetString+=str(packet[i])
        packetString+=","
    print("Packet: " + packetString)    
    
def decode(packet):
    decoded = bytearray()
    n = 0
    while n < len(packet):
        code = packet[n]
        if code == 1:
            decoded.append(0)
            n = n + 1
        else:
            q = 0
            while q < code-1:
                q = q + 1
                n = n + 1
                if n >= len(packet):
                    n = len(packet)-1
                decoded.append(packet[n])
            decoded.append(0)
            n = n + 1

    if len(decoded) != len(packet):
        print("PacketLength = " + str(len(packet)))
        printPacket(packet)
        print("DecodedLength = " + str(len(decoded)))
        printPacket(decoded)
        raise ValueError("Decoded packet length does not match input packet length")
    return decoded

def castValue(packet, index, numBytes, signed):
    a = bytearray()
    a = packet[index:index+numBytes]
    b = int.from_bytes(a, byteorder='little', signed=signed)
    return b
    
def task():
    numRead = readFromPort()  # pulls values from serial buffer and appends them to rawByteStream
    bytesRead.set("Bytes Read: " + str(numRead))
    while len(rawByteStream) > 11:
        packet = buildPacket(11)   # assembles a packet from the rawByteStream, removes the bytes from rawByteStream once used
        if packet:
            if checkEncoding(packet):
                packet = decode(packet)
                channel[0].append( castValue(packet, 0, 4, True) )
                channel[1].append( castValue(packet, 4, 4, True) )
                channel[2].append( castValue(packet, 8, 2, True) )

    global window
    numSamples = len(channel[0])
    XaxisMax = numSamples
    if XaxisMax < window.get():
        XaxisMax = window.get()
    XaxisMin = XaxisMax - window.get()
    if XaxisMin < 0:
        XaxisMin = 0
        
    graph.axis([XaxisMin, XaxisMax, -2000, 2000])
    #line0.set_xdata(arange(0, len(channel[0])))
    #line0.set_ydata(channel[0])
    #line1.set_xdata(arange(0, len(channel[1])))
    #line1.set_ydata(channel[1])
    line2.set_xdata(arange(0, len(channel[2])))
    line2.set_ydata(channel[2])
    canvas.draw()

    thisTime = timer()
    global lastTime
    deltaTime = (thisTime-lastTime)
    timeValue.set("Frame Time (ms): " + str(1000*(deltaTime)))
    bpsValue.set("bps: " + str(8*numRead/deltaTime))
    lastTime = thisTime;
    root.after(1, task)



############ UI SETUP #############    
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=(N,W,E,S))

### THE CHART
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.show()
canvas.get_tk_widget().grid(column=0, row=6, sticky=(N,W,E,S))
#

### PORT SELECT & REFRESH BUTTON
refreshPortsButton = ttk.Button(frame, text="Refresh Ports", command=refreshPorts)
portLabel = ttk.Label(frame, text="PORT")
portCombo = ttk.Combobox(frame, width = 20, textvariable=selectedPort, values=portList)
#
portLabel.grid(column=1, row=1, sticky=E)
portCombo.grid(column=2, row=1, sticky=(E,W))
refreshPortsButton.grid(column=3, row=1, sticky=(E,W))
###

### PORT OPEN/CLOSE CHECKBOX
portOpenBox = ttk.Checkbutton(frame, text="Port Closed", variable=portOpen, command=togglePort)
portOpenBox.grid(column=2, row=3, sticky=W)
###

### BAUD RATE SELECTION
baudLabel = ttk.Label(frame, text="BUAD")
baudBox = ttk.Entry(frame, width=6, textvariable=baud)
#
baudLabel.grid(column=1, row=2, sticky=E)
baudBox.grid(column=2, row=2, sticky=W)
###

### BYTE COUNTER (PER FRAME)
bytesReadLabel = ttk.Label(frame, width = 15, textvariable=bytesRead)
bpsLabel = ttk.Label(frame, width = 15, textvariable=bpsValue)
#
bpsLabel.grid(column=2, row=5, sticky=E)
bytesReadLabel.grid(column=2, row=4, sticky=E)
###

### FRAME TIMER
timeLabel = ttk.Label(frame, width=20, textvariable=timeValue)
timeLabel.grid(column=2, row=4)
#

### CHART WINDOW SLIDER
windowLabel = ttk.Label(frame, width=15, textvariable=window)
windowSlider = ttk.Scale(frame, orient=HORIZONTAL, length = 200, from_=10, to=10000, variable=window)
windowSlider.grid(column=4, row=10)
windowLabel.grid(column=4, row=9)




root.after(1, task)
root.mainloop()
