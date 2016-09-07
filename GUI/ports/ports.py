import serial.tools.list_ports

def refreshPortList():
    portList = []
    portInfoList = serial.tools.list_ports.comports()
    for portInfo in portInfoList:
        portList.append(portInfo[0])
    return portList

def togglePort():
    # If port is closed, try to open it
    """if portOpen.get() == 0:
        ser.close()
        portOpenBox['text'] = "Port Closed"
        baudBox.state(['!disabled'])
        portCombo.state(['!disabled'])
    else:
        ser.baudrate = baud.get()
        ser.port = selectedPort.get()
        try:
            ser.open()
            portOpenBox['text'] = "Port Open"
            print(ser.name + " opened.")
            baudBox.state(['disabled'])
            portCombo.state(['disabled'])
        except serial.SerialException as e:
            print(e)
            ser.close()
            portOpen.set(0)
            portOpenBox['text'] = "Port Closed"
            baudBox.state(['!disabled'])
            portCombo.state(['!disabled'])"""

"""def readFromPort():
    bytesRead = 0
    global rawByteStream
    if portOpen.get() == 1:
        while ser.inWaiting() > 0:
            rawByteStream.extend(ser.read())
            bytesRead = bytesRead + 1
    return bytesRead"""
